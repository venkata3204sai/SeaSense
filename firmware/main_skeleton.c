/* firmware/main_skeleton.c
 * Copied verbatim from docs/stage3-electronics-v1.0.md §5 (frozen 2026-11-14).
 * Concept skeleton only: not compiled, not tested. Helper functions are not implemented.
 */
/* SeaSense main cycle — concept skeleton (traceability in comments) */
void main(void) {
    hw_init(); store_init(); lora_join_otaa(); imu_start_background(); /* R-37, DO flags */
    for (;;) {
        sched_wait_next();                       /* RTC alarm: interval_min (R-05) */
        cycle_t c = {0};
        bool fix_due = trial_mode ? (c_count % 10 == 0) : true;   /* Assumption 9 */
        if (fix_due) gnss_power(true);           /* hot start with V_BCKP (R-06) */

        ports_rail12(true);                      /* 12 V boost + per-port switches (R-15) */
        c.temp = modbus_read_temp(ADDR_TEMP);                     /* R-01 */
        modbus_write_comp(ADDR_EC, c.temp);  c.cond = modbus_read_ec(ADDR_EC);
        c.sal  = pss78(c.cond, c.temp, 0.0);                      /* R-02 */
        modbus_write_comp(ADDR_DO, c.temp, c.sal);
        bool burst = do_burst_due();             /* every sample; hourly in 90-d profile (P-2) */
        c.do_mgl = burst ? do_burst(ADDR_DO, 10, 30 /*s*/, &c.do_trend) /* R-03 */
                         : modbus_read_do(ADDR_DO);
        if (port_fitted(TURB)) c.turb = modbus_read_turb(ADDR_TURB); /* R-04 */
        ports_rail12(false);                     /* ports on ~6 % of the time */

        if (fix_due) { c.fix = gnss_wait_fix(30 /*s*/); gnss_power(false); }
        c.batt = fuelgauge_read();  c.can = bme280_read();        /* R-10 */
        c.acc_rms = imu_rms_60s();  imu_wave_latest(&c.hs, &c.tp); /* R-37 */

        c.flags = qc_flags(&c);                  /* DO_LOW_MOTION, DO_DEPLETION_SUSPECT, LEAK, DISPLACED (R-09/10/11) */
        rec_t r = codec_sample(&c, seq++);       /* 34 B, spec v1 */
        store_append(&r);                        /* R-08: ring log */

        if (!trial_mode || batch_full()) {
            lora_send(trial_mode ? FPORT_TRIAL : FPORT_SAMPLE, codec_out(), dc_check()); /* R-12 */
            handle_downlink();                   /* interval, trial, backfill range (R-14) */
            backfill_if_budget(dc_remaining());  /* R-08 */
        }
        if (trial_mode && trial_expired()) trial_mode = false;   /* auto-expiry */
        wdt_feed();
    }
}
void leak_isr(void)  { flag_set(LEAK); sched_wake_now(ALARM); }      /* R-10 */
void reed_isr(void)  { ble_service_window(10 * 60); }                /* R-14: DFU, config */

class ErgonomicSleepMattressCustomizationTrialTrackerClient:
    def customize_orthopedic_mattress(self, sleeper_weight_kg=78.0, sleeping_posture='side_and_back', trial_day=24):
        return {
            'mattress_configuration_id': 'wkf_mat_5519',
            'recommended_firmness_scale_1_to_10': 6.8,
            'foam_layering_composition': ['Natural Latex Comfort Layer', 'Aeroflow Memory Foam', 'High-Resilience Orthopedic Core'],
            'active_100_night_trial_days_remaining': max(100 - trial_day, 0),
            'sleep_quality_improvement_reported_pct': 38.5,
            'free_doorstep_exchange_guarantee': True
        }

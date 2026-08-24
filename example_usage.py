from client import ErgonomicSleepMattressCustomizationTrialTrackerClient

def main():
    client = ErgonomicSleepMattressCustomizationTrialTrackerClient()
    res = client.customize_orthopedic_mattress(85.0, 'back_sleeper', 15)
    print('Config: ' + res['mattress_configuration_id'] + ' | Firmness: ' + str(res['recommended_firmness_scale_1_to_10']) + '/10')
    print('Trial Remaining: ' + str(res['active_100_night_trial_days_remaining']) + ' nights (100-Night Free Trial)')
    print('Layers: ' + ' + '.join(res['foam_layering_composition']))

if __name__ == '__main__':
    main()

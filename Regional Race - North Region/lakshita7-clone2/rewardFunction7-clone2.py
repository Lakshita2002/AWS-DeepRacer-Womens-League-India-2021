def reward_function(params):
    '''
    Example that penalizes steering, which helps mitigate zig-zag behaviors
    '''

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * params['track_width']
    marker_2 = 0.25 * params['track_width']
    marker_3 = 0.5 * params['track_width']

    # Give higher reward if the car is closer to center line and vice versa
    if params['distance_from_center'] <= marker_1:
        reward = 1
    elif params['distance_from_center'] <= marker_2:
        reward = 0.5
    elif params['distance_from_center'] <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 5

    # Penalize reward if the car is steering too much
    if abs(params['steering_angle']) > ABS_STEERING_THRESHOLD:  # Only need the absolute steering angle
        reward *= 0.5

    # penalize reward for the car taking slow actions
    # speed is in m/s
    # we penalize any speed less than 1.0m/s
    SPEED_THRESHOLD = 1.0
    if params['speed'] < SPEED_THRESHOLD:
        reward *= 0.5

    return float(reward)

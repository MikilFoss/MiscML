import math
def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    steering = abs(params['steering_angle'])
    x_pos = params['x']
    y_pos = params['y']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']

    heading = params['heading']

    progress = params['progress']

    reward = 1e-3

    if not all_wheels_on_track:
        return 1e-3
    
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 0.5
    elif distance_from_center <= marker_2:
        reward += 0.25
    elif distance_from_center <= marker_3:
        reward += 0.05
    else:
        reward = 1e-3

    #Promote smooth steering
    if steering < 2:
        reward += 1.5
    elif steering < 10:
        reward += 0.5
    elif steering < 15:
        reward += 0.25
    
    
    direction_waypoint = math.atan2(
    waypoints[closest_waypoints[1]][1] - waypoints[closest_waypoints[0]][1],
    waypoints[closest_waypoints[1]][0] - waypoints[closest_waypoints[0]][0])

    direction_car = math.radians(heading)

    direction_diff = abs(direction_waypoint - direction_car)

    if direction_diff < math.radians(5):
        reward += 1.5 
    elif direction_diff < math.radians(10):  
        reward += 0.75
    elif direction_diff < math.radians(15):
        reward += 0.25 
    else: 
        reward *= 0.5 # reduce reward for being too off-direction

    MAX_SPEED = 4  # Maximum car speed, this is an example value
    MIN_SPEED = 0.5  # Minimum car speed, this is an example value

    if steering > 15 and speed >(MAX_SPEED+MIN_SPEED)/2:
        reward *= 0.75
    else:
        reward *= (1 + speed / MAX_SPEED)**2

    if progress == 100:
        reward += 30

    return float(reward)
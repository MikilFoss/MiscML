import math
def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    steering = abs(params['steering_angle'])
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']

    heading = params['heading']

    progress = params['progress']

    reward = 1e-3

    if not all_wheels_on_track:
        return 1e-3

    #Promote smooth steering
    if steering < 0.5:
        reward += 3
    elif steering < 2:
        reward += 1.5
    elif steering < 10:
        reward += 0.5
    elif steering < 15:
        reward += 0.25
    
    #Reward for following waypoints
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

    

    reward *= speed

    if progress == 100:
        reward += 10

    return float(reward)
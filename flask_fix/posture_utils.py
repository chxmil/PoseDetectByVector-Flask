import math

max_distance_bow = float('-inf')

def check_bowed_pose(left_eye_y, right_eye_y, left_ear_y, right_ear_y):
    global max_distance_bow
    distance_bow = math.sqrt((left_eye_y - left_ear_y) ** 2 + (right_eye_y - right_ear_y) ** 2)

    if distance_bow > max_distance_bow:
        max_distance_bow = distance_bow
    
    return ((distance_bow / max_distance_bow) * 100)

def calculate_angle(nose, ear1, ear2):
    a = ear1[0] - ear2[0]
    b = nose[0] - ear2[0]

    x = ((a - b) / a) * 100
    angle_degrees = (0.9 * x) + 135
    return angle_degrees

def degrees_find(shoulder_LEFT, shoulder_RIGHT):
    horizontal_distance = shoulder_RIGHT.x - shoulder_LEFT.x
    vertical_distance = shoulder_RIGHT.y - shoulder_LEFT.y

    angle_radians = math.atan2(vertical_distance, horizontal_distance)
    angle_degrees = math.degrees(angle_radians)
    angle_degrees = 180 - (abs(180 - (angle_degrees % 360)))

    return angle_degrees

def calculate_posture(detect_status, head_turn, angle_degrees):
    if head_turn < (((12.673 * (angle_degrees) ** 2) - (4435.9 * angle_degrees)) + (388293)) * 0.7:
        if detect_status == 1:
            return "warning!"
        if detect_status == 0:
            return "fix your sitting position"
    else:
        if detect_status == 1:
            return "not work"
        if detect_status == 0:
            return "Right Position"

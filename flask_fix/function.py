import math
import mediapipe as mp
import cv2
import time
import matplotlib.pyplot as plt
import csv

# Initialize MediaPipe Pose solution
mp_pose = mp.solutions.pose

pose = mp_pose.Pose()
start_time = time.time()
count_time = start_time / 60
timestamp = 0
detect_status = 1111

i = 0
bowe_count = 0

# Initialize MediaPipe Drawing Utilities for visualization
mp_drawing = mp.solutions.drawing_utils

# Initialize maximum distance
max_distance = float('-inf')
max_distance_bow = float('-inf')

# Initialize CSV file and header
csv_filename = 'pose_distances_latest_000.csv'
csv_header = ['timestamp','distance', 'angle_degrees', 'bowe_sheck','head_turn','detect_status']
csv_rows = []


def check_bowed_pose(landmarks):
    global max_distance_bow  # Declare max_distance_bow as global
    nose_y = landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
    left_eye_y = landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE].y
    right_eye_y = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].y
    left_ear_y = landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].y
    right_ear_y = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].y

    distance_bow = math.sqrt((left_eye_y - left_ear_y) ** 2 + (right_eye_y - right_ear_y) ** 2)

    if distance_bow > max_distance_bow:
        max_distance_bow = distance_bow
    
    return  ((distance_bow/max_distance_bow)*100)

def calculate_angle(nose, ear1, ear2):

    a = ear1[0] - ear2[0]
    b = nose[0] - ear2[0]

    x = ((a-b)/a)*100
    angle_degrees = (0.9*x)+135
    #y=ax+b
    return angle_degrees

def degrees_find(landmarks):
    shoulder_LEFT = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
    shoulder_RIGHT = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]

    # Calculate the horizontal and vertical distances between the shoulder landmarks
    horizontal_distance = shoulder_RIGHT.x - shoulder_LEFT.x
    vertical_distance = shoulder_RIGHT.y - shoulder_LEFT.y

    # Calculate the angle using arctangent (in radians)
    angle_radians = math.atan2(vertical_distance, horizontal_distance)

    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)

    angle_degrees=180-(abs(180-(angle_degrees % 360)))

    return  (angle_degrees )


def get():
    global max_distant
    cap = cv2.VideoCapture(0)

    # Open CSV file for writing
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)

        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            # Convert the BGR image to RGB (MediaPipe uses RGB)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Process the image to get pose landmarks
            results = pose.process(image_rgb)

            # Draw the landmarks and connections on the image
            annotated_image = image.copy()  # Create a copy of the original image
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                landmarks = results.pose_landmarks

                # Calculate the distance between shoulder and mouth landmarks
                shoulder = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
                mouth = landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT]
                distance = math.sqrt((shoulder.x - mouth.x) ** 2 + (shoulder.y - mouth.y) ** 2)
                
                # Get landmarks for nose and ears
                nose = (landmarks.landmark[mp_pose.PoseLandmark.NOSE].x, landmarks.landmark[mp_pose.PoseLandmark.NOSE].y)
                left_ear = (landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].x, landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].y)
                right_ear = (landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].x, landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].y)

                # Calculate the angle formed by nose and ears
                head_turn = calculate_angle(nose, left_ear, right_ear)

                bowed_pose=check_bowed_pose(landmarks)

                angle_degrees = degrees_find(landmarks)
                #head_turn * 0.28 < ((-0.0074*angel_deegree)+1.3358)
                
                if distance > max_distance:
                    max_distance = distance
                elif distance <= 0.8 * max_distance:
                    if bowed_pose <= 40:
                        detect_status = 0
                    else:
                        bad += 1
                        bowe_count += 1
                        detect_status = 1
                else:
                    detect_status = 0
            
                if (head_turn) < (((12.673*(angle_degrees)**2)-(4435.9*angle_degrees))+(388293))*0.7:
                    #y = 12.673x^2 - 4435.9x + 388293   ((12.673*(angle_degrees)**2)-(4435.9*angle_degrees)+(388293)):)
                    if detect_status == 1:
                        return "Bowed posture"
                    if detect_status == 0:
                        return "High shoulder angle"
                else:
                    if detect_status == 1:
                        return "Poor posture (bowed & high angle)"
                    if detect_status == 0:
                        return "Good posture"

            if cv2.waitKey(5) & 0xFF == 27:
                break
    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


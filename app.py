from flask import Flask, render_template, Response, jsonify
from posture_utils import calculate_angle, check_bowed_pose, degrees_find, calculate_posture
import cv2
import mediapipe as mp
import math

app = Flask(__name__)

# Initialize global variables
detect_status = 11  # Initialize detect_status with a default value

def generate_frames():
    max_distance_bow = float('-inf')
    max_distance = float('-inf')
    global detect_status
    
    # Initialize MediaPipe Pose solution
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # Initialize MediaPipe Drawing Utilities for visualization
    mp_drawing = mp.solutions.drawing_utils  

    # Access the webcam (change the parameter to the path of a video file if needed)
    cap = cv2.VideoCapture(0)

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

            # Calculate the approximate position of the mouth
            landmarks = results.pose_landmarks.landmark
            # Approximate mouth position by taking the average of the landmarks corresponding to the lips
            mouth_x = (landmarks[mp_pose.PoseLandmark.MOUTH_LEFT].x + landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT].x) / 2
            mouth_y = (landmarks[mp_pose.PoseLandmark.MOUTH_LEFT].y + landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT].y) / 2

            # Calculate the distance between shoulder and mouth landmarks
            shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
            distance = math.sqrt((shoulder.x - mouth_x)**2 + (shoulder.y - mouth_y)**2)

            # Calculate additional posture metrics
            nose = (landmarks[mp_pose.PoseLandmark.NOSE].x, landmarks[mp_pose.PoseLandmark.NOSE].y)
            left_ear = (landmarks[mp_pose.PoseLandmark.LEFT_EAR].x, landmarks[mp_pose.PoseLandmark.LEFT_EAR].y)
            right_ear = (landmarks[mp_pose.PoseLandmark.RIGHT_EAR].x, landmarks[mp_pose.PoseLandmark.RIGHT_EAR].y)
            
            head_turn = calculate_angle(nose, left_ear, right_ear)

            left_eye_y = landmarks[mp_pose.PoseLandmark.LEFT_EYE].y
            right_eye_y = landmarks[mp_pose.PoseLandmark.RIGHT_EYE].y
            left_ear_y = landmarks[mp_pose.PoseLandmark.LEFT_EAR].y
            right_ear_y = landmarks[mp_pose.PoseLandmark.RIGHT_EAR].y
            bowed_pose , max_distance_bow= check_bowed_pose(left_eye_y, right_eye_y, left_ear_y, right_ear_y, max_distance_bow)

            shoulder_left = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
            shoulder_right = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            angle_degrees = degrees_find(shoulder_left, shoulder_right)

            # Update the global max_distance variable
            if distance > max_distance:
                max_distance = distance
            elif distance <= 0.7 * max_distance:
                if bowed_pose <= 40:
                    detect_status = 1
                else:
                    detect_status = 1
            else:
                detect_status = 0

            detect_status = calculate_posture(detect_status, head_turn, angle_degrees)

        # Encode the annotated image as JPEG
        ret, buffer = cv2.imencode('.jpg', annotated_image)
        frame = buffer.tobytes()

        # Yield the frame as a byte string
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # Close the MediaPipe Pose object
    pose.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def status():
    global detect_status
    return jsonify(status=detect_status)

if __name__ == '__main__':
    app.run(debug=True)

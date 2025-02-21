from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import math

app = Flask(__name__)

# Initialize maximum distance as a global variable
max_distance = float('-inf')

def generate_frames():
    global max_distance  # Access the global variable
    
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
            shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            distance = math.sqrt((shoulder.x - mouth_x)**2 + (shoulder.y - mouth_y)**2)
            
            # Update the global max_distance variable
            if distance > max_distance:
                max_distance = distance
            elif distance <= 0.8 * max_distance:
                cv2.putText(annotated_image, 'Stop', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

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
    # Pass the max_distance variable to the template
    return render_template('index.html', max_distance=max_distance)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

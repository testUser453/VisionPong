import cv2
import mediapipe as mp
import socket
import json

# Settings
HOST = "localhost"
PORT = 5052

# Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cap = cv2.VideoCapture(0)

pose_model = mp.solutions.pose

with pose_model.Pose(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
) as pose:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        # data = results.pose_world_landmarks
        data = results.pose_landmarks

        if data:
            
            # Adding movement based on the Nose
            # Landmark 0 is the nose and we are tracking the nose
            nose = data.landmark[0]

            '''
            Convert to centered coordinates: Unity reads center of the
            screen as (0,0) but mediapipe reads top left of computer 
            screen as (0,0).
            
            In Unity and Mediapipe:
            Mediapipe z: depth from camera, Unity z: forward backward
            Mediapipe y: top/bottom, Unity y: top/bottom
            Mediapipe x: left/right, Unity x: left/right
            '''
            xNose = nose.x - 0.5
            yNose = 0.5 - nose.y
            zNose = -nose.z

            # Adding movement based on the Right Wrist
            # Landmark 16 is the right wrist land mark
            wrist_r = data.landmark[16]
            
            xWrist_r = wrist_r.x - 0.5
            yWrist_r = 0.5 - wrist_r.y
            zWrist_r = -wrist_r.z

            # Adding movement based on the Left Wrist
            # Landmark 15 is the left wrist land mark
            wrist_l = data.landmark[15]

            xWrist_l = wrist_l.x - 0.5
            yWrist_l = 0.5 - wrist_l.y
            zWrist_l = -wrist_l.z

            # Adding movement based on Right Knee
            # Landmark 26 is the rigth knee
            knee_r = data.landmark[26]
            
            xKnee_r = knee_r.x - 0.5
            yKnee_r = 0.5 - knee_r.y
            zKnee_r = -knee_r.z

            # Adding movement based on Left Knee
            # Landmark 25 is the left knee
            knee_l = data.landmark[25]
            
            xKnee_l = knee_l.x - 0.5
            yKnee_l = 0.5 - knee_l.y
            zKnee_l = -knee_l.z

            # Adding movement based on Right Elbow
            # Landmark 14 is the right elbow
            elbow_r = data.landmark[14]
            
            xElbow_r = elbow_r.x - 0.5
            yElbow_r = 0.5 - elbow_r.y
            zElbow_r = -elbow_r.z

            # Adding movement based on Left Elbow
            # Landmark 13 is the left elbow
            elbow_l = data.landmark[13]
            
            xElbow_l = elbow_l.x - 0.5
            yElbow_l = 0.5 - elbow_l.y
            zElbow_l = -elbow_l.z

            # Adding movement based on Right Ankle
            # Landmark 28 is the right ankle
            ankle_r = data.landmark[28]
            
            xAnkle_r = ankle_r.x - 0.5
            yAnkle_r = 0.5 - ankle_r.y
            zAnkle_r = -ankle_r.z

            # Adding movement based on Left Ankle
            # Landmark 27 is the left ankle
            ankle_l = data.landmark[27]
            
            xAnkle_l = ankle_l.x - 0.5
            yAnkle_l = 0.5 - ankle_l.y
            zAnkle_l = -ankle_l.z

            # Adding movement based on the Right Shoulder
            # Landmark 12 is the right shoulder land mark
            shoulder_r = data.landmark[12]

            xShoulder_r = shoulder_r.x - 0.5
            yShoulder_r = 0.5 - shoulder_r.y
            zShoulder_r = -shoulder_r.z

            # Adding movement based on the Left Shoulder
            # Landmark 11 is the left shoulder land mark
            shoulder_l = data.landmark[11]

            xShoulder_l = shoulder_l.x - 0.5
            yShoulder_l = 0.5 - shoulder_l.y
            zShoulder_l = -shoulder_l.z

            # Adding movement based on the Right Hip
            # Landmark 24 is the right hip land mark
            hip_r = data.landmark[24]

            xHip_r = hip_r.x - 0.5
            yHip_r = 0.5 - hip_r.y
            zHip_r = -hip_r.z

            # Adding movement based on the Left Hip
            # Landmark 23 is the left hip land mark
            hip_l = data.landmark[23]

            xHip_l = hip_l.x - 0.5
            yHip_l = 0.5 - hip_l.y
            zHip_l = -hip_l.z


            data = {
                "nose": {
                    "x": xNose,
                    "y": yNose,
                    "z": -zNose
                },

                "right_wrist": {
                    "x": xWrist_r,
                    "y": yWrist_r,
                    "z": -zWrist_r
                },

                "left_wrist": {
                    "x": xWrist_l,
                    "y": yWrist_l,
                    "z": -zWrist_l
                },

                "right_knee": {
                    "x": xKnee_r,
                    "y": yKnee_r,
                    "z": -zKnee_r
                },

                "left_knee": {
                    "x": xKnee_l,
                    "y": yKnee_l,
                    "z": -zKnee_l
                },

                "right_elbow": {
                    "x": xElbow_r,
                    "y": yElbow_r,
                    "z": -zElbow_r
                },

                "left_elbow": {
                    "x": xElbow_l,
                    "y": yElbow_l,
                    "z": -zElbow_l
                },

                "right_ankle": {
                    "x": xAnkle_r,
                    "y": yAnkle_r,
                    "z": -zAnkle_r
                },

                "left_ankle": {
                    "x": xAnkle_l,
                    "y": yAnkle_l,
                    "z": -zAnkle_l
                },

                "right_shoulder": {
                    "x": xShoulder_r,
                    "y": yShoulder_r,
                    "z": -zShoulder_r
                },

                "left_shoulder": {
                    "x": xShoulder_l,
                    "y": yShoulder_l,
                    "z": -zShoulder_l
                },

                "right_hip": {
                    "x": xHip_r,
                    "y": yHip_r,
                    "z": -zHip_r
                },

                "left_hip": {
                    "x": xHip_l,
                    "y": yHip_l,
                    "z": -zHip_l
                }

            }

            message = json.dumps(data)
            sock.sendto(message.encode("utf-8"), (HOST, PORT))

        cv2.imshow("Pose", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
sock.close()
cv2.destroyAllWindows()
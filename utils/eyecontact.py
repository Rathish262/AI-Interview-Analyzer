import cv2
import mediapipe as mp


def analyze_eye_contact(video_path):

    mp_face_mesh = mp.solutions.face_mesh

    face_mesh = mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        refine_landmarks=True
    )

    cap = cv2.VideoCapture(video_path)

    total_frames = 0
    face_detected_frames = 0

    while cap.isOpened():

        success, frame = cap.read()

        if not success:
            break

        total_frames += 1

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            face_detected_frames += 1

    cap.release()
    face_mesh.close()

    if total_frames == 0:
        return 0

    eye_contact_score = (
        face_detected_frames / total_frames
    ) * 100

    return round(
        eye_contact_score,
        2
    )
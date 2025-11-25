import cv2
import time
from src.detector import FaceDetector
from src.analyzer import EmotionAnalyzer
from src.utils import draw_results, save_snapshot

def main():
    # Initialize modules
    detector = FaceDetector('assets/haarcascade_frontalface_default.xml')
    analyzer = EmotionAnalyzer()
    cap = cv2.VideoCapture(0)

    last_save_time = time.time()
    save_interval = 60 

    while True:
        ret, frame = cap.read()
        if not ret: break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        
        faces = detector.detect_faces(gray)

        for (x, y, w, h) in faces:
            face_roi = rgb[y:y + h, x:x + w]
            emotion = analyzer.analyze_emotion(face_roi)

            if emotion:
                draw_results(frame, x, y, w, h, emotion)
                
                # Logic to save every 60 seconds
                if time.time() - last_save_time >= save_interval:
                    save_snapshot(frame, emotion)
                    last_save_time = time.time()

        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

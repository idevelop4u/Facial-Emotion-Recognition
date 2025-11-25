from deepface import DeepFace

class EmotionAnalyzer:
    def analyze_emotion(self, face_roi):
        try:
            # Enforce detection is False because we already cropped the face
            results = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            return results[0]['dominant_emotion']
        except Exception as e:
            return None

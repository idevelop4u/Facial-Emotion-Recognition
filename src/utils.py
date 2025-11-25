import cv2
import os
import time

def draw_results(frame, x, y, w, h, emotion):
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

def save_snapshot(frame, emotion, folder="captured_faces"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    timestamp = int(time.time())
    filename = f"{folder}/{emotion}_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Saved snapshot: {filename}")

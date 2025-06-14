import cv2
import time
import csv
import os
import numpy as np
from keras.models import load_model
from deepface import DeepFace
import subprocess

# Load emotion classification model
model = load_model("C:/Users/Student/Documents/Python/emotion_model.h5")

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Settings
use_hardware = False  # Set to False for software inference (DeepFace)
MAX_FRAMES = 100
CSV_PATH = "emotion_predictions.csv"
mode = "Hardware" if use_hardware else "Software"

# Webcam capture
cap = cv2.VideoCapture(0)
frame_count = 0

# Open CSV in append mode if it already exists, otherwise write headers
write_header = not os.path.exists(CSV_PATH)
with open(CSV_PATH, mode="a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    if write_header:
        writer.writerow(["Frame", "Timestamp", "Mode", "Emotion", "InferenceTime(sec)"])

    while frame_count < MAX_FRAMES:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (48, 48)).astype('float32') / 255.0
        reshaped = np.reshape(resized, (1, 48, 48, 1))

        start_time = time.time()
        label = "Unknown"

        if use_hardware:
            np.savetxt("input_image.txt", reshaped.flatten())
            try:
                result = subprocess.run(["./obj_dir/Vcnn_accelerator"], capture_output=True, text=True)
                label_index_str = result.stdout.strip()
                label_index = int(label_index_str)
                if 0 <= label_index < len(emotion_labels):
                    label = emotion_labels[label_index]
            except Exception as e:
                label = "Unknown"
        else:
            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                label = result[0]['dominant_emotion'].capitalize()
            except Exception as e:
                label = "Unknown"

        end_time = time.time()
        inference_time = end_time - start_time
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{mode}] Inference Time: {inference_time:.6f} sec | Emotion: {label}")
        writer.writerow([frame_count + 1, timestamp, mode, label, f"{inference_time:.6f}"])

        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_count += 1

cap.release()
cv2.destroyAllWindows()

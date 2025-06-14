import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import time

# Load your trained CNN model
model = load_model("emotion_model.h5")
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Start webcam
cap = cv2.VideoCapture(0)

expression_counter = 0
max_expressions = 50

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale and resize to 48x48 (FER input)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = cv2.resize(gray, (48, 48))
    face = face.reshape(1, 48, 48, 1) / 255.0  # Normalize

    # Time the inference
    start_time = time.time()
    prediction = model.predict(face, verbose=0)
    end_time = time.time()
    inference_time = end_time - start_time

    # Get emotion
    emotion_idx = np.argmax(prediction)
    emotion = emotion_labels[emotion_idx]
    print(f"Expression: {emotion} | Inference Time: {inference_time:.4f} sec")

    expression_counter += 1

    # Show feed
    cv2.imshow('Emotion Detection', frame)

    if expression_counter >= max_expressions or cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

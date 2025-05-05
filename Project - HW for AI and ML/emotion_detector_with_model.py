import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load the trained model
model = load_model("emotion_model.h5")

emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Initialize webcam
cap = cv2.VideoCapture(0)

expression_counter = 0
max_expressions = 50

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        roi = img_to_array(roi_gray)
        roi = np.expand_dims(roi, axis=0)
        roi = roi / 255.0

        preds = model.predict(roi)[0]
        label = emotion_labels[np.argmax(preds)]
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)

        expression_counter += 1

    cv2.imshow('Emotion Detection', frame)

    if expression_counter >= max_expressions:
        print(f"Processed {max_expressions} expressions. Exiting...")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
from deepface import DeepFace

# Initialize webcam
cap = cv2.VideoCapture(0)

# Counter to track how many expressions are processed
expression_counter = 0
max_expressions = 50

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        print("Failed to grab frame")
        break

    # Perform emotion detection using DeepFace
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        print(f"Expression: {result[0]['dominant_emotion']}")
        expression_counter += 1
    except Exception as e:
        print("Error in analysis:", e)

    # Show the webcam feed
    cv2.imshow('Emotion Detection', frame)

    # Break the loop after processing 50 expressions
    if expression_counter >= max_expressions:
        print(f"Processed {max_expressions} expressions. Exiting...")
        break

    # Check if the user pressed the 'q' key to exit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()

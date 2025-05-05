This project implements a real-time emotion detection system using a custom-trained Convolutional Neural Network (CNN) model on the FER-2013 dataset. The pipeline includes:

Training a CNN model to classify facial expressions

Running real-time emotion detection using a webcam

Preparing the trained model for future hardware acceleration using FPGA

**emotiondetection:**
This was the initial prototype using the DeepFace library for real-time emotion detection. It served as a baseline for comparing performance with the custom-trained CNN model.

**fer2013:**
The preprocessed dataset extracted from the FER-2013 ZIP file. It contains train/ and test/ folders with 48x48 grayscale images categorized by emotion labels.

**train_emotion_cnn:**
Contains the Python script used to train the CNN model on the FER-2013 dataset. This includes preprocessing, model architecture, training, and saving the trained .h5 model.

**emotion_model.h5:**
The final trained Keras CNN model capable of classifying 7 facial emotions. This model is used by emotion_detector_with_model for inference.

**emotion_detector_with_model:**
Contains the real-time emotion detection script that loads the trained model (emotion_model.h5) and processes webcam input to predict emotions in real time.

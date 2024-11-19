import json
import cv2
import os
import numpy as np
from config.config import settings

# Initialize face detector and recognizer
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Function to prepare data for training
def prepare_training_data():
    faces = []
    labels = []
    label_map = {}  # To map employee ID to their name

    # Loop through images in the folder
    for filename in os.listdir(settings.UPLOAD_FOLDER):
        image_path = os.path.join(settings.UPLOAD_FOLDER, filename)
        
        # Check if it's an image file (just to be safe)
        if filename.endswith(".jpg"):
            # Extract employee ID and name from the filename (assumes format "employee_id_name.jpg")
            parts = filename.split('_')
            if len(parts) != 2:
                print(f"Skipping invalid filename format: {filename}")
                continue
            employee_id = parts[0]  # This is the employee ID (e.g., '1')
            employee_name = parts[1].split('.')[0]  # This is the employee name (e.g., 'john')
            
            # Load the image
            img = cv2.imread(image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces in the image
            detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            
            for (x, y, w, h) in detected_faces:
                face = gray[y:y+h, x:x+w]  # Crop the face
                faces.append(face)
                
                # Use the employee ID as the label
                if employee_id not in label_map:
                    label_map[employee_id] = employee_name  # Map employee ID to employee name
                labels.append(employee_id)
    
    return faces, labels, label_map

# Step 2: Train the recognizer
def train_recognizer():
    faces, labels, label_map = prepare_training_data()
    
    # Train the recognizer
    recognizer.train(faces, np.array(labels))
    
    # Save the trained model
    recognizer.save('employee_face_recognizer.yml')  # Save to file
    
    # Save the label map for later use in recognition
    with open('label_map.json', 'w') as f:
        json.dump(label_map, f)
    
    print(f"Training completed. Labels: {label_map}")

# Train the model
train_recognizer()


# def recognize_employee(image_path: str):
#     # Load the trained recognizer and label map
#     recognizer.read('employee_face_recognizer.yml')
#     with open('label_map.json', 'r') as f:
#         label_map = json.load(f)
    
#     # Load the image
#     img = cv2.imread(image_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the image
#     detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#     for (x, y, w, h) in detected_faces:
#         face = gray[y:y+h, x:x+w]  # Crop the face
        
#         # Recognize the face
#         label, confidence = recognizer.predict(face)
        
#         # Get the employee name from the label (which is the employee ID)
#         employee_name = label_map.get(str(label), "Unknown")
        
#         print(f"Employee recognized: {employee_name} with confidence: {confidence}")

# # Test the face recognition with a new image
# recognize_employee("path_to_test_image.jpg")

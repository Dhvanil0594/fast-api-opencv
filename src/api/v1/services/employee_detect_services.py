from logger import logger

def check_employee_id(result):
    logger.info(f"check_employee_id: {result}")
    if len(result) > 0:
        result = result[0]["identity"]
        image_name = result.split("/")[-1]
        employee_id = image_name.split("_")[0]
    else:
        employee_id = None

    return employee_id

# ---------------------------------------------------------------------------------------------------------

# # Path for saving models and training data
# MODEL_PATH = 'src/api/v1/constants/face_trained.yml'
# FEATURES_PATH = 'src/api/v1/constants/features.npy'
# LABELS_PATH = 'src/api/v1/constants/labels.npy'

# # People list (static for now, could be dynamic later)
# people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# haar_cascade = cv.CascadeClassifier('src/api/v1/constants/haarcascade_frontalface_default.xml')

# # LBPH face recognizer
# face_recognizer = cv.face.LBPHFaceRecognizer_create()

# # Load existing model if it exists
# if os.path.exists(MODEL_PATH):
#     face_recognizer.read(MODEL_PATH)
#     print('Model loaded successfully.')

# # Helper functions

# def create_train(features, labels):
#     """Function to train the face recognizer."""
#     logger.info("9")
#     face_recognizer.train(features, labels)
#     logger.info("10")
#     face_recognizer.save(MODEL_PATH)
#     logger.info("11")

# def update_features_and_labels(person_name, img_array, features, labels):
#     """Detect faces, extract features, and update training data."""
#     logger.info("12")
#     gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
#     logger.info("13")
#     faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
#     logger.info("14")

#     for (x, y, w, h) in faces_rect:
#         logger.info("15")
#         faces_roi = gray[y:y + h, x:x + w]
#         logger.info(f"16, {faces_roi}")
        
#         # Append the flattened face ROI to features
#         features.append(faces_roi.flatten())
#         logger.info("17")
        
#         # Ensure the person is in the list and get their label
#         if person_name not in people:
#             people.append(person_name)
#         labels.append(people.index(person_name))  # Add the index as the label
#         logger.info("18")
        
#     return features, labels

# async def train_face(name, file):
#     """Train the model with new face data."""
#     try:
#         logger.info(f"train_face: {name}")
        
#         # Load the uploaded image
#         img = np.array(cv.imdecode(np.frombuffer(await file.read(), np.uint8), cv.IMREAD_COLOR))
#         logger.info("1")
#         if img is None:
#             return None
#         logger.info("2")
        
#         # Initialize or load existing features and labels
#         features, labels = [], []
#         if os.path.exists(FEATURES_PATH) and os.path.exists(LABELS_PATH):
#             features = np.load(FEATURES_PATH, allow_pickle=True).tolist()  # Load saved features
#             labels = np.load(LABELS_PATH).tolist()  # Load saved labels
#         else:
#             features = []
#             labels = []

#         logger.info("3")
        
#         # Update features and labels with new data
#         features, labels = update_features_and_labels(name, img, features, labels)
#         logger.info(f"5, {features}, {labels}")
        
#         # Convert lists to NumPy arrays for saving and training
#         features = np.array(features, dtype='object')  # 2D array of face ROIs
#         labels = np.array(labels)  # 1D array of integer labels
        
#         # Save the updated features and labels
#         np.save(FEATURES_PATH, features)
#         logger.info("6")
#         np.save(LABELS_PATH, labels)
#         logger.info("7")
        
#         # Re-train the model with the new data
#         create_train(features, labels)
#         logger.info("8")
#         return True

#     except Exception as e:
#         logger.error(f"Error: {e}")
#         return False

# =================================================================================================================================

# async def recognize_face(file):
#     """Recognize the face from the uploaded image."""
#     try:
#         # Load the uploaded image
#         img = np.array(cv.imdecode(np.frombuffer(await file.read(), np.uint8), cv.IMREAD_COLOR))
        
#         if img is None:
#             return JSONResponse(content={"message": "Invalid image"}, status_code=400)

#         gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#         faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

#         if len(faces_rect) == 0:
#             return JSONResponse(content={"message": "No faces detected"}, status_code=400)

#         results = []

#         for (x, y, w, h) in faces_rect:
#             faces_roi = gray[y:y + h, x:x + w]
#             label, confidence = face_recognizer.predict(faces_roi)

#             # Only consider matches with confidence < 100 (the lower the confidence, the better the match)
#             if confidence < 100:
#                 person_name = people[label]
#                 results.append({"name": person_name, "confidence": confidence})
#                 cv.putText(img, person_name, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#                 cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             else:
#                 results.append({"name": "Unknown", "confidence": confidence})

#         # Save or display the processed image
#         cv.imwrite("attendance_output.jpg", img)

#         return JSONResponse(content={"message": "Attendance recognized", "results": results}, status_code=200)

#     except Exception as e:
#         return JSONResponse(content={"message": f"Error: {str(e)}"}, status_code=500)

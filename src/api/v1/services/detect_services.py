from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet import preprocess_input

# List of class labels
labels = ['Apple Braeburn', 'Apple Golden 1', 'Apple Golden 2', 'Apple Golden 3', 'Apple Granny Smith', 'Apple Red 1', 'Apple Red 2', 'Apple Red 3', 'Apple Red Delicious', 'Apple Red Yellow', 'Apricot', 'Avocado', 'Avocado ripe', 'Banana', 'Banana Red', 'Cactus fruit', 'Carambula', 'Cherry', 'Clementine', 'Cocos', 'Dates', 'Granadilla', 'Grape Pink', 'Grape White', 'Grape White 2', 'Grapefruit Pink', 'Grapefruit White', 'Guava', 'Huckleberry', 'Kaki', 'Kiwi', 'Kumquats', 'Lemon', 'Lemon Meyer', 'Limes', 'Litchi', 'Mandarine', 'Mango', 'Maracuja', 'Nectarine', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Peach Flat', 'Pear', 'Pear Abate', 'Pear Monster', 'Pear Williams', 'Pepino', 'Pineapple', 'Pitahaya Red', 'Plum', 'Pomegranate', 'Quince', 'Raspberry', 'Salak', 'Strawberry', 'Tamarillo', 'Tangelo']

# Image preprocessing and prediction function
def predict_image(img: Image.Image):
    # Load the trained model
    model = load_model('src/api/v1/constants/fruits_model.keras')
    # Resize and preprocess the image
    img = img.resize((100, 100))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Apply the ResNet preprocessing
    
    # Perform prediction
    prediction = model.predict(img_array)
    
    # Get the predicted class index and the corresponding label
    predicted_class_index = np.argmax(prediction)
    predicted_class_label = labels[predicted_class_index]
    
    return predicted_class_label
import tensorflow as tf
import numpy as np
import io
import urllib.request
from PIL import Image

# Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2()

# Function to preprocess the input image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = image.convert('RGB')  # Convert the image to RGB color mode
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return image

# Function to make predictions on the input image
def predict_image(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]
    results = []
    for _, label, probability in decoded_predictions:
        results.append((label, probability))
    return results

# Function to load an image from a URL
def load_image_from_url(url):
    image_data = urllib.request.urlopen(url).read()
    image = Image.open(io.BytesIO(image_data))
    return image

# Get the URL of an image from the user
image_url = input("Enter the URL of an image: ")

# Load and predict the image
image = load_image_from_url(image_url)
predictions = predict_image(image)

# Display the predictions
print("Predictions:")
for label, probability in predictions:
    print(f"{label}: {probability}")

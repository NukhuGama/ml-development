import numpy as np
from PIL import Image
import tensorflow as tf
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

# Load the Keras model (.h5)
model = tf.keras.models.load_model('ml_models/my_model.h5')

# Load labels
with open('ml_models/labels.txt', 'r') as f:
    labels = [line.strip() for line in f.readlines()]

def preprocess_image(img):
    img = img.resize((120, 120))  # Adjust based on model input
    img = np.array(img).astype(np.float32)
    img = np.expand_dims(img, axis=0)
    return img

def predict(img_tensor):
    predictions = model.predict(img_tensor)
    class_id = int(np.argmax(predictions))
    confidence = float(predictions[0][class_id])
    return labels[class_id], confidence

def predict_image(request):
    context = {}
    if request.method == 'POST' and 'image' in request.FILES:
        img_file = request.FILES['image']

        # Save uploaded image to media folder
        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)
        file_url = fs.url(filename)  # URL for <img src=...>

        # Load and preprocess image
        img_path = os.path.join(settings.MEDIA_ROOT, filename)
        img = Image.open(img_path).convert('RGB')
        input_tensor = preprocess_image(img)

        # Predict
        class_name, confidence = predict(input_tensor)

        # Pass prediction + image path to template
        context = {
            'image_url': file_url,
            'class_name': class_name,
            'confidence': round(confidence * 100, 2),
        }

    return render(request, 'index.html', context)

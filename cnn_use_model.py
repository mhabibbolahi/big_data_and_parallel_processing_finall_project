<<<<<<< HEAD
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import time
import os
# open('static/b'Abyssinian_1.jpg'.jpg')

def preprocess_image(img_path):

    time.sleep(1)
    img = image.load_img(img_path, target_size=(32, 32))  # CIFAR-10 تصاویر 32x32 هستند
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # نرمال‌سازی تصویر
    return img_array


def main(img_path):
    model = load_model('final_model_cnn.h5')

    predictions = model.predict(preprocess_image(img_path))
    predicted_label = np.argmax(predictions, axis=1)
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    return class_names[predicted_label[0]], str(model.summary())
=======
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import time
import os
# open('static/b'Abyssinian_1.jpg'.jpg')

def preprocess_image(img_path):

    time.sleep(1)
    img = image.load_img(img_path, target_size=(32, 32))  # CIFAR-10 تصاویر 32x32 هستند
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # نرمال‌سازی تصویر
    return img_array


def main(img_path):
    model = load_model('final_model_cnn.h5')

    predictions = model.predict(preprocess_image(img_path))
    predicted_label = np.argmax(predictions, axis=1)
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    return class_names[predicted_label[0]], str(model.summary())
>>>>>>> 2b99315f86eab7221a5c36628d0a0c9c4de96459

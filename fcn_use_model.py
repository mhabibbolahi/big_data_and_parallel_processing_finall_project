<<<<<<< HEAD
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

model = load_model('final_model_fcn.h5')

label_colors = np.random.randint(0, 255, (40, 3), dtype=np.uint8)

def preprocess_input_image(image_path, target_size=(224, 224)):
    image = load_img(image_path, target_size=target_size)
    image_array = img_to_array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

def main(input_image_path):
    input_image = preprocess_input_image(input_image_path)
    mask = model.predict(input_image)

    mask = np.squeeze(mask, axis=0)
    predicted_mask = np.argmax(mask, axis=-1)
    output_mask = np.zeros((*predicted_mask.shape, 3), dtype=np.uint8)
    for label in range(len(label_colors)):
        output_mask[predicted_mask == label] = label_colors[label]
    mask_image = Image.fromarray(output_mask)

    mask_image.save(input_image_path)

    return input_image_path


=======
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

model = load_model('final_model_fcn.h5')

label_colors = np.random.randint(0, 255, (40, 3), dtype=np.uint8)

def preprocess_input_image(image_path, target_size=(224, 224)):
    image = load_img(image_path, target_size=target_size)
    image_array = img_to_array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

def main(input_image_path):
    input_image = preprocess_input_image(input_image_path)
    mask = model.predict(input_image)

    mask = np.squeeze(mask, axis=0)
    predicted_mask = np.argmax(mask, axis=-1)
    output_mask = np.zeros((*predicted_mask.shape, 3), dtype=np.uint8)
    for label in range(len(label_colors)):
        output_mask[predicted_mask == label] = label_colors[label]
    mask_image = Image.fromarray(output_mask)

    mask_image.save(input_image_path)

    return input_image_path


>>>>>>> 2b99315f86eab7221a5c36628d0a0c9c4de96459

<<<<<<< HEAD
import keras
import os
import random
import numpy as np
from matplotlib.image import imread
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dropout, concatenate, Conv2DTranspose
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator


INPUT_HEIGHT = 224
INPUT_WIDTH = 224
dir_mask = os.listdir('oxford_iiit_pet/mask2')
dir_pick = os.listdir('oxford_iiit_pet/pick2')
pick = np.empty((3680, 224, 224,3),dtype='float16')
mask = np.empty((3680, 224, 224),dtype='float16')
i = 0
s = random.sample(range(pick.shape[0]), pick.shape[0])
for x in dir_pick:
    pick[i, :, :,:] = imread('oxford_iiit_pet/pick2/' + x).shape
    i += 1

x_train = pick[s[int(len(s) * 0.4):], :,:,:]
x_val =   pick[s[int(len(s)*0.2):int(len(s)*0.4)]]
x_test =   pick[s[:int(len(s)*0.2)]]
pick = None
i = 0
for x in dir_mask:
    mask[i,:,:] = imread('oxford_iiit_pet/mask2/' + x)
    i +=1

y_train = mask[s[int(len(s) * 0.4):], :,:]
y_val = mask[s[int(len(s) * 0.2):int(len(s) * 0.4)], :,:]
y_test = mask[s[:int(len(s) * 0.2)], :,:]
mask = None


NUM_CLASSES = 3

# تغییر در لایه خروجی و تابع فعال‌سازی
def unet_model(input_shape=(224, 224, 3), num_classes=NUM_CLASSES):
    inputs = Input(input_shape)

    # Encoder
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(inputs)
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = Conv2D(128, 3, activation='relu', padding='same')(pool1)
    conv2 = Conv2D(128, 3, activation='relu', padding='same')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = Conv2D(256, 3, activation='relu', padding='same')(pool2)
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = Conv2D(512, 3, activation='relu', padding='same')(pool3)
    conv4 = Conv2D(512, 3, activation='relu', padding='same')(conv4)

    # Decoder
    up5 = Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same')(conv4)
    up5 = concatenate([up5, conv3], axis=3)
    conv5 = Conv2D(256, 3, activation='relu', padding='same')(up5)
    conv5 = Conv2D(256, 3, activation='relu', padding='same')(conv5)

    up6 = Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(conv5)
    up6 = concatenate([up6, conv2], axis=3)
    conv6 = Conv2D(128, 3, activation='relu', padding='same')(up6)
    conv6 = Conv2D(128, 3, activation='relu', padding='same')(conv6)

    up7 = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv6)
    up7 = concatenate([up7, conv1], axis=3)
    conv7 = Conv2D(64, 3, activation='relu', padding='same')(up7)
    conv7 = Conv2D(64, 3, activation='relu', padding='same')(conv7)

    # Output layer
    outputs = Conv2D(num_classes, 1, activation='softmax')(conv7)  # Output layer with num_classes filters

    model = Model(inputs=inputs, outputs=outputs)
    return model

# تبدیل برچسب‌ها به فرمت one-hot
y_train_one_hot = to_categorical(y_train, num_classes=NUM_CLASSES)
y_val_one_hot = to_categorical(y_val, num_classes=NUM_CLASSES)
y_test_one_hot = to_categorical(y_test, num_classes=NUM_CLASSES)

# ساخت مدل
model = unet_model()

# کامپایل مدل
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# چاپ خلاصه مدل
model.summary()

# تعریف callbacks برای کاهش نرخ یادگیری و توقف زودهنگام
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.0001)
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

# آموزش مدل
history = model.fit(x_train, y_train_one_hot, batch_size=32, epochs=6, validation_data=(x_val, y_val_one_hot), callbacks=[reduce_lr, early_stop])

# ارزیابی مدل
loss, accuracy = model.evaluate(x_test, y_test_one_hot)
print(f'Test loss: {loss}, Test accuracy: {accuracy}')
=======
import keras
import os
import random
import numpy as np
from matplotlib.image import imread
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dropout, concatenate, Conv2DTranspose
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator


INPUT_HEIGHT = 224
INPUT_WIDTH = 224
dir_mask = os.listdir('oxford_iiit_pet/mask2')
dir_pick = os.listdir('oxford_iiit_pet/pick2')
pick = np.empty((3680, 224, 224,3),dtype='float16')
mask = np.empty((3680, 224, 224),dtype='float16')
i = 0
s = random.sample(range(pick.shape[0]), pick.shape[0])
for x in dir_pick:
    pick[i, :, :,:] = imread('oxford_iiit_pet/pick2/' + x).shape
    i += 1

x_train = pick[s[int(len(s) * 0.4):], :,:,:]
x_val =   pick[s[int(len(s)*0.2):int(len(s)*0.4)]]
x_test =   pick[s[:int(len(s)*0.2)]]
pick = None
i = 0
for x in dir_mask:
    mask[i,:,:] = imread('oxford_iiit_pet/mask2/' + x)
    i +=1

y_train = mask[s[int(len(s) * 0.4):], :,:]
y_val = mask[s[int(len(s) * 0.2):int(len(s) * 0.4)], :,:]
y_test = mask[s[:int(len(s) * 0.2)], :,:]
mask = None


NUM_CLASSES = 3

# تغییر در لایه خروجی و تابع فعال‌سازی
def unet_model(input_shape=(224, 224, 3), num_classes=NUM_CLASSES):
    inputs = Input(input_shape)

    # Encoder
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(inputs)
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = Conv2D(128, 3, activation='relu', padding='same')(pool1)
    conv2 = Conv2D(128, 3, activation='relu', padding='same')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = Conv2D(256, 3, activation='relu', padding='same')(pool2)
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = Conv2D(512, 3, activation='relu', padding='same')(pool3)
    conv4 = Conv2D(512, 3, activation='relu', padding='same')(conv4)

    # Decoder
    up5 = Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same')(conv4)
    up5 = concatenate([up5, conv3], axis=3)
    conv5 = Conv2D(256, 3, activation='relu', padding='same')(up5)
    conv5 = Conv2D(256, 3, activation='relu', padding='same')(conv5)

    up6 = Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(conv5)
    up6 = concatenate([up6, conv2], axis=3)
    conv6 = Conv2D(128, 3, activation='relu', padding='same')(up6)
    conv6 = Conv2D(128, 3, activation='relu', padding='same')(conv6)

    up7 = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv6)
    up7 = concatenate([up7, conv1], axis=3)
    conv7 = Conv2D(64, 3, activation='relu', padding='same')(up7)
    conv7 = Conv2D(64, 3, activation='relu', padding='same')(conv7)

    # Output layer
    outputs = Conv2D(num_classes, 1, activation='softmax')(conv7)  # Output layer with num_classes filters

    model = Model(inputs=inputs, outputs=outputs)
    return model

# تبدیل برچسب‌ها به فرمت one-hot
y_train_one_hot = to_categorical(y_train, num_classes=NUM_CLASSES)
y_val_one_hot = to_categorical(y_val, num_classes=NUM_CLASSES)
y_test_one_hot = to_categorical(y_test, num_classes=NUM_CLASSES)

# ساخت مدل
model = unet_model()

# کامپایل مدل
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# چاپ خلاصه مدل
model.summary()

# تعریف callbacks برای کاهش نرخ یادگیری و توقف زودهنگام
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.0001)
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

# آموزش مدل
history = model.fit(x_train, y_train_one_hot, batch_size=32, epochs=6, validation_data=(x_val, y_val_one_hot), callbacks=[reduce_lr, early_stop])

# ارزیابی مدل
loss, accuracy = model.evaluate(x_test, y_test_one_hot)
print(f'Test loss: {loss}, Test accuracy: {accuracy}')
>>>>>>> 2b99315f86eab7221a5c36628d0a0c9c4de96459
model.save('final_model_fcn.h5')
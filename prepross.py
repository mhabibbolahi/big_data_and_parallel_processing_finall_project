import numpy as np
from PIL import Image
from matplotlib.image import imread
# import keras
import os
dir_list = os.listdir('oxford_iiit_pet/mask')
dir_list2 = os.listdir('oxford_iiit_pet/pick')
pick = []
mask = []
INPUT_HEIGHT = 224
INPUT_WIDTH = 224
for x in dir_list2:
    y = Image.open('oxford_iiit_pet/pick/'+x).crop((0, 0, INPUT_WIDTH, INPUT_WIDTH))
    y.save('oxford_iiit_pet/pick2/'+x)
print('55')
for x in dir_list:
    y = Image.open('oxford_iiit_pet/mask/' + x).crop((0, 0, INPUT_WIDTH, INPUT_WIDTH))
    y.save('oxford_iiit_pet/mask2/' + x)
print('55')

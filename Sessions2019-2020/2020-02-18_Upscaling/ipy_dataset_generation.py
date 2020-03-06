# Code to be executed with ipython

import cv2
import h5py
import numpy as np

h5_path = "train_tiles2.h5"
images_path = !ls tiles | grep .jpg | head -n15000
hr_images = []
lr_images = []
for image in images_path:
    hr_img = cv2.imread('tiles/' + image)
    hr_images.append(hr_img)
    lr_img = cv2.resize(hr_img, (64, 64))
    lr_images.append(lr_img)
data = np.array(lr_images)
label = np.array(hr_images)

std = np.std(label, axis=(1,2,3))
std_sort_index = np.argsort(std)

data = data[std_sort_index[5_000:]]
label = label[std_sort_index[5_000:]]

with h5py.File(h5_path, 'w') as h5:
    h5.create_dataset('highres', data=label)
    h5.create_dataset('lowres', data=data)

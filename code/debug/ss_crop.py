# debug file : to check the cropping 

import os
import sys
import inspect
import cv2
import matplotlib.pyplot as plt

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import utils

from utils.ss_to_image import final_crop

file_name = '../../resource/screenshots/'+ sys.argv[1] + '.jpeg'
print('file_name', file_name)
print(os.getcwd())
print('listdir',os.listdir('../../resource/screenshots/'))

if sys.argv[1] + '.jpeg' in os.listdir('../../resource/screenshots/'):

	cropped_image = final_crop(file_name)
else:
	file_name = '../../resource/screenshots/'+ sys.argv[1].split('_')[0] + '/' + sys.argv[1] + '.jpeg'
	cropped_image = final_crop(file_name)

plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.show()



# debug file : to check the cropping 

import os
import sys
import inspect
import cv2
import matplotlib.pyplot as plt

currentdir = os.getcwd()
#print('current dir', currentdir)
#print('os wala',os.getcwd())
parentdir = os.path.dirname(currentdir)
#print('parent',parentdir)
sys.path.insert(0,parentdir) 

import utils

from utils.ss_to_image import final_crop

def get_cropped_image(input):
	file_name = '../../resource/screenshots/'+ str(input) + '.jpeg'
	#print('file_name', file_name)
	#print(os.getcwd())
	#print('listdir',os.listdir('../../resource/screenshots/'))

	if str(input) + '.jpeg' in os.listdir('../../resource/screenshots/'):

		cropped_image = final_crop(file_name)
	else:
		file_name = '../../resource/screenshots/'+ str(input).split('_')[0] + '/' + str(input) + '.jpeg'
		cropped_image = final_crop(file_name)

	return cropped_image

if __name__ == '__main__':
	
	cropped_image = get_cropped_image(sys.argv[1])
	plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
	plt.show()



# Blurs the upper part of the screenshots

import os
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

kernel = np.ones((5,5),np.float32)/25
k = 20

name = sys.argv[1] + '.jpeg'
file_path = '../../resource/screenshots/' + sys.argv[1] + '.jpeg'

if name in os.listdir('../../resource/screenshots/'):
	
	img = cv2.imread(file_path)

	n_row = (img.shape[0]//2)

	for i in range(k):
	    img[:n_row, :] = cv2.filter2D(img[:n_row, :],-1,kernel)
	
	#plt.figure(figsize=(12,10))
	#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
	#plt.show()
	directory = '../../resource/screenshots'
	os.chdir(directory) 

	filename = sys.argv[1] + '.jpeg'  
	cv2.imwrite(filename, img) 

else:
	file_name = '../../resource/screenshots/' + str(sys.argv[1])
	
	for i in os.listdir(file_name):

	    file_path = os.path.join(file_name, i)
	    img = cv2.imread(file_path)

	    n_row = (img.shape[0]//2)

	    for j in range(k):
            	img[:n_row, :] = cv2.filter2D(img[:n_row, :],-1,kernel)

	    #plt.figure(figsize=(12,10))
	    #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
	    #plt.show()	

	    cwd = os.getcwd() 

	    directory = '../../resource/screenshots/' + str(sys.argv[1])
	    os.chdir(directory) 

	    filename = str(i).split('.')[0] + '.jpeg'  
	    cv2.imwrite(filename, img) 
	    
	    os.chdir(cwd) 

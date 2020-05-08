# transforms the screenshot to process-able image

import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# The objective is to find the last peak in the range [lower, upper]
  
def recur_max(l, lower, upper):
    
    def in_range(m):
        output = True
        if not (m<=upper and m>=lower):
            output = False
        return output
    
    max_1, loc_1 = np.max(l), np.argmax(l)
    if in_range(max_1):
        
         if in_range(np.max(l[loc_1+1:])):
                return recur_max(l[loc_1+1:], lower, upper)
         else:
                return max_1
    else:
        
        return recur_max(l[loc_1+1:], lower, upper)
        

def crop_upper(file_path):
    
    # discard half
    def halved(file_path):

        img = cv2.imread(file_path)
        n_row = (img.shape[0]//2)
        img = img[n_row:, :]

        return img
    
    half_img = halved(file_path)
    pixel_array = half_img[:,:,0][:,0]
    
    loc = np.max(np.where(pixel_array == recur_max(pixel_array, lower = 145, upper = 155)))
    
    cropped_img = half_img[loc:,:]
    
    return cropped_img

def crop(file_path):
    
    up_cropped = crop_upper(file_path)
    
    pixel_array_0 = up_cropped[:,:,0][up_cropped.shape[0]//2:,1]  #51
    pixel_array_1 = up_cropped[:,:,1][up_cropped.shape[0]//2:,1]  #44
    pixel_array_2 = up_cropped[:,:,2][up_cropped.shape[0]//2:,1]  #35
    
    loc_0 = np.min(np.where(pixel_array_0==51))
    loc_1 = np.min(np.where(pixel_array_1==44))
    loc_2 = np.min(np.where(pixel_array_2==35))
    
    #print("0", np.min(np.where(pixel_array_0==51)))
    #print("1", np.min(np.where(pixel_array_1==44)))
    #print("2", np.min(np.where(pixel_array_2==35)))
    
    loc = max(loc_0, loc_1, loc_2) # IDK why I did this
    
    cropped_img = up_cropped[:loc+up_cropped.shape[0]//2, :]
    
    return cropped_img

def final_crop(file_path):

    main_img = crop(file_path)
    
    kernel = np.ones((5,5),np.float32)/25

    k = 20
    
    img = main_img
    for i in range(k):
        img = cv2.filter2D(img,-1,kernel)
        
    pixel_array = img[:,:,2][:,200]
    peaks, val = find_peaks(pixel_array, height=0)

    num_emojis = len(peaks)
    
    if num_emojis > 4:
        loc = (peaks[-2]+peaks[-1])//2
        output = main_img[:loc, :]
    elif num_emojis < 4:
        loc = 2*peaks[-1]-(peaks[-2]+peaks[-1])//2
        output = main_img[:loc, :]
    else:
        output = main_img
        
    
    return output



# takes the process-able image as input outputs the list of emojis as a list of np arrays

import cv2
import statistics
import numpy as np
from scipy.signal import find_peaks

def image_2_emoji(image):
    
    def to_half(image):
        
        n_col = image.shape[1]//2

        img_left = image[:, :n_col]
        img_right = image[:, n_col:]

        return (img_left, img_right)

    def extract_from_half(image):
        
        emoji_list = []
        for i in range(4):
            for j in range(4):
                temp = image[i*70:(i+1)*70,j*70:(j+1)*70]
                emoji_list.append(temp)
        return emoji_list
    
    img = image
    
    dim = (560,280)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
    
    halfed = to_half(resized)
    
    output = extract_from_half(halfed[0])
    output += extract_from_half(halfed[1])
    
    return output


def image_2_emoji_2(image):
    img_1 = image.copy()
    
    kernel = np.ones((5,5),np.float32)/25
    k = 20
    for i in range(k):
        image = cv2.filter2D(image,-1,kernel)
        
    # Row check
    peak_len = []
    l = np.random.uniform(low=0, high=image.shape[0], size=1000).astype(int)
    for i in l:
        pixel_array = image[:,:,2][i]
        peaks, val = find_peaks(pixel_array, height=0)
        peak_len.append(len(peaks))
    num_emojis_row = statistics.mode(peak_len)
    
    # Column check
    peak_len = []
    l = np.random.uniform(low=0, high=image.shape[0]//2, size=1000).astype(int)
    for i in l:
        pixel_array = image[:,:,2][:, i]
        peaks, val = find_peaks(pixel_array, height=0)
        peak_len.append(len(peaks))
    num_emojis_col = statistics.mode(peak_len)
    
    dim = (70*num_emojis_row,70*num_emojis_col)    
    img_1 = cv2.resize(img_1, dim, interpolation = cv2.INTER_AREA) 
    
    emoji_list = []
    for i in range(num_emojis_col):
        for j in range(num_emojis_row):
            temp = img_1[i*70:(i+1)*70,j*70:(j+1)*70]
            emoji_list.append(temp)
    
    return emoji_list


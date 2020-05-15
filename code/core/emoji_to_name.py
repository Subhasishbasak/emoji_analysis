# implements CV2.matchtemplate to identify the extracted emojis
# takes the image as input outputs the list names of emojis as a list 

import os
import cv2
from core.image_to_emoji import image_2_emoji_2 

def emoji_2_name(image, method = 'cv2.TM_SQDIFF_NORMED'):
    
    '''
    available methods : 'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'
    '''
    
    methods = eval(method)
    emoji_list = image_2_emoji_2(image)
    emoji_name_list = [0]*len(emoji_list)
    output = [0]*len(emoji_list)
    
    for i in os.listdir('../resource/emoji_database'):
        
        template = cv2.imread('../resource/emoji_database/' + str(i))
        dim = (50,50)
        template = cv2.resize(template, dim, interpolation = cv2.INTER_AREA) 

        for j in range(len(emoji_list)):
            
            res = cv2.matchTemplate(emoji_list[j][:, :, 1] ,template[:, :, 1],methods)

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            try:
                if emoji_name_list[j][0]>min_val:
                    emoji_name_list[j] = (min_val, i)
            except TypeError:
                emoji_name_list[j] = (min_val, i)
            output[j] = emoji_name_list[j][1].split('_')[0]
    
    #print(emoji_name_list)
    return output
    

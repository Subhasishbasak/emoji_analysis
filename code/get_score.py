# mail function to run
# takes the screenshot as input and outputs the sentiment score

import sys
import pickle
import numpy as np
from image_to_name import image_2_name
from ss_to_image import final_crop

with open('../lib/name_2_score.pickle', 'rb') as handle:
    name_2_score = pickle.load(handle)

def image_2_score(image):
    
    output = None
    emoji_name_list = image_2_name(image)
    for i in emoji_name_list:
        try:
            output = np.add(output,np.array(name_2_score[i]))
        except TypeError:
            output = np.array(name_2_score[i])
        except KeyError:
            pass
    
    return output/np.sum(output)


name = sys.argv[1]
file_path = '../resource/screenshots/' + name + '.jpeg'

cropped_image = final_crop(file_path)
l = image_2_score(cropped_image)
print('')
print(' Negative : ',l[0].round(3))
print(' Neutral  : ',l[1].round(3))
print(' Positive : ',l[2].round(3))
print('')

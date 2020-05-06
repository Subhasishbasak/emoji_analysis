# mail function to run
# takes the screenshot as input and outputs the sentiment score

import sys
import pickle
import numpy as np
from image_to_name import image_2_name

with open('../lib/name_2_score.pickle', 'rb') as handle:
    name_2_score = pickle.load(handle)

def image_2_score(file_path):
    
    output = None
    emoji_name_list = image_2_name(file_path)
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

l = image_2_score(file_path)
print('')
print(' Negative : ',l[0].round(3))
print(' Neutral  : ',l[1].round(3))
print(' Positive : ',l[2].round(3))
print('')

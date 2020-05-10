# takes input the image and outputs the list of scores (l = [neg, net, pos])

import pickle
import numpy as np
from core.emoji_to_name import emoji_2_name


with open('../lib/score_dict.pickle', 'rb') as handle:
    score_dict = pickle.load(handle)

def name_2_score(image):
    
    output = None
    emoji_name_list = emoji_2_name(image)
    for i in emoji_name_list:
        try:
            output = np.add(output,np.array(score_dict[i]))
        except TypeError:
            output = np.array(score_dict[i])
        except KeyError:
            pass
    
    return output/np.sum(output)

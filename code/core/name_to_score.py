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

def name_2_diag(image):
	
	l_neg = []
#	l_net = []
	l_pos = []
	emoji_name_list = emoji_2_name(image)

	for i in set(emoji_name_list):

		try:
			l_neg.append([i, score_dict[i][0]])
			l_pos.append([i, score_dict[i][2]])
		except KeyError:
	                pass

	l_neg.sort(key = lambda x: x[1], reverse = True)
	l_pos.sort(key = lambda x: x[1], reverse = True)

	l_neg_top_emojis, l_neg_top_score  = zip(*l_neg[: 5])
	l_pos_top_emojis, l_pos_top_score  = zip(*l_pos[: 5])

	neg = [l_neg_top_emojis, l_neg_top_score]
	pos = [l_pos_top_emojis, l_pos_top_score]

	return neg, pos
				
		
	

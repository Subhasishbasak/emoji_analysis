# plots the graph of sentiment scores if a series of screenshots are provided

import os
import sys
from tqdm import tqdm
import matplotlib.pyplot as plt
from core.name_to_score import name_2_score
from utils.ss_to_image import final_crop

name = sys.argv[1] + '.jpeg'
file_path = '../resource/screenshots/' + sys.argv[1] + '.jpeg'
	
if name in os.listdir('../resource/screenshots/'):
	raise NotImplementedError

file_name = '../resource/screenshots/' + str(sys.argv[1])

l_neg = []
l_net = []
l_pos = []

for i in tqdm(os.listdir(file_name), bar_format='{l_bar}{bar:20}{r_bar}{bar:-10b}'):
	
    file_path = os.path.join(file_name, i)

    cropped_image = final_crop(file_path)
    l_neg.append(name_2_score(cropped_image)[0].round(3))
    l_net.append(name_2_score(cropped_image)[1].round(3))
    l_pos.append(name_2_score(cropped_image)[2].round(3))

plt.figure()

plt.plot(range(len(l_neg)),l_neg, label = 'negative', color='red')
plt.plot(range(len(l_net)),l_net, label = 'neutral', color='orange')
plt.plot(range(len(l_pos)),l_pos, label = 'positive', color='green')

plt.xlabel('time_Stamps')
plt.ylabel('score consolidate de emoji')
plt.title('Sentiment Graph de ' + str(sys.argv[1]))

#plt.ylim(bottom = bottom, top = top)
plt.legend(loc = "lower right", prop = {'size':8})
plt.show()



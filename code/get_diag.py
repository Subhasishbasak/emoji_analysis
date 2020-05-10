# plots the top neg/pos emojis along with their score


import os
import sys
import emoji
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from core.name_to_score import name_2_diag
from utils.ss_to_image import final_crop

name = sys.argv[1] + '.jpeg'
file_path = '../resource/screenshots/' + sys.argv[1] + '.jpeg'
	
if name in os.listdir('../resource/screenshots/'):
	
	cropped_image = final_crop(file_path)
	neg, pos = name_2_diag(cropped_image)
	
	x = pos[0]
	energy = pos[1]

	x_pos = [i for i, _ in enumerate(x)]

	plt.figure(1, figsize=(12,6))
	plt.bar(x_pos, energy, color='green')
	plt.xlabel("positive emojis")
	plt.ylabel("score de sentiment")
	plt.title("report de diagnostic : Top 5 positive emojis")
	plt.xticks(x_pos, x)

	
	x = neg[0]
	energy = neg[1]

	x_neg = [i for i, _ in enumerate(x)]

	plt.figure(2, figsize=(12,6))
	plt.bar(x_pos, energy, color='red')
	plt.xlabel("negative emojis")
	plt.ylabel("score de sentiment")
	plt.title("report de diagnostic : Top 5 negative emojis")
	plt.xticks(x_neg, x)

	plt.show()

else:
	file_name = '../resource/screenshots/' + str(sys.argv[1])

	neg = []
	pos = []

	for i in tqdm(os.listdir(file_name), bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
		
	    file_path = os.path.join(file_name, i)

	    cropped_image = final_crop(file_path)
	    try:

		    neg = neg + list(zip(name_2_diag(cropped_image)[0][0], name_2_diag(cropped_image)[0][1]))
		    pos = pos + list(zip(name_2_diag(cropped_image)[1][0], name_2_diag(cropped_image)[1][1]))

	    except NameError:
		    neg = list(zip(name_2_diag(cropped_image)[0][0], name_2_diag(cropped_image)[0][1]))
		    pos = list(zip(name_2_diag(cropped_image)[1][0], name_2_diag(cropped_image)[1][1]))
	

	neg.sort(key = lambda x: x[1], reverse = True)
	pos.sort(key = lambda x: x[1], reverse = True)

	neg_emoji = [neg[0][0]]
	neg_score = [neg[0][1]]
	
	c = 0
	for i in neg[1:]:

		if not i[0] in neg_emoji:
			c += 1
			neg_emoji.append(i[0])
			neg_score.append(i[1])
		else:
			pass
		if c>3:
			break

	pos_emoji = [pos[0][0]]
	pos_score = [pos[0][1]]
	
	c = 0
	for i in pos[1:]:

		if not i[0] in pos_emoji:
			c += 1
			pos_emoji.append(i[0])
			pos_score.append(i[1])
		else:
			pass
		if c>3:
			break

	
	x = tuple(pos_emoji)
	energy = tuple(pos_score)


	x_pos = [i for i, _ in enumerate(x)]

	plt.figure(1, figsize=(12,6))
	plt.bar(x_pos, energy, color='green')
	plt.xlabel("positive emojis")
	plt.ylabel("sentiment score")
	plt.title("report de diagnostic : Top 5 positive emojis")
	plt.xticks(x_pos, x)

	
	x = tuple(neg_emoji)
	energy = tuple(neg_score)

	x_neg = [i for i, _ in enumerate(x)]

	plt.figure(2, figsize=(12,6))
	plt.bar(x_pos, energy, color='red')
	plt.xlabel("negative emojis")
	plt.ylabel("sentiment score")
	plt.title("report de diagnostic : Top 5 negative emojis")
	plt.xticks(x_neg, x)

	plt.show()

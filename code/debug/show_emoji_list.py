# debug file : to check the extracted emoji list

import os
import sys
from show_cropped_img import get_cropped_image
currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from core.emoji_to_name import emoji_2_name


cropped_img = get_cropped_image(sys.argv[1])
directory = '../' # this made my day !!
os.chdir(directory) 

emoji_name_list = emoji_2_name(cropped_img)

print(emoji_name_list)


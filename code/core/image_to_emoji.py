# takes the process-able image as input outputs the list of emojis as a list of np arrays

import cv2

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


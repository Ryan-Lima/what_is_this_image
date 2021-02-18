# image utils

import os
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt 

def what_is_this_image(mystery_image, show = False):
    if isinstance(mystery_image, np.ndarray):
        print("It's an np.ndarray")
        print(f"It's shape is: {mystery_image.shape}")
        sh = mystery_image.shape
        dims = len(mystery_image.shape)
        print(f"It's dims are: {dims}")
        if dims == 2:
            print("It contains 1 channel")
        else:
            print(f"It contains {sh[-1]} channels")
        print(f"It's size is: {mystery_image.size}")
        print(f"It's dtype is: {mystery_image.dtype}")
        print(f"This Array's min value is {np.min(mystery_image)}")
        print(f"This Array's max value is {np.max(mystery_image)}")
        im_type = 'A'
    elif isinstance(mystery_image, Image.Image):
        print("It's a PIL image")
        print(f"It's format is {mystery_image.format}")
        print(f"It's size is {mystery_image.size}")
        print(f"It's height is {mystery_image.height}")
        print(f"It's width is {mystery_image.width}")
        n_channels = len(mystery_image.split())
        print(f"It has {n_channels} channels")
        print(f"It's mode is {mystery_image.mode}")
        extrema = mystery_image.getextrema()
        print(f"It's (min,max) values are {extrema}")
        im_type = 'P'
    else:
        print("Its not a np.ndarray or a PIL image....")
        im_type = 'U'
    if show == True:
        try:
            if im_type == 'P':
                md = mystery_image.mode
                if md == 'L':
                    plt.imshow(mystery_image, cmap = 'gray')
                    plt.show(block = False)
                    plt.close('all')
                else:
                    plt.imshow(mystery_image)
                    plt.show(block = False)
                    plt.close('all')
            elif im_type == 'A':
                # check channels
                if dims == 2:
                    plt.imshow(mystery_image, cmap = 'gray')
                    plt.colorbar()
                    plt.show(block = False)
                    plt.close('all')

                else:
                    plt.imshow(mystery_image)
                    plt.colorbar()
                    plt.show(block = False)
                    plt.close('all')
            else:
                print('im_type == U or Unknown')
        except:
            print('image could not be shown with plt.imshow() ')
    else:
        pass

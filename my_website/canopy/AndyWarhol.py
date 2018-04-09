import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw
import numpy as np
from PIL import Image

"""def color_paste(original_image):
    #width, height = original_image.size
    #img[r][c] = [0,0,45,128]"""
    
def paste_image():    
    directory = ("C:\\Users\\hssteam\\Desktop\\1.4.7\\Image")   
    filename = os.path.join(directory, 'chris.jpg')
    img = plt.imread(filename) 
    new_image_list = color_image(directory)
    #color_image(img)
    new_directory = os.path.join(directory, 'modified')

    #create the axes
    fig, ax = plt.subplots(2, 2)
    #pastes the image four times on four different subplots in a 2x2 axes
    """img = new_image_list[0]"""
    ax[0,0].imshow(new_image_list[0])
    ax[0,0].set_axis_off()
    """img = new_image_list[1]"""
    ax[0,1].imshow(new_image_list[1])
    ax[0,1].set_axis_off()
    """img = new_image_list[2]"""
    ax[1,0].imshow(new_image_list[2])
    ax[1,0].set_axis_off()
    """img = new_image_list[3]"""
    ax[1,1].imshow(new_image_list[3])
    ax[1,1].set_axis_off()
    #removes the gaps between the subplots
    plt.subplots_adjust(wspace=0, hspace=0)
    """new_image_filename = os.path.join(Andified + '.jpg')
    #new_image.save(new_image_filename)"""
    plt.show()#Shows the image
    img2=PIL.Image.fromarray(plt)
    img2_filename = os.path.join(new_directory, filename + 'color' + '.jpg')
    img2.save(img2_filename)
def color_image(img):
    new_image_list = []
    directory = ("C:\\Users\\hssteam\\Desktop\\1.4.7\\Image")   
    filename = os.path.join(directory, 'chris.jpg')
    img = plt.imread(filename) 
    tempimage=plt.imread(filename) 
    height = len(tempimage)
    width = len(tempimage[0])
    for r in range(height):
        for c in range(width):
            if sum(tempimage[r][c])>300:
                tempimage[r][c]=[0,0,255] #Colors the image BLUE
    new_image_list.append(tempimage)#appends the image to a list

    tempimage2=plt.imread(filename) 
    height = len(tempimage2)
    width = len(tempimage2[0])
    for r in range(height):
        for c in range(width):
            if sum(tempimage2[r][c])>300:
                tempimage2[r][c]=[255,0,0] #Colors RED
    new_image_list.append(tempimage2) #appends the image to a list
    
    tempimage3=plt.imread(filename) 
    height = len(tempimage3)
    width = len(tempimage3[0])
    for r in range(height):
        for c in range(width):
            if sum(tempimage3[r][c])>300:
                tempimage3[r][c]=[0,255,0] #Colors the image GREEN
    new_image_list.append(tempimage3) #appends the image to a list
       
    tempimage4=plt.imread(filename) 
    height = len(tempimage4)
    width = len(tempimage4[0])
    for r in range(height):
        for c in range(width):
            if sum(tempimage4[r][c])>300:
                tempimage4[r][c]=[255,255,0] #Colors the image YELLOW
    new_image_list.append(tempimage4) #appends the image to a list

    return new_image_list
    
paste_image()
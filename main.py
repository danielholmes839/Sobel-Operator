# Daniel Holmes
# 2019/1/6
# Sobel Operator
# Takes an image from a file or url and outline the edges using a sobel operator

import os
from functions import sobel_from_file, sobel_from_url

while True:
    file_or_url = str(input('image from file or url: '))            # choose to get an image from a url or a file

    if file_or_url.lower() == 'file':
        image_name = str(input('Image name: '))                     # image name
        folder_name = image_name.split('.')[0]                      # folder name will be the image name excluding the file type

        if not os.path.exists(folder_name):                         # if there is no folder
            os.mkdir(folder_name)                                   # create a folder

        sobel_image = sobel_from_file(image_name)                                   # get the image after the sobel operator
        sobel_image.save(folder_name + os.sep + folder_name + " sobel.png", 'png')  # save the to the folder

    elif file_or_url.lower() == 'url':
        # very similar to the code in the previous if statement
        image_url = str(input('Image url: '))
        folder_name = str(input('output folder (will be created if it does not exist): '))  # folder name isn't set automatically

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        sobel_image = sobel_from_url(image_name)                                            # changed to sobel_from_url instead of sobel_from_file
        sobel_image.save(folder_name + os.sep + folder_name + " sobel.png", 'png')

    else:
        print('Sorry you did not enter a valid option. Valid options are: file, url')
        continue  # restart

    yes_or_no = str(input('would you like to process more images? [y/n]: ')).lower()
    if yes_or_no != 'y':
        break

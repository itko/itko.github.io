import os
from pathlib import Path
from PIL import Image


def ensure_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def resize_image(file, size, savePath):
    with Image.open(file) as im:
        # Resize
        im.thumbnail((size, size), Image.ANTIALIAS)
        print(savePath)
        im.save(savePath)


def resize_folder(path, size):
    for item in os.listdir(path):
        if '.jpg' in item or '.JPG' in item:
            imgName = item.split('.')[0]
            imgExt = item.split('.')[1]
            imgPath = os.path.join(path, item)
            folder = 'resize_' + str(size)
            ensure_folder(os.path.join(path, folder))
            file = imgName + '_' + str(size) + '.' + imgExt
            # Check if it exists already
            if file in os.listdir(os.path.join(path, folder)):
                print('No need to resize, already done.')
            else:
                resize_image(imgPath, size, os.path.join(path, folder, file))
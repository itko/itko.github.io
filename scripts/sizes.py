from PIL import Image
import collections
import glob
import os
import yaml
import copy
import json
import argparse


jsonPath = '../assets/gallery.json'
SIZES = [300, 1000, 2000]


def ensure_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def resize_image(file, size, savePath):
    with Image.open(file) as im:
        # Resize
        im.thumbnail((size, size), Image.ANTIALIAS)
        im.save(savePath)


def store_in_json(data, filePath):
    with open(filePath, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def read_from_json(filePath):
    with open(filePath, 'r') as jsonFile:
        data = json.load(jsonFile)
    return data


def get_previous_processed_images(filePath):
    gallery = read_from_json(filePath)
    files = []
    return gallery['images']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--source',
        help='Path of source folder (folder containing original photos',
        nargs='+')
    parser.add_argument('--destination', help='Path of destination folder')
    parser.add_argument(
        '--overwrite',
        action='store_true',
        help='OVerwrite photos even if they have previously been resized')
    args = parser.parse_args()

    if not (args.source or args.destination):
        parser.error('Provide both source and destination folders')

    print('Resizing...')
    photos = []
    for source in args.source:
        print(source)
        SOURCE_DIRECTORY = source
        ensure_folder(SOURCE_DIRECTORY)
        DEST_DIRECTORY = args.destination
        ensure_folder(DEST_DIRECTORY)
        folderName = os.path.split(DEST_DIRECTORY)[1]
        fileNames = os.listdir(SOURCE_DIRECTORY)
        store = {}
        store['gallery_name'] = folderName
        # Check if a file already exists
        if os.path.exists(jsonPath):
            # Get a list of previously resized images
            photos += get_previous_processed_images(jsonPath)
        for imgName in fileNames:
            paths = []
            responsive = ''
            photo = {}
            for size in SIZES:
                imagePath = os.path.join(SOURCE_DIRECTORY, imgName)
                # Only take files (assume all files are images)
                if os.path.isfile(imagePath):
                    newImgName = imgName.split(
                        '.')[0] + '-' + str(size) + '.' + imgName.split('.')[1]
                    newImagePath = os.path.join(DEST_DIRECTORY, newImgName)
                    # Check if we processed it already
                    if photos:
                        if not imgName in [photo['name'] for photo in photos]:
                            print(newImgName)
                            resize_image(
                                imagePath,
                                size,
                                newImagePath)
                            paths.append(newImagePath[2:])
                            responsive += (paths[-1] + ' ' + str(size) + ',')
                        else:
                            print('Skipping {}'.format(imgName))
            photo['name'] = imgName
            photo['tag'] = os.path.split(SOURCE_DIRECTORY)[1]
            photo['year'] = None
            photo['paths'] = paths
            photo['responsive'] = responsive[:-2]
            photos.append(photo)
    store['images'] = photos
    store_in_json(store, jsonPath)
    print('Done!')


if __name__ == '__main__':
    main()

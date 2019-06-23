import os

PATH = os.path.expanduser('/media/itto/TOSHIBA EXT/Photos/To sort')

for item in os.listdir(PATH):
    itemPath = os.path.join(PATH, item)
    if os.path.isfile(itemPath):
        pass
    else:
        day, month, year = item.split('-')
        newName = '{}-{}-{}'.format(year, month, day)
        newPath = os.path.join(PATH, newName)
        os.rename(itemPath, newPath)

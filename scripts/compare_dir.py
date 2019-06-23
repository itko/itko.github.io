import os
from shutil import copyfile

FOLDER_A = '/media/itto/TOSHIBA EXT/Photos/Southeast Asia'
FOLDER_B = '/media/itto/disk/PRIVATE/AVCHD/BDMV/STREAM'
files_a = []
files_b = []
for dirpath, dirnames, filenames in os.walk(FOLDER_A):
    files_a += filenames

for dirpath, dirnames, filenames in os.walk(FOLDER_B):
    files_b += filenames

inA_notB = []
inB_notA = []
for file in files_b:
    if file not in files_a:
        inB_notA.append(file)
for file in files_a:
    if file not in files_b:
        inA_notB.append(file)

print('{} in Folder A. {} in Folder B.'.format(len(files_a), len(files_b)))
print('In A but not B: {}'.format(len(inA_notB)))
print('In B but not A: {}'.format(len(inB_notA)))


def EnsureFolder(path):
    if os.path.isdir(path):
        pass
    else:
        # Make folder
        os.mkdir(path)


def CopyLeftoverFromBToA():
    for file in inB_notA:
        EnsureFolder(os.path.join(FOLDER_A, 'transfer'))
        src = os.path.join(FOLDER_B, file)
        dst = os.path.join(FOLDER_A, 'transfer', file)
        if not os.path.exists(dst):
            print('Copying {}'.format(file))
            copyfile(src, dst)
        else:
            print('{} previously copied'.format(file))
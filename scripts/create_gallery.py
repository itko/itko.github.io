import dropbox
from dominate import document
from dominate.tags import *
import os
from pathlib import Path
from PIL import Image
import yaml


def ToWebsiteRoot(path):
    website = str(Path(__file__).parent.parent)
    return os.path.join(website, path)


with open(ToWebsiteRoot('tokens.yml')) as f:
    tokens = yaml.load(f)

accessToken = tokens['dropbox']

db = dropbox.Dropbox(accessToken)

gallery = div(cls='photo-gallery')

resize_folder('/media/itto/SHARE/Photos/simple_gallery', 1000)

with gallery:
    for entry in db.files_list_folder('').entries:
        link = db.sharing_create_shared_link(entry.path_lower)
        src = link.url.split('?')[0]
        src += '?raw=1'
        figure(cls='photo-figure').add(img(src=src))


with open(ToWebsiteRoot('_pages/photos.md'), 'w+') as f:
    f.write('---')
    f.write('\r\n')
    f.write('permalink: /photos/\r\n')
    f.write('layout: gallery\r\n')
    f.write('author_profile: false\r\n')
    f.write('\r\n')
    f.write('---')
    f.write('\r\n')

    f.write(str(gallery))

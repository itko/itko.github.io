from dominate import document
from dominate.tags import *
import os, yaml
import dropbox


with open('./tokens.yml') as f:
    tokens = yaml.safe_load(f)

accessToken = tokens['dropbox']

db = dropbox.Dropbox(accessToken)

gallery = div(cls='photo-gallery')

with gallery:
    for entry in db.files_list_folder('').entries:
        link = db.sharing_create_shared_link(entry.path_lower)
        src = link.url.split('?')[0]
        src += '?raw=1'
        figure(cls='photo-figure').add(img(data_src=src, cls='lazyload'))


with open('../_pages/photos.md', 'w+') as f:
    f.write('---')
    f.write('\r\n')
    f.write('permalink: /photos/\r\n')
    f.write('layout: gallery\r\n')
    f.write('author_profile: false\r\n')
    f.write('---')
    f.write('\r\n')

    f.write(str(gallery))

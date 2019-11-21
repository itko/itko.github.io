from dominate import document
from dominate.tags import *
import os, yaml, json, requests

with open('./keys.yml') as f:
    keys = yaml.safe_load(f)

API_KEY = keys['cloudinary_api']
SECRET_KEY = keys['cloudinary_secret']

req = ''
req += 'https://'
req += API_KEY
req += ':'
req += SECRET_KEY
req += '@'
req += 'api.cloudinary.com/v1_1/itko/resources/image/upload/?prefix=photos/original&max_results=50'
res = requests.get(req)

images = json.loads(res.content)['resources']

gallery = div(cls='photo-gallery')

with gallery:
    root = 'https://res.cloudinary.com/itko/image/upload/'
    for i,im in enumerate(images):
        data_src = root + im['public_id']
        src = root + 't_lqip/' + im['public_id']
        figure(cls='photo-figure').add(img(cls='lazyload',id='img'+str(i),src=src,data_src=data_src))


with open('../_pages/photos.md', 'w+') as f:
    f.write('---')
    f.write('\r\n')
    f.write('title: Photos\r\n')
    f.write('permalink: /photos/\r\n')
    f.write('layout: gallery\r\n')
    f.write('author_profile: false\r\n')
    f.write('---')
    f.write('\r\n')

    f.write(str(gallery))

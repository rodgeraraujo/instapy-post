import time
from instapy_cli import client

username = 'pyrocodesoftware'
password = 'password'
image = 'photo_2019_stories.jpg'

image_files = ['photo_2019_stories.jpg'] #, 'docs/image-story-2.jpg', 'docs/image-story-3.jpg', 'docs/image-story-4.jpg']

with client(username, password) as cli:
    for i in range(0, len(image_files)):
        print('image: ', image_files[i])
        res = cli.upload(image_files[i], story=True)
        print('IG: >> ', res)
        time.sleep(1)
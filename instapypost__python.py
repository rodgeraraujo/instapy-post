from instapy_cli import client

# instagram username
username = 'rodgeraraujo'
# you account password
password = 'password'
# here you put the image path
image = 'photo_2019_post.jpg'
# here is the description of your post
content = 'Sunset!' + '\r\n' + 'Posted with python script :)' + '\r\n' + '#sunset #pic #pythoncode #developer #learningcode'
with client(username, password) as cli:
    cli.upload(image, content) 

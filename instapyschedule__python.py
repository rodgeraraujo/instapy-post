import datetime
from instapy_cli import client

# instagram username
username = 'pyrocodesoftware'
# you account password
password = 'pyrocode321'
# here you put the image path
image = 'photo_2019_schedule.jpg'
# here is the description of your post
content = '#pyrocode #code #pic #pythoncode #developer #learningcode'

loop = True

while loop:
    schedule_datetime = datetime.datetime(2019, 8, 5, 0, 13, 0).strftime("%d/%m/%Y %H:%M:%S")
    current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(schedule_datetime)
    print(current_datetime)

    if schedule_datetime == current_datetime:
        loop = False
        with client(username, password) as cli:
            cli.upload(image, content) 
        print('posted post')

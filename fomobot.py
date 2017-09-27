from twython import Twython
import random
from time import sleep
from picamera import PiCamera

#Add your secret information from Twitter back in here
APP_KEY = ""
APP_SECRET = ""

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter.verify_credentials()


while True:
    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        sleep(2)
        camera.capture("output.png",format='png')
        camera.stop_preview()
    
    message = "Wish you were here!"
    photo = open('output.png', 'rb')
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=message, media_ids=[response['media_id']])
    sleep(60)

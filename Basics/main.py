from sys import api_version
from googleapiclient.discovery import build

key = "AIzaSyD8XSh0zwR4a6QGOhikq9v0XJVGReOh6U4"


youtube = build('youtube', 'v3', developerKey=key)

request = youtube.channels().list(
    part='statistics',
    id='UC16q47Erm1NjuK_AXzuOUGQ' #channel id
)


response = request.execute()

print(response)





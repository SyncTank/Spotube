import requests
from requests.auth import HTTPBasicAuth
import pyyoutube


class YoutubeAuth:
    def __init__(self):
        self.__client_id: str = 'YOUR_CLIENT_ID'
        self.__client_secret: str = 'Your_SECRET_KEY'
        self._content: list = []
        self.__base_url: str = ''
        self.__url_token: str = ""
        self.response: str = ''
        self.__token: str = ''
        print("test")

# private file implement extend with Auth class.
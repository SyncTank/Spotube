import requests
import os 
import json

from Auth import Auth, pull_json_data

def youtube_relog() -> NotImplemented:
    return NotImplemented

class YoutubeAuth(Auth):
    def __init__(self):
        super().__init__()
        self.__url_token: str = ""
        self.__base_url: str = ''
        self.__self_path: str = "YoutubeClientAuth2.txt"
        self.setup_client(self.__self_path)
        try:
            self.__token = self.authenticate(self.__url_token)
        except Exception as e:
            print(e)

    def request_playlist(self, request: str) -> NotImplemented:
        return NotImplemented

    def create_playlist(self, request: str) -> NotImplemented:
        return NotImplemented

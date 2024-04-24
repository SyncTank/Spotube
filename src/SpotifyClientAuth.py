import os.path

import requests
from requests.auth import HTTPBasicAuth


class SpotifyAuth:
    def __init__(self):
        self.__client_id: str = 'YOUR_CLIENT_ID'
        self.__client_secret: str = 'Your_SECRET_KEY'
        self.content: list = []
        self.__base_url: str = 'https://api.spotify.com/v1/'
        self.__url_token: str = "https://accounts.spotify.com/api/token"
        self.response: str = ''
        self.__token: str = ''
        self.__setup_client()
        try:
            self.__authenticate()
        except Exception as e:
            print(e)

    def __setup_client(self) -> None:
        try:
            with open("private/SpotifyClientAuth.txt", "r") as file:
                self.content = file.readlines()
        except FileNotFoundError:
            print("File does not exist.")

        if self.content is not None:
            self.__client_id = self.content[0].replace("\n", "")
            self.__client_secret = self.content[1]
        else:
            print("Please read docs or contact the administrator.")
        self.content.clear()

    def __authenticate(self, status=200) -> None:
        if status == 200 and len(self.__token) < 1:
            self.response = requests.post(self.__url_token,
                                          data={'grant_type': 'client_credentials'},
                                          auth=HTTPBasicAuth(self.__client_id, self.__client_secret))
            self.__token = self.response.json().get('access_token')
        elif status != 200:
            self.response = requests.post(self.__url_token,
                                          data={'grant_type': 'refresh_token',
                                                'refresh_token': self.__token, },
                                          auth=HTTPBasicAuth(self.__client_id, self.__client_secret))

            self.__token = self.response.json().get('access_token')
        else:
            raise Exception("Invalid token.")

        print(f"Access Token: {self.__token}")

    def request_example(self, request: str) -> None:
        headers = {"Authorization": f"Bearer {self.__token}", }
        response = requests.get(f"{self.__base_url}{request}", headers=headers)

        print(response.json(), response.status_code)

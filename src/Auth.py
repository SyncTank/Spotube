import json
import os
from requests_oauthlib import HTTPBasicAtuh

class Auth:
    def __init__(self):
        self.__client_id: str = 'YOUR_CLIENT_ID'
        self.__client_secret: str = 'Your_SECRET_KEY'
        self.content: list = []
        self.__url_token: str = url_token
        self.__file_path: str = file_path
        self.response: str = ''
        self.__token: str = ''
        self.__setup_client(self.__file_path)
        try:
            self.__authenticate()
        except Exception as e:
            print(e)

    def __setup_client(self, file_path: str) -> None:
        try:
            with open(f"private/{file_path}", "r") as file:
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


    def pull_json_data(self, pulldata: str) -> dict:
        data : dict = dict()
        try:
            with open(pulldata, 'r') as json_data:
                data = json.load(json_data)
        except Exception as e:
            print(e)

        return data

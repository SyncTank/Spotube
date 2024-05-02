import json
import os
import requests
from requests.auth import HTTPBasicAuth


def pull_json_data(pulldata: str) -> dict:
    data: dict = dict()
    try:
        with open(pulldata, 'r') as json_data:
            data = json.load(json_data)
    except Exception as e:
        print(e)

    return data

def set_path() -> str:
    while "src" in os.getcwd():
        os.chdir("..")
    return os.getcwd()

class Auth:
    def __init__(self):
        self.__client_id: str = 'YOUR_CLIENT_ID'
        self.__client_secret: str = 'Your_SECRET_KEY'
        self.content: list = []
        self.response = ''
        self.__token: str = ''
        self.file_dir: str = os.getcwd()

    def setup_client(self, file_path: str) -> None:
        try:
            print(f"{self.file_dir}/private/{file_path}")
            with open(f"{self.file_dir}/private/{file_path}", "r") as file:
                self.content = file.readlines()
        except FileNotFoundError:
            print("File does not exist.")

        if self.content is not None:
            print(f"{self.content}, {type(self.content)}")
            self.__client_id = self.content[0].replace("\n", "")
            self.__client_secret = self.content[1]
        else:
            print("Please read docs or contact the administrator.")
        self.content.clear()

    def authenticate(self, url_token: str, status: int = 200) -> str:
        if status == 200 and len(self.__token) < 1:
            self.response = requests.post(url_token,
                                          data={'grant_type': 'client_credentials'},
                                          auth=HTTPBasicAuth(self.__client_id, self.__client_secret))
            self.__token = self.response.json().get('access_token')
        elif status != 200:
            self.response = requests.post(url_token,
                                          data={'grant_type': 'refresh_token',
                                                'refresh_token': self.__token, },
                                          auth=HTTPBasicAuth(self.__client_id, self.__client_secret))

            self.__token = self.response.json().get('access_token')
        else:
            raise Exception("Invalid token.")

        print(f"Access Token: {self.__token}\nData reponse: {self.response}")
        return self.__token

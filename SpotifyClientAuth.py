import requests
from requests.auth import HTTPBasicAuth


class App_authentication:
    def __init__(self):
        self._client_id: str = 'YOUR_CLIENT_ID'
        self._client_secret: str = 'Your_SECRET_KEY'
        self._content: list = []
        self._base_url: str = 'https://api.spotify.com/v1/'
        self._response: str = ''
        self.__token: str = ''
        self.refresh_token: str = ''
        self._setup_client()
        self._authenticate()

    def _setup_client(self) -> None:
        try:
            with open("ClientAuth.txt", "r") as file:
                self._content = file.readlines()
        except FileNotFoundError:
            print("File does not exist.")

        if self._content is not None:
            self._client_id = self._content[0].replace("\n", "")
            self._client_secret = self._content[1]
        else:
            print("Please read docs or contact the administrator.")

    def _authenticate(self, status=200) -> None:
        if status == 200:
            # Authenticate with Spotify API
            self._response = requests.post('https://accounts.spotify.com/api/token',
                                          data={'grant_type': 'client_credentials'},
                                          auth=HTTPBasicAuth(self._client_id, self._client_secret))
            # Extract access token from _response
            self.__token = self._response.json().get('access_token')
        else:
            # Refresh _response to get a new token - Testing
            self._response = requests.post('https://accounts.spotify.com/api/token',
                                          data={'grant_type': 'refresh_token',
                                                'refresh_token': self.__token,},
                                          auth=HTTPBasicAuth(self._client_id, self._client_secret))

            self.__token = self._response.json().get('access_token')


    def request_example(self) -> None:
        headers = {"Authorization": f"Bearer {self.__token}", }
        _response = requests.get("https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb", headers=headers)

        print(_response.json(), _response.status_code)

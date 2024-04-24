import requests
from requests.auth import HTTPBasicAuth


class SpotifyAuth:
    def __init__(self):
        self.__client_id: str = 'YOUR_CLIENT_ID'
        self.__client_secret: str = 'Your_SECRET_KEY'
        self._content: list = []
        self.__base_url: str = 'https://api.spotify.com/v1/'
        self.__url_token: str = "https://accounts.spotify.com/api/token"
        self.response: str = ''
        self.__token: str = ''
        self._setup_client()
        self._authenticate()

    def _setup_client(self) -> None:
        try:
            with open("/private/SpotifyClientAuth.txt", "r") as file:
                self._content = file.readlines()
        except FileNotFoundError:
            print("File does not exist.")

        if self._content is not None:
            self.__client_id = self._content[0].replace("\n", "")
            self.__client_secret = self._content[1]
        else:
            print("Please read docs or contact the administrator.")

    def _authenticate(self, status=200) -> None:
        if status == 200:
            # Authenticate with Spotify API
            self.response = requests.post(self.__url_token,
                                          data={'grant_type': 'client_credentials'},
                                          auth=HTTPBasicAuth(self.__client_id, self.__client_secret))
            # Extract access token from _response
            self.__token = self.response.json().get('access_token')
        else:
            # Refresh _response to get a new token - Testing
            self.response = requests.post(self.__url_token,
                                          data={'grant_type': 'refresh_token',
                                                'refresh_token': self.__token, },
                                          auth=HTTPBasicAuth(self.__client_id, self.__client_secret))

            self.__token = self.response.json().get('access_token')

    def request_example(self, request: str) -> None:
        request = "artists/4Z8W4fKeB5YxbusRsdQVPb"
        headers = {"Authorization": f"Bearer {self.__token}", }
        response = requests.get(f"{self.__base_url}{request}", headers=headers)

        print(response.json(), response.status_code)

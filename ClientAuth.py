import requests
from requests.auth import HTTPBasicAuth


class App_authentication:
    def __init__(self):
        self._client_id: str = 'YOUR_CLIENT_ID'
        self._client_secret: str = 'Your_SECRET_KEY'
        self._content: list = []
        self.base_url: str = 'https://api.spotify.com/v1/'
        self.response: str = ''
        self.access_token: str = ''
        self.refresh_token: str = ''
        self.setup_client()
        self.authenticate()
        self.request_example()

    def setup_client(self) -> None:
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

    def authenticate(self, status=200) -> None:
        if status == 200:
            # Authenticate with Spotify API
            self.response = requests.post('https://accounts.spotify.com/api/token',
                                          data={'grant_type': 'client_credentials'},
                                          auth=HTTPBasicAuth(self._client_id, self._client_secret))
            # Extract access token from response
            self.access_token = self.response.json().get('access_token')
        else:
            # Refresh response to get a new token - Testing
            self.response = requests.post('https://accounts.spotify.com/api/token',
                                          data={'grant_type': 'refresh_token',
                                                'refresh_token': self.access_token,},
                                          auth=HTTPBasicAuth(self._client_id, self._client_secret))

            self.access_token = self.response.json().get('access_token')


    def request_example(self) -> None:
        headers = {"Authorization": f"Bearer {self.access_token}", }
        response = requests.get("https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb", headers=headers)

        print(response.json(), response.status_code)

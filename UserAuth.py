class App_authentication:
    def __init__(self):
        self._client_id: str = 'YOUR_CLIENT_ID'
        self._client_secret: str = 'Your_SECRET_KEY'
        self._content: list = []
        self.setup_client()
        self.authenticate()

    def setup_client(self) -> None:
        try:
            with open("UserAuth.txt", "r") as file:
                self._content = file.readlines()
        except FileNotFoundError:
            print("File does not exist.")

    def authenticate(self) -> None:
        if self._content is not None:
            self._client_id = self._content[0]
            self._client_secret = self._content[1]
        else:
            print("Please read docs or contact the administrator.")

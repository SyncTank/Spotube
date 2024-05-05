import json
import os
import requests

from Auth import Auth, pull_json_data


def spotify_relog() -> set:
    playlist_data = dict(pull_json_data('SpotifyDump.json'))
    playlist_log = set()
    print(os.getcwd())
    playlist_data = playlist_data['tracks']['items']

    for item in playlist_data:
        song = item['track']['name']
        album = item['track']['album']['name']
        artist = item['track']['artists'][0]['name']
        playlist_log.add((song, album, artist))

    #for i in playlist_log:
    #    print(i)

    return playlist_log


class SpotifyAuth(Auth):
    def __init__(self):
        super().__init__()
        self.__url_token: str = "https://accounts.spotify.com/api/token"
        self.__base_url: str = 'https://api.spotify.com/v1/'
        self.__self_path: str = "SpotifyClientAuth.txt"
        self.__search_list: list  = []
        self.setup_client(self.__self_path)
        try:
            self.__token = self.authenticate(self.__url_token)
        except Exception as e:
            print(e)

    def request_playlist(self, request: str) -> None:
        playlist_name = "SpotifyDump.json"
        if os.path.exists(playlist_name):
            os.remove(playlist_name)

        playlist_request = self.__base_url + 'playlists/' + request
        field_filter = '?fields=tracks.items%28track%28name%2C+artists%2C+album%28name%29+%29%29'
        headers = {"Authorization": f"Bearer {self.__token}"}
        response = requests.get(playlist_request + field_filter, headers=headers, stream=True).json()

        with open("SpotifyDump.json", "w", encoding='utf-8') as file:
            json.dump(response, file, ensure_ascii=False, indent=4)


    def spotify_search(self, log_items: list) -> None:
        pass


    def create_playlist(self, request: str):
        return NotImplementedError

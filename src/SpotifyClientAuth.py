import json
import os

import requests

from Auth import Auth, pull_json_data


class SpotifyAuth(Auth):
    def __init__(self):
        super().__init__()
        self.__url_token: str = "https://accounts.spotify.com/api/token"
        self.__base_url: str = 'https://api.spotify.com/v1/'
        self.__self_path: str = "SpotifyClientAuth.txt"
        self.setup_client(self.__self_path)
        try:
            self.authenticate(self.__url_token)
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

    def spotify_playlist_relog(self) -> set:
        playlist_data = pull_json_data('SpotifyDump.json')
        playlist_log = set()

        for item in playlist_data['tracks']['items']:
            song = item['track']['name']
            album = item['track']['album']['name']
            artist = item['track']['artists'][0]['name']
            playlist_log.add((song, album, artist))

        return playlist_log

    def create_playlist(self, request: str):
        return NotImplementedError

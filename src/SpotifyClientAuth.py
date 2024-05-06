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
        self.__search_list: list = []
        self.setup_client(self.__self_path)
        try:
            self.__token = self.authenticate(self.__url_token)
        except Exception as e:
            print(e)
        self.__header = {"Authorization": f"Bearer {self.__token}"}

    def request_playlist(self, request: str) -> None:
        playlist_name = "SpotifyDump.json"
        if os.path.exists(playlist_name):
            os.remove(playlist_name)

        playlist_request = self.__base_url + 'playlists/' + request
        field_filter = '?fields=tracks.items%28track%28name%2C+artists%2C+album%28name%29+%29%29'
        response = requests.get(playlist_request + field_filter, headers=self.__header, stream=True).json()

        with open("SpotifyDump.json", "w", encoding='utf-8') as file:
            json.dump(response, file, ensure_ascii=False, indent=4)

    def spotify_search(self, log_items: list) -> None:
        for song in log_items:
            song_search = self.__base_url + "search?q=" + song.replace(" ", "+") + "&type=track&limit=10"
            r = requests.get(song_search, headers=self.__header, stream=True).json()
            print(song, r['tracks']['items'][0]['name'], r['tracks']['items'][0]['id'])
            self.add_too_playlist(r['tracks']['items'][0]['id'])
            break

    def add_too_playlist(self, request) -> None:
        # 4ChHbaRX9II5dHCKrPkgWP
        headers = {
            'Authorization': 'Bearer ' + self.__token,
            'Content-Type': 'application/json'
        }
        playlist_url = self.__base_url + "playlists/" + "4ChHbaRX9II5dHCKrPkgWP" + "/tracks?uris=spotify%3Atrack%3A" + request
        print(playlist_url)
        response = requests.post(url=playlist_url, headers=headers, data={"uris": ["string"],"position": 0})
        print(response)

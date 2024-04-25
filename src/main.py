import json
import InterfaceSpt

from SpotifyClientAuth import SpotifyAuth
from YoutubeClientAuth import YoutubeAuth
from InterfaceSpt import MainWindow
import pyyoutube


# New_user = App_authentication()
# New_user.request_example()

# https://open.spotify.com/playlist/6ykxrtWbLE6KzU8ISQ6xqM?si=ad4e308e24cf4381
# https://open.spotify.com/playlist/4pydUxIkuBaI3T1v6lhImj
# https://open.spotify.com/playlist/4pydUxIkuBaI3T1v6lhImj?si=7ad92174bb9a4fac&nd=1&dlsi=618e68b889064fe8

# https://youtube.com/playlist?list=PLaQ2znw11EHJ0KlUDDzuXyqll-db3hWX6&si=WEOSDl4QMg2JlcW4

def pull_json_data(pulldata: str) -> dict:
    data = None
    try:
        with open(pulldata, 'r') as json_data:
            data = json.load(json_data)
    except Exception as e:
        print(e)

    return data


def spotify_playlist_relog() -> set:
    playlist_data = pull_json_data('SpotifyDump.json')
    playlist_log = set()

    for item in playlist_data['tracks']['items']:
        song = item['track']['name']
        album = item['track']['album']['name']
        artist = item['track']['artists'][0]['name']
        playlist_log.add((song, album, artist))

    return playlist_log


def main():
    #spotify_client = SpotifyAuth()
    #youtube_client = YoutubeAuth()

    #spotify_client.request_playlist("4pydUxIkuBaI3T1v6lhImj")
    #spotify_data = spotify_playlist_relog()

    main_window = MainWindow(800, 600)


if __name__ == '__main__':
    main()

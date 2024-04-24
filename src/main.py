from SpotifyClientAuth import SpotifyAuth
from YoutubeClientAuth import YoutubeAuth
from InterfaceSpt import MainWindow
import pyyoutube
import asyncio


# New_user = App_authentication()
# New_user.request_example()

# https://open.spotify.com/playlist/6ykxrtWbLE6KzU8ISQ6xqM?si=ad4e308e24cf4381

# https://youtube.com/playlist?list=PLaQ2znw11EHJ0KlUDDzuXyqll-db3hWX6&si=WEOSDl4QMg2JlcW4


def main():
    spotify_client = SpotifyAuth()
    youtube_client = YoutubeAuth()

    spotify_client.request_example("artists/4Z8W4fKeB5YxbusRsdQVPb")

    main_window = MainWindow(800, 600)

if __name__ == '__main__':
    main()

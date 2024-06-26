import os

from Auth import set_path, Auth
import time
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect
from SpotifyClientAuth import SpotifyAuth, spotify_relog
from YoutubeClientAuth import YoutubeAuth, youtube_relog
from InterfaceSpt import MainWindow

#from YoutubeClientAuth import YoutubeAuth
#from InterfaceSpt import MainWindow


# New_user = App_authentication()
# New_user.request_example()

# https://open.spotify.com/playlist/6ykxrtWbLE6KzU8ISQ6xqM?si=ad4e308e24cf4381
# https://open.spotify.com/playlist/4pydUxIkuBaI3T1v6lhImj
# https://open.spotify.com/playlist/4pydUxIkuBaI3T1v6lhImj?si=7ad92174bb9a4fac&nd=1&dlsi=618e68b889064fe8

# https://youtube.com/playlist?list=PLaQ2znw11EHJ0KlUDDzuXyqll-db3hWX6&si=WEOSDl4QMg2JlcW4
# https://youtube.com/playlist?list=PLaQ2znw11EHIBF-SH802jObjHSpTB4ZNV&si=9BFg_iQSN_GNryFY

# Playlist to addinto for test
# https://open.spotify.com/playlist/4ChHbaRX9II5dHCKrPkgWP?si=03c68fd95cbe4833


app = Flask(__name__)

app.secret_key = ""
app.config['SESSION_COOKIE_NAME'] = 'User Cookie'


@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page():
    sp_oauth = create_spotify_oauth()
    session.clear()
    access_token = spotify_relog()
    return 'redirect'





def create_spotify_oauth():
    return SpotifyOAuth(client_id=clientid,
                        client_secret=clientsecrt,
                        redirect_uri=url_for('redirect_page', _external=True),
                        scope='user-library-read playlist-modify-private playlist-modify-public',)


app.run()


def main():
    set_path()

    #spotify_client = SpotifyAuth()
    #youtube_client = YoutubeAuth()
    #auth_client = Auth()

    #spotify_client.request_playlist("4pydUxIkuBaI3T1v6lhImj")
    #youtube_client.request_playlist("https://youtube.com/playlist?list=PLaQ2znw11EHIBF-SH802jObjHSpTB4ZNV&si=9BFg_iQSN_GNryFY")

    #spotify_data = spotify_relog()
    #youtube_data = youtube_relog()

    #spotify_client.spotify_search(youtube_data)

    #main_window = MainWindow(800, 600)


if __name__ == '__main__':
    main()

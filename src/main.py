from Auth import set_path, Auth
import time
import spotipy.oauth2 as SpotifyOAuth
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
app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key = 'secret key'
TOKEN_INFO = 'token_info'


@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('login', _external=True))


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        # if the token info is not found, redirect the user to the login route
        redirect(url_for('login', _external=False))

    # check if the token is expired and refresh it if necessary
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        redirect_uri=url_for('redirect_page', _external=True),
        scope='user-library-read playlist-modify-public playlist-modify-private'
    )


app.run(debug=True)


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

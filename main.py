from SpotifyClientAuth import Spotify_Auth
from YoutubeClientAuth import Youtube_Auth
from InterfaceSpt import MainWindow
import pyyoutube
import asyncio


# New_user = App_authentication()
# New_user.request_example()

#main_window = MainWindow(800, 600)

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
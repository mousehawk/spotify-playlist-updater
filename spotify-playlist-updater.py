import time
import schedule
import spotipy
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

import base64

print("Starting Playlist Updater")
  
def func():
    scope = 'playlist-modify-public ugc-image-upload'

    # Spotify Username
    username = 'username'

    # Spotify Developer App Client ID and Secret ID
    SPOTIPY_CLIENT_ID = 'clientid'
    SPOTIPY_CLIENT_SECRET = 'clientsecret'

    token = util.prompt_for_user_token(username,scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,redirect_uri='http://yourdomain.com',cache_path='tokens.txt')
    sp = spotipy.Spotify(auth=token)

    # Playlist Data
    id = 'https://open.spotify.com/playlist/0000000000000000000000'
    results = sp.playlist(id)
    playlist_name = 'Your Playlist Title'
    playlist_description = 'Your playlist description'

    # Get the current time
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Check if the playlist has been reset
    if playlist_name != (results["name"]):
        
        # If it has changed, advance the counter
        f = open('counter.txt', "r")
        counter = f.readline()
        f.close()
        counter = int(counter)
        counter += int(1)
        counter = str(counter)
        g = open('counter.txt', "w")
        g.write(counter)
        g.close()
        
        # Restore the thumbnail, title & description
        with open("C:\\Users\\Username\\Documents\\spotify-playlist-updater\\Data\\thumbnail.jpg", "rb") as img_file:
         myimage = base64.b64encode(img_file.read())
        image_b64 = myimage
        sp.playlist_upload_cover_image(playlist_id=id, image_b64 = myimage)
        sp.user_playlist_change_details(username, id, name=playlist_name, description=playlist_description)
        
        # Show that the playlist was restored for the Xth time
        print(current_time, " - playlist restored x", counter)

    else:
        # If it hasn't changed, just show that the playlist was checked
        print(current_time, " - ok")


# Run the script every 1 minutes
while True:
    try:
        func()
        schedule.every(1).minutes.do(func)
    except:
        pass
    else:
        break

# Keep the script repeating indefinitely
while True:
    try:
        schedule.run_pending()
        time.sleep(30)
    except:
        pass


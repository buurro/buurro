import spotipy
import random
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    )
)

playlist_id = "552XL8oJY1VSZfPqFUnltY"
playlist = sp.playlist_tracks(playlist_id)["items"]

track = random.choice(playlist)["track"]

with open("template.md", "r") as f:
    template = f.read()

readme = template.format(
    track_artist=track["artists"][0]["name"],
    track_name=track["name"],
    track_url=track["href"],
)

with open("README.md", "w") as f:
    f.write(readme)

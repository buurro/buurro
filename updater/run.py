import spotipy
import random
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

PLAYLIST_ID = "552XL8oJY1VSZfPqFUnltY"

sp = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    )
)

playlist = sp.playlist_tracks(
    PLAYLIST_ID,
    fields="items(added_at, track(name, external_urls.spotify, artists.name))",
)["items"]

added_today = []
for i in playlist:
    added_at = datetime.strptime(i["added_at"], "%Y-%m-%dT%H:%M:%SZ")
    if datetime.utcnow() - added_at < timedelta(hours=2):
        added_today.append(i)

if added_today:
    track = random.choice(added_today)["track"]
else:
    track = random.choice(playlist)["track"]

artists = [a["name"] for a in track["artists"]]


with open("template.md", "r") as f:
    template = f.read()

readme = template.format(
    track_artists=", ".join(artists),
    track_name=track["name"],
    track_url=track["external_urls"]["spotify"],
)

with open("README.md", "w") as f:
    f.write(readme)

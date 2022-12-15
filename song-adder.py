import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = ["user-library-read", "playlist-modify-public"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
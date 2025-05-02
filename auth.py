import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize Spotify client with required scopes

def init_spotify_client(client_id: str, client_secret: str, redirect_uri: str, scope: str = "user-read-recently-played") -> spotipy.Spotify:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        )
    )
    return sp

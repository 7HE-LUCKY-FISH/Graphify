from typing import List
import spotipy

# Fetch user's recently played tracks and extract genres

def get_genre_sequence(
    sp: spotipy.Spotify,
    limit: int = 100
) -> List[str]:
    """
    Returns a chronological list of genres from the user's recently played tracks.
    """
    results = sp.current_user_recently_played(limit=limit)
    genre_sequence = []

    for item in reversed(results["items"]):  # oldest first
        track = item["track"]
        artist_id = track["artists"][0]["id"]
        artist = sp.artist(artist_id)
        genres = artist.get("genres", [])
        genre = genres[0] if genres else "unknown"
        genre_sequence.append(genre)

    return genre_sequence

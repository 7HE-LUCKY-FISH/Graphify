from auth import init_spotify_client
from data_fetch import get_genre_sequence
from model import build_chain, predict_next
from visualize import draw_chain
import random
import os
from dotenv import load_dotenv

def main():
    load_dotenv()  
    # Spotify API credentials
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI")

    # Initialize client
    sp = init_spotify_client(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI
    )

    # Fetch and build model
    sequence = get_genre_sequence(sp, limit=50)
    chain = build_chain(sequence)

    # Visualize
    draw_chain(chain, predicted_genre=next_genre, current_genre=current)

    current = sequence[-1] if sequence else random.choice(list(chain.keys()))
    next_genre = predict_next(current, chain)
    print(f"Last listened genre: {current}")
    print(f"Predicted next genre: {next_genre}")


if __name__ == "__main__":
    main()

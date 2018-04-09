import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def main():
    init()
    print("Welcome to SpotiFinder! Please select your method of finding sonngs")
    print("1. Playlist")
    print("2. Binary Search")

def init():
    print(sp.audio_features())


if __name__ == '__main__':
    main()

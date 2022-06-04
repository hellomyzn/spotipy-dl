import os
import sys

import spotipy


def setting():
    # get api data from environment environment variables
    client_id = os.environ["SPOTIPY_CLIENT_ID"]
    client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]

    client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spotify


def getIdByArtist(artist_name):
    results = spotify.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    artist = items[0]
    artist_id = artist["id"]
    return artist_id


def getIdByUrl(url):
    return url.split('/')[-1]


def getDiscographies(spotify, search_id: str, album_type: str):
    """
        Ref: https://spotipy.readthedocs.io/en/2.19.0/#spotipy.client.Spotify.artist_albums
            album_type
            - album
            - single
            - appears on
            - compilation
    """
    try:
        results = spotify.artist_albums(search_id, limit=50, album_type=album_type)
        album_datas = results['items']
        while results['next']:
            results = spotify.next(results)
            album_datas.extend(results['items'])
        for data in album_datas :
            print(data['external_urls']['spotify'])

    except IndexError:
        print("IndexError has occurred!")
    except AttributeError:
        print("AttributeError has occurred!")


if __name__ == '__main__':
    spotify = setting()
    args = sys.argv
    url = args[1]
    search_id = getIdByUrl(url)
    album_types = ['album', 'single']
    for album_type in album_types:
        getDiscographies(spotify, search_id, album_type)

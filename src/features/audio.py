import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from src import config

#ID CREDENTIALS
cid= config.API_KEYS['external_api']['spotify']['cid'] # API client ID
secret = config.API_KEYS['external_api']['spotify']['secret'] #Your API secret ID 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_audio_features(playlist_id):
    track_name = []
    artist_name = []
    tracks_ids = []

    #REQUEST PLAYLIST DETAILS FROM SPOTIFY API
    playlist = sp.playlist(playlist_id, fields=None, market=None)

    for i, t in enumerate (playlist['tracks']['items']):
        track_name.append(playlist['tracks']['items'][i]['track']['name'])
        tracks_ids.append(playlist['tracks']['items'][i]['track']['id'])
        artist_name.append(playlist['tracks']['items'][i]['track']['artists'][0]['name'])

    #REQUEST TRACK AUDIO FEATURES FROM SPOTIFT API
    track_features = sp.audio_features(tracks_ids)

    audio_sentiment=[]
    valence_score=[]

    #DEFINE SENTIMENT PER TRACK
    for i, t in enumerate(track_features):
        valence=track_features[i]['valence']
        valence_score.append(valence)
        if valence >= 0.5:
            sentiment= 'Positive'
        elif valence < 0.5:
            sentiment= 'Negative'
        audio_sentiment.append(sentiment)
        
    #CREATE DATAFRAME
    df=pd.DataFrame({'track_name': track_name, 'artist_name': artist_name, 'audio_valence_score' : valence_score, 'audio_sentiment': audio_sentiment})
    
    return df





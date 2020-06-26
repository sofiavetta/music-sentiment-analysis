from src.features.audio import get_audio_features
#from features.lyrics import get_lyrics_features
from src.features.lyrics import get_lyrics_features
import pandas as pd

def get_complete_data(playlist_id):
    audio_feature_df = get_audio_features(playlist_id) 
    lyrics_features_df = get_lyrics_features(audio_feature_df)
    df=pd.merge(audio_feature_df,lyrics_features_df,on='track_name')
    return df

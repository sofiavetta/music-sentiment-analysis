import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd

rcParams.update({'figure.autolayout': True})

def get_bar_plot(df):
    ax = df[['lyrics_sentiment_score','audio_valence_score']].plot(kind='bar', title ="VALENCE", figsize=(15, 10), legend=True, fontsize=12)
    ax.set_xticklabels(df['track_name'])
    ax.set_xlabel("Track", fontsize=12)
    ax.set_ylabel("Valence", fontsize=12)
    return ax

def get_pie_plot(audio_pos_count, lyrics_pos_count, len_df):
    audio_data = [audio_pos_count, len_df-audio_pos_count]
    lyrics_data = [lyrics_pos_count, len_df-lyrics_pos_count]

    audio_series = pd.Series(audio_data, index=("Positve", "Negative"))
    lyrics_series = pd.Series(lyrics_data, index=("Positive", "Negative"))

    audio_series.plot.pie(label="", title="AUDIO VALENCE")
    plt.show()
    lyrics_series.plot.pie(label="", title="LYRICS VALENCE")
    plt.show()
    

    #plot = df.plot(kind='pie', y='lyrics_sentiment', title = 'LYRICS VALENCE', figsize=(5, 5))
    #return plot


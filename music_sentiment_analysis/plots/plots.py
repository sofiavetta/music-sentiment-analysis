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

def get_pie_plot(df):
    figure, axes = plt.subplots(1, 2)
    df['audio_sentiment'].value_counts().plot(kind="pie",label="", title="AUDIO SENTIMENT", ax=axes[0])
    df['lyrics_sentiment'].value_counts().plot(kind="pie",label="", title="LYRICS SENTIMENT", ax=axes[1])
    plt.show()

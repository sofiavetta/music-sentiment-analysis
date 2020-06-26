import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from src import config

def sentiment_analyzer (lyrics):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score= analyzer.polarity_scores(lyrics)
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score['compound'] > -0.05 and sentiment_score['compound'] < 0.05:
        sentiment = 'Neutral'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'Negative'
    print(sentiment)
    return [sentiment_score['pos'], sentiment_score['compound'], sentiment]


def get_lyrics_features(audio_features_df):
    track_name = []
    sentiment_score = []
    sentiment = []
    for i in audio_features_df[['track_name', 'artist_name']].values:
        #track=i[0]
        if i[0].find('-'):
            track = i[0].split('-', maxsplit=1)[0]
        elif i[0].find('('):
            track = i[0].split('(', maxsplit=1)[0]
        print (track)
        track_name.append(i[0])
        artist=i[1]
        # GENIUS CREDENTIALS    
        base_url = 'https://api.genius.com'
        headers = {'Authorization': 'Bearer ' + config.API_KEYS['external_api']['genius']['access_token']}
        #SEARCH TRACK AND ARTIST
        search_url = base_url + '/search'
        data = {'q': track + ' ' + artist}
        response = requests.get(search_url, data=data, headers=headers)
        json = response.json()
        #CHECK IF IT IS A MATCH BETWEEN SPOTIFY AND GENIUS
        try:
            q_artist = json['response']['hits'][0]['result']['primary_artist']['name']
            if artist == q_artist:
                # GET LYRICS URL
                lyrics_url=json['response']['hits'][0]['result']['url']
                print(lyrics_url)
                # LOOK FOR LYRICS WITH WEB SCRAPING
                page = requests.get(lyrics_url)
                html = BeautifulSoup(page.text, 'html.parser')
                for div in html.findAll('div', class_= 'lyrics'):
                    lyrics = ' '.join(div.text.strip().split("\n"))
                #CALL THE SENTIMENT ANALYZER FUNCTION
                pos_score, score, sent = sentiment_analyzer(lyrics)
                sentiment.append(sent)
                sentiment_score.append(pos_score)
                #print(sentiment)
            else:
                sentiment.append(np.nan)
                sentiment_score.append(np.nan)
        except:
            sentiment.append(np.nan)
            sentiment_score.append(np.nan)

        #CREATE DATAFRAME
        df=pd.DataFrame({'track_name': track_name, 'lyrics_sentiment_score': sentiment_score, 'lyrics_sentiment':sentiment})

    return df






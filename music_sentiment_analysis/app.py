if __name__ == '__main__':
    run()

def run ():
    from music_sentiment_analysis.features.all_features import get_complete_data
    from music_sentiment_analysis.plots.plots import get_bar_plot, get_pie_plot
    import pandas as pd
    import matplotlib.pyplot as plt
    import time
    
    start_time=time.time()
    df = get_complete_data('37i9dQZF1DXdLtD0qszB1w') 
    pd.set_option('display.max_columns', None)

    def coincidence(df):
        count = 0
        for i in df[['audio_sentiment', 'lyrics_sentiment']].values:
            if i[0] == i[1]:
                count+=1
        coincidence_per = (count/len(df)*100)
        return coincidence_per

    def data_cleaning(df):
        #nan_count = df['lyrics_sentiment_score'].isnull().sum()
        df_clean = df.dropna()    
        return df_clean

    def valence(df_clean):
        lyrics_sentiment_count=0
        audio_sentiment_count=0
    
        for i in df[['audio_sentiment', 'lyrics_sentiment']].values:
            if i[0]=='Positive':
                audio_sentiment_count+=1
            if i[1]=='Positive':
                lyrics_sentiment_count+=1
        
        audio_valence_score_sum = 0
        lyrics_sentiment_score_sum = 0

        for i in df[['audio_valence_score', 'lyrics_sentiment_score']].values:
            audio_valence_score_sum+=i[0]
            lyrics_sentiment_score_sum+=i[1]
        
        avg_audio_positive= (audio_valence_score_sum/(len(df_clean)))*100
        avg_lyrics_positive= (lyrics_sentiment_score_sum/(len(df_clean)))*100
        audio_positive_per= (audio_sentiment_count/(len(df_clean)))*100
        lyrics_positive_per= (lyrics_sentiment_count/(len(df_clean)))*100

        return [avg_audio_positive, avg_lyrics_positive, audio_positive_per, lyrics_positive_per]

    #DATA CLEANING FUNCTION
    df_clean = data_cleaning(df)
    print (df_clean)

    #POSITIVENESS CALCULATOR FUNCTION
    audio_pos_avg, lyrics_pos_avg, audio_positive_per, lyrics_positive_per = valence(df_clean)

    #GRAPH BAR PLOT FROM PLOTS MODULE
    get_bar_plot(df)
    plt.show()

    #GRAPH PIE CHART FROM PLOTS MODULE
    get_pie_plot(df_clean)

    #PRINT RESULTS
    print (df_clean.describe())
    print ("TOTAL TRACKS ----->", len(df)) 
    print ("NaN COUNT ----->", len(df)-len(df_clean))
    print ("% OF COINCIDENCES BETWEEN LYRICS AND AUDIO SENTIMENTS -----> ", coincidence(df_clean))
    print ("% POSITIVE CLASSIFIED TRACKS (AUDIO) -----> ", audio_positive_per)
    print ("AVG VALENCE (AUDIO) ----->", audio_pos_avg)
    print ("% POSITIVE CLASSIFIED TRACKS (LYRICS) -----> ", lyrics_positive_per)
    print ("AVG VALENCE (LYRICS) ----->", lyrics_pos_avg)

    print ("PROCESSING TIME ----->" , (time.time() - start_time))
if __name__ == '__main__':
    run()

def run ():
    from music_sentiment_analysis.features.all_features import get_complete_data
    from music_sentiment_analysis.plots.plots import get_bar_plot, get_pie_plot
    import pandas as pd
    import matplotlib.pyplot as plt
    import time
    
    start_time=time.time()
    df = get_complete_data('165uXGnvfZuBUZLZnBiJsB') # El Estado Playlist
    #df = get_complete_data('3WCDdRaZZRLOEUEm6kd8Jx')
    pd.set_option('display.max_columns', None)

    def coincidence(df):
        count = 0
        for i in df[['audio_sentiment', 'lyrics_sentiment']].values:
            if i[0] == i[1]:
                count+=1
        coincidence_per = (count/len(df)*100)
        return coincidence_per

    def data_cleaning(df):
        nan_count = df['lyrics_sentiment_score'].isnull().sum()
        df_clean = df.dropna()    
        return [df_clean, nan_count]

    def valence(df):
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
        
        avg_audio_positive= (audio_valence_score_sum/(len(df)-nan_count))*100
        avg_lyrics_positive= (lyrics_sentiment_score_sum/(len(df)-nan_count))*100
        audio_positive_per= (audio_sentiment_count/(len(df)-nan_count))*100
        lyrics_positive_per= (lyrics_sentiment_count/(len(df)-nan_count))*100

        return [avg_audio_positive, avg_lyrics_positive, audio_sentiment_count, lyrics_sentiment_count]

    #DATA CLEANING FUNCTION
    df_clean, nan_count = data_cleaning(df)

    #POSITIVENESS CALCULATOR FUNCTION
    audio_pos_avg, lyrics_pos_avg, audio_pos_count, lyrics_pos_count = valence(df_clean)

    #GRAPH BAR PLOT FROM PLOTS MODULE
    get_bar_plot(df_clean)
    plt.show()

    #GRAPH PIE CHART FROM PLOTS MODULE
    get_pie_plot(audio_pos_count, lyrics_pos_count, len(df))
    plt.show()

    #PRINT RESULTS
    print (df_clean.describe())
    print ("TOTAL TRACKS ----->", len(df)) 
    print ("NaN COUNT ----->", nan_count)
    print ("% OF COINCIDENCES -----> ", coincidence(df_clean))
    print ("% POSITIVE TRACKS (AUDIO) -----> ", audio_pos_count/len(df_clean)*100)
    print ("AVG VALENCE (AUDIO) ----->", audio_pos_avg)
    print ("% POSITIVE TRACKS (LYRICS) -----> ", lyrics_pos_count/len(df_clean)*100)
    print ("AVG VALENCE (LYRICS) ----->", lyrics_pos_avg)

    print ("PROCESSING TIME ----->" , (time.time() - start_time))
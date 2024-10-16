import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def plot_content_type_distribution(df):
    return px.pie(df, names='type', title='Content Type Distribution')

def plot_top_countries(df):
    top_countries = df['country'].value_counts().head(10)
    return px.bar(top_countries, x=top_countries.index, y=top_countries.values, title='Top 10 Countries Producing Content')

def plot_rating_distribution(df):
    return px.bar(df['rating'].value_counts(), title='Rating Distribution')

def plot_content_trends(df):
    content_trends = df.groupby(df['date_added'].dt.year)['show_id'].count().reset_index()
    return px.line(content_trends, x='date_added', y='show_id', title='Yearly Content Addition Trends')

def plot_top_genres(df):
    genres = df['listed_in'].str.split(', ').explode()
    top_genres = genres.value_counts().head(10)
    return px.bar(top_genres, x=top_genres.index, y=top_genres.values, title='Top 10 Genres')

def plot_movie_duration_distribution(df):
    movie_durations = df[(df['type'] == 'Movie') & (df['duration'] != 'missing')]['duration'].str.replace(' min', '').astype(int)
    return px.histogram(movie_durations, title='Movie Duration Distribution')

def plot_tv_show_season_distribution(df):
    tv_show_durations = df[(df['type'] == 'TV Show') & (df['duration'] != 'missing')]['duration'].apply(lambda x: '6+ seasons' if int(x.split(' ')[0]) >= 6 else x)
    return px.pie(tv_show_durations.value_counts(), values=tv_show_durations.value_counts().values, names=tv_show_durations.value_counts().index, title='TV Show Season Distribution')

def generate_wordcloud(df):
    text = ' '.join(df['description'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    return fig
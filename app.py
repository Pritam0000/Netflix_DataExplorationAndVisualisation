# app.py
import streamlit as st
from data_loader import load_data
from visualizations import (
    plot_content_type_distribution,
    plot_top_countries,
    plot_rating_distribution,
    plot_content_trends,
    plot_top_genres,
    plot_movie_duration_distribution,
    plot_tv_show_season_distribution,
    generate_wordcloud
)
from utils import filter_data

st.set_page_config(page_title="Netflix Content Analysis", layout="wide")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header('Filters')
content_type = st.sidebar.multiselect('Select Content Type', options=df['type'].unique(), default=df['type'].unique())
selected_years = st.sidebar.slider('Select Year Range', min_value=int(df['release_year'].min()), max_value=int(df['release_year'].max()), value=(int(df['release_year'].min()), int(df['release_year'].max())))

# Filter data
filtered_df = filter_data(df, content_type, selected_years)

# Main content
st.title('Netflix Content Analysis Dashboard')

st.header('Content Overview')
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_content_type_distribution(filtered_df), use_container_width=True)
    st.plotly_chart(plot_rating_distribution(filtered_df), use_container_width=True)
with col2:
    st.plotly_chart(plot_top_countries(filtered_df), use_container_width=True)
    st.plotly_chart(plot_top_genres(filtered_df), use_container_width=True)

st.plotly_chart(plot_content_trends(filtered_df), use_container_width=True)

st.header('Duration Analysis')
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_movie_duration_distribution(filtered_df), use_container_width=True)
with col2:
    st.plotly_chart(plot_tv_show_season_distribution(filtered_df), use_container_width=True)

st.header('Content Description Word Cloud')
st.pyplot(generate_wordcloud(filtered_df))

st.header('Data Explorer')
st.dataframe(filtered_df)


# data_loader.py
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv('netflix.csv')
    
    # Replace missing values with 'missing'
    columns_to_fill = df.columns[df.isnull().any()].tolist()
    df[columns_to_fill] = df[columns_to_fill].fillna('missing')
    
    # Replace incorrect rating values with 'UR'
    df['rating'] = np.where(np.isin(df['rating'], ['74 min', '84 min', '66 min', 'missing']), 'UR', df['rating'])
    
    # Convert date_added to datetime
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    
    return df

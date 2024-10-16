def filter_data(df, content_type, year_range):
    return df[(df['type'].isin(content_type)) & (df['release_year'].between(year_range[0], year_range[1]))]

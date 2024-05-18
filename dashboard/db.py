import pandas as pd
from config import POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_HOST, POSTGRES_USER

DB_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def read_data():
    query = "SELECT * FROM analytics_log"
    df = pd.read_sql(query, DB_URI)
    df['hour'] = df['hour'].apply(format_time)
    dfs = []
    for action in df['action_name'].unique():
        dfs.append(df.loc[df['action_name'] == action, :])
    print(dfs)
    return df


def format_date(date):
    return date.strftime('%Y-%m-%d')


def format_time(date):
    return date.strftime('%Y-%m-%d %H')

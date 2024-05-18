import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from db import read_data
import plotly.express as px

df_an = read_data()

app = dash.Dash(__name__)

timeline = px.line(df_an, x="hour", y="cnt", title='Динамика действий бота')
df = df_an.copy()

fig = px.pie(df, values='pop', names='country', title='Распределение действий бота')

app.layout = html.Div([
    html.H1("Продажи за последние месяцы"),
    dcc.Graph(figure=timeline),
])

if __name__ == '__main__':
    app.run_server(debug=True)

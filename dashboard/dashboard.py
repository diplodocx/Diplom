import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from db import read_distibution, read_dynamic
import plotly.express as px

dfs = read_dynamic()
df = read_distibution()

app = dash.Dash(__name__)

timeline_1 = px.line(dfs[0].sort_values('hour'), x="hour", y="cnt", title='Динамика действий бота, двигатель')
timeline_2 = px.line(dfs[1].sort_values('hour'), x="hour", y="cnt", title='Динамика действий бота, лампочки')
pie = px.pie(df, values='cnt', names='action_name', title='Распределение действий бота')

app.layout = html.Div([
    html.H1("Действия бота"),
    dcc.Graph(figure=timeline_1),
    dcc.Graph(figure=timeline_2),
    dcc.Graph(figure=pie)
])

if __name__ == '__main__':
    app.run_server(debug=True)

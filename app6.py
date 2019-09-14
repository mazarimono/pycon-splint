import dash
import dash_core_components as dcc
import dash_html_components as html 
import pandas as pd

df = pd.read_csv("sleep_prefectures.csv")

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(figure={
        "data": [{"x": df["都道府県"], "y":df["2016"], "type":"bar"}]
    })
])

app.run_server(debug=True)
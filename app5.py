import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv("dogFrame.csv")
df = df[df["temp"]=="12月"]


app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(figure={
        "data": [{"x": df["year"], "y": df["temp"]}]
    })
])

app.run_server(debug=True)

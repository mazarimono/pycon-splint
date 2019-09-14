import dash
import dash_core_components as dcc
import dash_html_components as html 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("sleep_prefectures.csv")

app = dash.Dash()

app.layout = html.Div([
    html.H1(id="graphtitle", style={"textAlign":"center"}),
    dcc.Dropdown(id="pickdrop", options=[{"label": i, "value": i} 
    for i in df.columns[-3:]],
    value = df.columns[-3]
    ),
    dcc.Graph(id="graph-output")
])

@app.callback(dash.dependencies.Output("graph-output", "figure"),
        [dash.dependencies.Input("pickdrop", "value")])
def make_graph(value):
    return {"data": [go.Bar(x=df["都道府県"], y=df[value]/60)]}

@app.callback(dash.dependencies.Output("graphtitle", "children"),
            [dash.dependencies.Input("pickdrop", "value")])
def make_title(value):
    return "{}年の都道府県別睡眠時間".format(value)



app.run_server(debug=True)
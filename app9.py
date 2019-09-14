import json

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
    html.Div([
    dcc.Dropdown(id="pickdrop", options=[{"label": i, "value": i} 
    for i in df.columns[-3:]],
    value = df.columns[-3]
    )], style={"width": "50%", "margin": "auto"}),
    dcc.Graph(id="graph-output",
    hoverData={"points":[{"x": "東京都"}]}),
    html.H1(id="showdata"),
    html.Div([
    dcc.Graph(id="graph-output2")], style={"width": "50%", "margin": "auto"})
])

@app.callback(dash.dependencies.Output("graph-output", "figure"),
        [dash.dependencies.Input("pickdrop", "value")])
def make_graph(value):
    return {"data": [go.Bar(x=df["都道府県"], y=df[value]/60)]}

@app.callback(dash.dependencies.Output("graphtitle", "children"),
            [dash.dependencies.Input("pickdrop", "value")])
def make_title(value):
    return "{}年の都道府県別睡眠時間".format(value)

@app.callback([dash.dependencies.Output("showdata", "children"),
            dash.dependencies.Output("graph-output2", "figure")],
            [dash.dependencies.Input("graph-output", "hoverData")])
def return_data(hoverData):
    if hoverData != None:
        kenmei = hoverData["points"][0]["x"]
        df1 = df[df["都道府県"] == kenmei]
        df2 = pd.concat([df1.iloc[:, 0], df1.iloc[:, -3:]], axis=1)
        df3 = pd.melt(df2, id_vars="都道府県")
        return kenmei,px.line(df3, x="variable", y="value")



app.run_server(debug=True)

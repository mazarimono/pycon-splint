import dash
import dash_core_components as dcc 
import dash_html_components as html 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)

app.layout = html.Div(id="first", children=[
    html.H1(id="second", children=["Hello Dash"], style={"textAlign": "center"}),
    dcc.Graph(id="third", figure={"data":[
        {"x":[1,2,3,4], "y":[4,3,2,1], "name":"Tokyo", "type":"bar"},
        {"x":[1,2,3,4], "y": [5,3,4,1], "name": "Kyoto", "type":"bar"}
    ],
    "layout":{"title": "dash_application"}
    })
], style={"width":"80%", "margin":"auto"})

app.run_server(debug=True)


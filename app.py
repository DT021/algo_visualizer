import dash
import dash_core_components as dcc
import dash_html_components as html
import time
import visualizer as vs
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(className="main", children=[
  html.H1('Really slow sorts'),
  html.A('Refresh', href='/'),
  dcc.Graph(id='graph1', figure=vs.plotlyMS()),
  dcc.Graph(id='graph2', figure=vs.plotlyBasicSorts("Selection sort")),
  dcc.Graph(id='graph3', figure=vs.plotlyBasicSorts("Insertion sort")),
  dcc.Graph(id='graph4', figure= vs.plotlyBasicSorts("Bubble sort")),
])

if __name__ == "__main__":
  app.run_server(debug=True)
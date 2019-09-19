import dash
import dash_core_components as dcc
import dash_html_components as html
import time
import visualizer as vs
from dash.dependencies import Input, Output, State

app = dash.Dash()
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
  dcc.Graph(id='graph1', figure=vs.plotlyMS()),
  dcc.Graph(id='graph2', figure=vs.plotlyBasicSorts("Selection sort")),
  dcc.Graph(id='graph3', figure=vs.plotlyBasicSorts("Insertion sort")),
  dcc.Graph(id='graph4', figure= vs.plotlyBasicSorts("Bubble sort")),
  
  # dcc.Dropdown(
  #       id='dropdown',
  #       options=[
  #         {'label': 'Merge Sort', 'value': 'sort_1'},
  #         {'label': 'Selection Sort', 'value': 'sort_2'},
  #         {'label': 'Insertion Sort', 'value': 'sort_3'},
  #         {'label': 'Bubble Sort', 'value': 'sort_4'},
  #       ],
  #       value='sort_1'
  #   ),
  # dcc.Loading(id="loading-1", children=[dcc.Graph(id='graph')], type="default"),
])

# @app.callback(Output("loading-1", "children"), [Input("dropdown", "value")])
# def input_triggers_spinner(selected_value):
#   if selected_value == 'sort_1':
#     return dcc.Graph(id='graph', figure=vs.plotlyMS())
#   elif selected_value == 'sort_2':
#     return dcc.Graph(id='graph', figure= vs.plotlyBasicSorts("Selection sort"))
#   elif selected_value == 'sort_3':
#     return dcc.Graph(id='graph', figure= vs.plotlyBasicSorts("Insertion sort"))
#   elif selected_value == 'sort_4':
#     return dcc.Graph(id='graph', figure= vs.plotlyBasicSorts("Bubble sort"))
#   else:
#     return dcc.Graph(id='graph', figure=vs.plotlyMS())

if __name__ == "__main__":
  app.run_server(debug=False)
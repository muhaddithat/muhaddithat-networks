# via https://dash.plotly.com/layout

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# https://dash.plotly.com/cytoscape/events : examples on making lists of nodes/edges via loop
nodes = [
            {'data': {'id': '53', 'label': 'Aisha bint Abi Bakr'}}, 
            {'data': {'id': '56', 'label': 'Umm Salamah'}},
            {'data': {'id': '10737', 'label': 'Khayra Umm al-Hasan al-\'Abbassri'}},
            {'data': {'id': '11734', 'label': 'Hind bint al-Harith al-Farasiyya '}},
            {'data': {'id': '54', 'label': 'Hafsa bint Umar'}},
            {'data': {'id': '1181', 'label': 'Safiyya bint Abi \'Ubaid al-Thaqafi'}},
            {'data': {'id': '1293', 'label': 'Umm Mubashir al-Ansariyya'}},
        ]

edges = [
            {'data': {'source': '56', 'target': '10737'}},
            {'data': {'source': '56', 'target': '11734'}},
            {'data': {'source': '54', 'target': '1181'}},
            {'data': {'source': '54', 'target': '1293'}},
        ]

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': '#8e4bd1',
            'label': 'data(label)'
        }
    },
    {
        'selector': 'edge',
        'style': {
            'line-color': '#cc99ff'
        }
    }
]

app.layout = html.Div([
    html.P("Dash Cytoscape:"),
    cyto.Cytoscape(
        #id='cytoscape',
        id='cytoscape-event-callbacks-3',
        elements= edges + nodes,
        layout={'name': 'breadthfirst'},
        style={'width': '100%', 'height': '500px'},
        stylesheet=default_stylesheet
    ),
    dcc.Markdown(id='cytoscape-selectedNodeData-markdown')
])

@app.callback(Output('cytoscape-selectedNodeData-markdown', 'children'),
              Input('cytoscape-event-callbacks-3', 'selectedNodeData'))
def displaySelectedNodeData(data_list):
    if data_list is None:
        return "No narrator selected."

    narrators_list = [data['label'] for data in data_list]
    return "You selected the following narrators: " + "\n* ".join(narrators_list)


if __name__ == '__main__':
    app.run_server(debug=True)
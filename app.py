# via https://dash.plotly.com/layout

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Dash Cytoscape:"),
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            {'data': {'id': '53', 'label': 'Aisha bint Abi Bakr'}}, 
            {'data': {'id': '56', 'label': 'Umm Salamah'}},
            {'data': {'id': '10737', 'label': 'Khayra Umm al-Hasan al-\'Abbassri'}},
            {'data': {'id': '11734', 'label': 'Hind bint al-Harith al-Farasiyya '}},
            {'data': {'id': '54', 'label': 'Hafsa bint Umar'}},
            {'data': {'id': '1181', 'label': 'Safiyya bint Abi \'Ubaid al-Thaqafi'}},
            {'data': {'id': '1293', 'label': 'Umm Mubashir al-Ansariyya'}},
            {'data': {'source': '56', 'target': '10737'}},
            {'data': {'source': '56', 'target': '11734'}},
            {'data': {'source': '54', 'target': '1181'}},
            {'data': {'source': '54', 'target': '1293'}},
        ],
        layout={'name': 'breadthfirst'},
        style={'width': '100%', 'height': '500px'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
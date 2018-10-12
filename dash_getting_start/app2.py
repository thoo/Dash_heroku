import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app=dash.Dash()

app.layout=html.Div([
    dcc.Input(id='my-id',value="initial value",type='text'),
    html.Div(id='my-div')
    ])

@app.callback(
    Output(component_id='my-div',component_property='children'),
    [Input(component_id='my-id',component_property='value')]
    )

def update_output_div(input_val):
    return 'You\'ve entered {}'.format(input_val)

if __name__=='__main__':
    app.run_server(port=8051,debug=True)
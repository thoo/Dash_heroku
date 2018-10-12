import datetime

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

my_hr_style={
                #'border-width' : '4px',
                'border-top': '2px solid #21ABCD',
                'margin-top': '0.5rem',
                'margin-bottom': '0.5rem'
            }
app = dash.Dash()

app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.H2(
        children='Facial Expression Recognition',
        style={
            'textAlign': 'center',
            'color': 'black',
            'margin-top': '1.0rem',
            'margin-bottom': '1.0rem'
        }
    ),
    #html.Hr(),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A(' Select A Image')
        ]),
        style={
            'width': '40%',
            'height': '40px',
            'lineHeight': '40px',
            'borderWidth': '3px',
            'borderStyle': 'solid',
            'borderRadius': '50px',
            'borderColor': '#007FFF',
            #'backgroundColor':'rgb(242, 242, 242)',
            'textAlign': 'center',
            
            #'marginLeft':'10px',
            
            'margin': 'auto'
            #'padding': '10px 100px 10px 200px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Hr(
            style=my_hr_style
    ),
    html.Div(id='output-image-upload'),
])


def parse_contents(contents, filename):
    return html.Div([
        html.H5(filename),
        #html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents),
        html.Hr(style=my_hr_style),
        #html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #     'whiteSpace': 'pre-wrap',
        #     'wordBreak': 'break-all'
        # })
    ])


@app.callback(Output('output-image-upload', 'children'),
              [Input('upload-image', 'contents'),
               Input('upload-image', 'filename')])
               #Input('upload-image', 'last_modified')])
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [ parse_contents(c, n) for c, n in 
            zip(list_of_contents, list_of_names)]
        return children


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
import datetime

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import openface as opf
import dlib
from skimage.color import rgb2gray

import base64
from skimage import io

dlib_fun=opf.AlignDlib('./lib/dlib_model/shape_predictor_68_face_landmarks.dat')
my_hr_style={
                #'border-width' : '4px',
                'border-top': '2px solid #21ABCD',
                'margin-top': '0.5rem',
                'margin-bottom': '0.5rem',
                'margin-left': 'auto',
                'margin-right': 'auto'
            }
h5_style = {
            'textAlign': 'center',
            'color': 'black',
            'margin-top': '1.0rem',
            'margin-bottom': '1.0rem'
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

def get_face(contents):
    if contents.startswith('data:image/jpeg;base64,'):
        contents=contents[len('data:image/jpeg;base64,'):]
    imgdata = base64.b64decode(contents)
    arr = np.frombuffer(imgdata,np.uint8)
    #arr = io.imread(imgdata,plugin='imageio')
    # arr = base64.decodestring(contents.encode('ascii'))
    # arr = np.frombuffer(arr, dtype = np.float)
    return arr

def arrtobase64(arr):
    return 'data:image/png;base64,{}'.format(base64.encodestring(arr).decode('utf-8'))

def layout_plot(list_images):
    layout_img = []
    for image in list_images:
        layout_img.extend([
           html.Img(src=image, style={ 'margin' : 'auto', 'display': 'block'}),
           html.Hr(style=my_hr_style),
        ])
    return layout_img

def parse_contents(contents, filename):

    test = get_face(contents)
    encoded_img = arrtobase64(test)
    import pdb;pdb.set_trace()
    return html.Div([
        html.Div([
            html.H5(filename, style= h5_style),
        #html.H6(datetime.datetime.fromtimestamp(date)),
        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
            html.Img(src=contents, style = { 'margin' : 'auto', 'display': 'block'}),
            html.Hr(style=my_hr_style),
            ]),
        html.Div([
            html.Div(
                layout_plot([encoded_img]),
            # html.Img(src=encoded_img, style={ 'margin' : 'auto', 'display': 'block'}),
            # html.Hr(style=my_hr_style),
        #html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #     'whiteSpace': 'pre-wrap',
        #     'wordBreak': 'break-all'
        # })
                className="six columns"),
            html.Div(
                layout_plot([contents]),
                className="six columns"),
        ],className="row")
        #
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
    app.run_server(debug=True, port=8819)

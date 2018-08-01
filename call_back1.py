import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input,Output

app= dash.Dash()

app.layout=html.Div([
	dcc.RadioItems(
		id='dropdown-a',
		options=[{'label':i,'value':i} for i in ['Canada','USA','Mexico']],
		value='Canada'),
	html.Div(id='output-a'),
		dcc.RadioItems(
			id='dropdown-b',
			options=[{'label':i , 'value':i} for i in ['MTL','NYC','SF']],
			value='MTL'),
		html.Div(id='output-b')
	])

@app.callback(
	Output('output-a','children'),
	[Input('dropdown-a','value')])

def callback_a(dropdown_a):
	return 'You\'ve selected "{}"'.format(dropdown_a)

@app.callback(
	Output('output-b','children'),
	[Input('dropdown-b','value')])

def callback_b(dropdown_b):
	return 'You\'ve selected "{}"'.format(dropdown_b)

if __name__ == '__main__':
	app.run_server(debug=True,port=8888)
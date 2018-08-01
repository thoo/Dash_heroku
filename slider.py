import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import pandas as pd 
import plotly.graph_objs as go 

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash()

app.layout=html.Div([
	dcc.Graph(style={'width':'1200px'}	,
		id='graph_with_slider'),
	html.Div(
		dcc.Slider(
		id='year_slider',
		min=df['year'].min(),
		max=df['year'].max(),
		value=df['year'].min(),
		step=None,
		marks={str(year):str(year) for year in df['year'].unique()}
	),
		style={'width':'80%','padding': '10px 0px 10px 50px'}
		)
	])


@app.callback(
	Output('graph_with_slider','figure'),
	[Input('year_slider','value')])
def update_figure(selected_year):
	filtered_df=df[df.year == selected_year]
	traces=[]
	for i in filtered_df.continent.unique():
		df_by_continent=filtered_df[filtered_df.continent == i]
		traces.append(go.Scatter(
			x=df_by_continent['gdpPercap'],
			y=df_by_continent['lifeExp'],
			text=df_by_continent['country'],
			mode='markers',
			opacity=0.7,
			marker={
			'size':15,
			'line': {'width':0.5,'color':'white'}
			},
			name=i 
		))

	return {
		'data':traces,
		'layout':go.Layout(
			xaxis={'type':'log','title':'GDP Per Capita'},
			yaxis={'title':'Life Expetancy','range':[20,90]},
			margin={'l': 100, 'b': 40, 't': 10, 'r': 100},
			legend={'x':0,'y':1},
			hovermode='closest'
		)
	}

if __name__ == '__main__':
	app.run_server(port=8051,debug=True)
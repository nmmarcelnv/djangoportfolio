import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

from . import SIRmodel

app = dash.Dash()
server = app.server


available_indicators = np.arange(0, 1, 0.05)
app.layout = html.Div([
    html.Div([

	#html div element
        html.Div([
            dcc.Dropdown(
                id='S0',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value=0.9999
            ),
            dcc.RadioItems(
                id='S0-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

	#another html div element
        html.Div([
            dcc.Dropdown(
                id='I0',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value=0.0001
            ),
            dcc.RadioItems(
                id='I0-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    html.Div([
    	dcc.Slider(
        	id='beta--slider',
        	min=0,
        	max=2,
        	value=1.4,
        	step=0.01,
        	marks={beta: str(beta) for beta in [0, 0.5, 1.0, 1.5, 2.0]}
    	) ],
	style={'width': '20%', 'display': 'inline-block'} ),

	html.Div([
    	dcc.Slider(
        	id='gamma--slider',
        	min=0,
        	max=1,
        	value=0.1,
        	step=0.01,
        	marks={gamma: str(gamma) for gamma in [0, 0.25, 0.50, 0.75, 1.0]}
    	) ],
	style={'width': '20%', 'display': 'inline-block'}),

])

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('S0', 'value'),
     dash.dependencies.Input('S0-type', 'value'),
     dash.dependencies.Input('I0', 'value'),
     dash.dependencies.Input('I0-type', 'value'),
     dash.dependencies.Input('beta--slider', 'value'),
     dash.dependencies.Input('gamma--slider', 'value')])
def update_graph(S0, S0type, I0, I0type,
                 beta, gamma):

    dff = SIRmodel.solve_model(model = SIRmodel.epidemic_model, 
		initial_conditions = (S0, I0, 0.0) , 
		parameters = (beta, gamma) )
    
    data = [
	go.Scatter(
		x = dff.index,
		y = dff[column_name],
		text = column_name,
		mode='markers',
		marker={
			'size': 15,
			'opacity': 0.5,
			'line': {'width': 0.5, 'color': 'white'}
		}
         ) for column_name in dff.columns 
    ]

    return {
        'data': data,
        'layout': go.Layout(
            xaxis={
                'title': 'Time',
                'type': 'linear' if S0type == 'Linear' else 'log'
            },
            yaxis={
                'title': 'Proportions',
                'type': 'linear' if I0type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
if __name__ == '__main__':
    app.run_server()

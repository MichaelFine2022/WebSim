import pandas as pd
import dash
import datetime
from dash import dcc, html, Input, Output, State
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import dash_bootstrap_components as dbc

def displayMessage(record_address):
    global CAPITAL
    with open(str(record_address),"a") as file:
        file.write("CURRENT FUNDS: " + str(CAPITAL) + "\n")
        
# Load and reverse the data
data = pd.read_csv('HistoricalData.csv')

data = data[::-1]
CAPITAL = 100000
# Prepare the data for display
data.columns = data.columns.str.strip()
data['Date'] = pd.to_datetime(data['Date'])
data['Open'] = data['Open'].str.replace('$', '').astype(float)
data['Close/Last'] = data['Close/Last'].str.replace('$', '').astype(float)
data['High'] = data['High'].str.replace('$', '').astype(float)
data['Low'] = data['Low'].str.replace('$', '').astype(float)

print(data)

with open('ledger.txt', 'w') as ledger:
    ledger.write("LEDGER INITIALIZED: " + str(datetime.datetime.now()) + "\n")
    displayMessage('ledger.txt')

    

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    html.H4('Stock candlestick chart'),
    dcc.Checklist(
        id='toggle-rangeslider',
        options=[{'label': 'Include Rangeslider', 
                  'value': 'slider'}],
        value=['slider']
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("toggle-rangeslider", "value"))
def display_candlestick(value):
    #controls how many graphs are displayed
    fig = make_subplots(rows = 2, cols = 1, shared_xaxes=True)
    #adds the main candlestick graph
    fig.add_trace(go.Candlestick(
        x=data.Date,
        open=data.Open,
        high=data.High,
        low=data.Low,
        close=data['Close/Last'],
        opacity=0.25,
        name="Graphed Stock"),
        row=1,
        col=1)
    #adds entry and exit markers
    """
    fig.add_trace(go.Scatter(
        x=
        y=
        mode="markers"
        marker_symbol="triangle-up",
        marker_size=13
        marker_line_color= "rgb(0,255,0)",
        name="Entries"
    ), row=1,col=1)
    fig.add_trace(go.Scatter(
        x=
        y=
        mode="markers"
        marker_symbol="triangle-down",
        marker_size=13
        marker_line_color= "rgb(255,0,0)",
        name="Exits"
    ), row=1,col=1)
    """
    #adds a volume indicator
    fig.add_trace(go.Scatter(
        x=data.Date,
        y=data.Volume,
        name="Volume"),
        row=2,
        col=1)

    fig.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    return fig
if __name__ == '__main__':
    app.run_server(debug=True)

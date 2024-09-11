import plotly.graph_objects as go
from datetime import datetime

# Sample data for the candlestick chart
open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
dates = [datetime(year=2013, month=10, day=10),
         datetime(year=2013, month=11, day=10),
         datetime(year=2013, month=12, day=10),
         datetime(year=2014, month=1, day=10),
         datetime(year=2014, month=2, day=10)]

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=dates,
    open=open_data,
    high=high_data,
    low=low_data,
    close=close_data
)])

# Add annotations to the chart
fig.add_annotation(
    x=dates[0],         # x-coordinate of the annotation
    y=open_data[0],     # y-coordinate of the annotation
    text="Start",       # Text of the annotation
    showarrow=True,     # Whether to show an arrow pointing to the annotation
    arrowhead=2,        # Style of the arrowhead
    ax=0,               # x-offset of the annotation text
    ay=-40              # y-offset of the annotation text
)

fig.add_annotation(
    x=dates[4],         # x-coordinate of the annotation
    y=close_data[4],    # y-coordinate of the annotation
    text="End",         # Text of the annotation
    showarrow=True,     # Whether to show an arrow pointing to the annotation
    arrowhead=2,        # Style of the arrowhead
    ax=0,               # x-offset of the annotation text
    ay=-40              # y-offset of the annotation text
)

fig.add_annotation(
    x=dates[2],         # x-coordinate of the annotation
    y=high_data[2],     # y-coordinate of the annotation
    text="Peak",        # Text of the annotation
    showarrow=True,     # Whether to show an arrow pointing to the annotation
    arrowhead=2,        # Style of the arrowhead
    ax=0,               # x-offset of the annotation text
    ay=-40              # y-offset of the annotation text
)

# Display the chart with annotations
fig.show()

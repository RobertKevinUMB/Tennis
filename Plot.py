import pandas as pd
import plotly as px
import matplotlib as plt
import plotly.graph_objects as go
def plot_graph():
    first_csv = pd.read_csv("csv1.csv")
    second_csv = pd.read_csv("csv2.csv")


    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = first_csv['x'],
            y=  first_csv['y'],

                marker=dict(
                color='green',
                size=15)
        )
    )
    fig.add_trace(
        go.Scatter(
            x = second_csv['x'],
            y=  second_csv['y'],

                marker=dict(
                color='green',
                size=15)
        )
    )
    fig.add_trace(
        go.Scatter(
            x = [0,23.77],
            y = [0,0],
            
        )
    )
    fig.add_shape(type= "line",
        x0 = 11.885, y0 = 0, x1 = 11.885, y1 = .992,
        line = dict (color = "RoyalBlue", width = 3)
    
    )
    fig.update_layout(
    margin=dict(l=1, r=1, t=1, b=1),
    paper_bgcolor="LightSteelBlue",
    )
    fig.add_shape(type= "line",
    x0 = 18.285, y0 = -.05, x1 = 18.285, y1 = .05,
    line = dict (color = "RoyalBlue", width = 3)
    )
    fig.show()
    fig.update(layout_showlegend=False)
    return plot_graph
plot_graph()
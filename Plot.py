import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg
from pandastable import Table
from tkintertable import TableCanvas
import pandas as pd
import plotly as px
import matplotlib as plt
import plotly.graph_objects as go
root = tk.Tk()
root.title("Comapre CSV's")
canvas1 = tk.Canvas(root, width = 1920, height = 1080, relief='raised')
canvas1.pack()
def plot_graph():
    tk.file_name1 = filedialog.askopenfilename(initialdir = '/Desktop',
    title = 'Select a CSV file',
    filetypes = (('csv file','*.csv'),
    ('csv file','*.csv')))           
    first_csv= pd.read_csv(tk.file_name1)
    tk.file_name2 = filedialog.askopenfilename(initialdir = '/Desktop',
    title = 'Select a CSV file',
    filetypes = (('csv file','*.csv'),
    ('csv file','*.csv')))           
    second_csv = pd.read_csv(tk.file_name2)


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
button1 = tk.Button(text='Upload the two files you want to compare', command=plot_graph, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(750,280, window=button1)
root.mainloop()

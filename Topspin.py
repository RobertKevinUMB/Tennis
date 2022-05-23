import tkinter as tk
import pandas as pd
import matplotlib as plt
import plotly as px
import plotly.graph_objects as go
from webbrowser import get
from Topspincal import top_Spin
root= tk.Tk()
root.title("TopSpin")
canvas1 = tk.Canvas(root, width = 1920, height = 1080, relief='raised')
canvas1.pack()
x0 = tk.StringVar()
y0 = tk.StringVar()
Velocity = tk.StringVar()
Theta = tk.StringVar()
Rpm = tk.StringVar()
Res = tk.StringVar()
DeltaT = tk.StringVar()
entry1 = tk.Entry (root,textvariable=x0) 
canvas1.create_window(100, 140, window=entry1)
label1 = tk.Label(root, text='Enter the Inititial ball location(x0)')
label1.config(font=('helvetica', 10))
canvas1.create_window(100, 180, window=label1)
entry2 = tk.Entry (root,textvariable=y0)
canvas1.create_window(300, 140, window=entry2)
label2 = tk.Label(root, text='Enter the Inititial ball location(y0)')
label2.config(font=('helvetica', 10))
canvas1.create_window(300, 180, window=label2)
entry3 = tk.Entry (root,textvariable=Velocity)
canvas1.create_window(500, 140, window=entry3)
label3 = tk.Label(root, text='Enter the Inititial velocity')
label3.config(font=('helvetica', 10))
canvas1.create_window(500, 180, window=label3)
entry4 = tk.Entry (root,textvariable=Theta)
canvas1.create_window(700, 140, window=entry4)
label4 = tk.Label(root, text='Enter the Inititial angle')
label4.config(font=('helvetica', 10))
canvas1.create_window(700, 180, window=label4)
entry5 = tk.Entry (root,textvariable=Rpm) 
canvas1.create_window(900, 140, window=entry5)
label5 = tk.Label(root, text='Enter the Inititial rate of spin in rpm')
label5.config(font=('helvetica', 10))
canvas1.create_window(900, 180, window=label5)
entry6 = tk.Entry (root,textvariable=Res)
canvas1.create_window(1100, 140, window=entry6)
label6 = tk.Label(root, text='Enter the Restitution Coefficient')
label6.config(font=('helvetica', 10))
canvas1.create_window(1100, 180, window=label6)
entry7 = tk.Entry (root,textvariable=DeltaT)
canvas1.create_window(1300, 140, window=entry7)
label7 = tk.Label(root, text='Enter the Delta T in seconds')
label7.config(font=('helvetica', 10))
canvas1.create_window(1300, 180, window=label7)
def pltgrp():
    first_csv = pd.read_csv("topspindata.csv")
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = first_csv['x'],
            y=  first_csv['y'],

                marker=dict(color='green',
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
    fig.add_shape(type= "line",
        x0 = 5.485, y0 = -.05, x1 = 5.484, y1 = .05,
        line = dict (color = "RoyalBlue", width = 3)
    )
    fig.add_shape(type= "line",
    x0 = 18.285, y0 = -.05, x1 = 18.285, y1 = .05,
    line = dict (color = "RoyalBlue", width = 3)
    )
    fig.update_layout(
    margin=dict(l=1, r=1, t=1, b=1),
    paper_bgcolor="LightSteelBlue",
    )
    fig.show()
def calc ():
 try:
     x0 = float(entry1.get())
     y0 = float(entry2.get())
     Velocity = float(entry3.get())
     Theta = float(entry4.get())
     Rpm = float(entry5.get())
     Res = float(entry6.get())
     DeltaT = float(entry7.get())
     top_Spin(Velocity,x0,y0,Theta,Rpm,Res,DeltaT)
     pltgrp()
 except Exception as label8:
     label8 = tk.Label(root, text='Must Enter non Zero Values!')
     label8.config(font=('helvetica',10))
     canvas1.create_window(750,380, window=label8)           
button1 = tk.Button(text='Calculate Trajectory', command=calc, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(750,280, window=button1)
root.mainloop()
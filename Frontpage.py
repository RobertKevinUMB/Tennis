# Import module 
from tkinter import *
import subprocess
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("1920x1080")
root.title("Tennis Project CS682")

# Add image file
bg = PhotoImage(file = "Your_img.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 400,height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
  
  
# Create Buttons with links 
def run_topspin():
    subprocess.call(["python", "Topspin.py"])
button1 = Button(text='Trajectory with Topspin', command=run_topspin, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

def run_backspin():
    subprocess.call(["python", "Backspin.py"])
button2 = Button(text='Trajectory with Backspin', command=run_backspin, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

def run_both():
    subprocess.call(["python", "Plot.py"])
button3 = Button(text='Plot comparison of two CSVs - Folder must contain the CSVs', command=run_both, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

  
# Display Buttons
button1_canvas = canvas1.create_window( 300, 300, anchor = "nw", window = button1)
  
button2_canvas = canvas1.create_window( 700, 300, anchor = "nw", window = button2)
  
button3_canvas = canvas1.create_window( 1100, 300, anchor = "nw", window = button3)
  
# Execute tkinter
root.mainloop()
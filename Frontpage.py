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
    subprocess.call(["python3", "Topspin.py"])
button1 = Button( root, text = "Trajectory with Topspin", command=run_topspin)
def run_backspin():
    subprocess.call(["python3", "Backspin.py"])
button2 = Button( root, text = "Trajectory with Backspin", command=run_backspin)
def run_both():
    subprocess.call(["python3", "Plot.py"])
button3 = Button( root, text = "Compare two .csv files", command=run_both)
  
# Display Buttons
button1_canvas = canvas1.create_window( 100, 10, anchor = "nw", window = button1)
  
button2_canvas = canvas1.create_window( 100, 40, anchor = "nw", window = button2)
  
button3_canvas = canvas1.create_window( 100, 70, anchor = "nw", window = button3)
  
# Execute tkinter
root.mainloop()
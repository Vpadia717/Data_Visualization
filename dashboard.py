# Import the tkinter module and alias it as "tk"
import tkinter as tk

# Import the ttk submodule from tkinter for themed widgets
from tkinter import ttk

# Import the ImageTk and Image modules from the Python Imaging Library (PIL) for working with images
from PIL import ImageTk, Image

root = tk.Tk()  # Create a new instance of the Tk class from the tkinter module
# Set the size of the window to be 2000 x 1080 pixels
root.geometry("2000x1080")
# Create a new instance of the ttk Frame class for holding widgets
container = ttk.Frame()
# Set the title of the window to 'Covid Analysis Dashboard'
root.title('Covid Analysis Dashboard')
# Create a new instance of the Canvas class from the tkinter module with a width of 1300 and height of 700 pixels
canvas = tk.Canvas(container, width=1300, height=700)
# Create a new instance of the Scrollbar class from the ttk module with a vertical orientation and a command to scroll the canvas along the y-axis
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
# Create a new instance of the ttk Frame class for holding the scrollable widgets
scrollable_frame = ttk.Frame(canvas)

# Bind the "<Configure>" event to the scrollable_frame so that the canvas will update its scroll region whenever the frame is resized
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# Create a new window on the canvas and set its anchor point to the northwest corner
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Configure the canvas to use the scrollbar to control the vertical scrolling of the canvas content
canvas.configure(yscrollcommand=scrollbar.set)

# Open an image file named "img1.png" using the Python Imaging Library (PIL)
img = Image.open("img1.png")
# Resize the image to a width of 1250 pixels and a height of 500 pixels using anti-aliasing for smoother edges
resized = img.resize((1250, 500), Image.ANTIALIAS)
# Create a new instance of the PhotoImage class from the ImageTk module using the resized image
new_pic = ImageTk.PhotoImage(resized)
# Place the canvas widget in the top-left corner of the container using the northwest anchor point
canvas.place(anchor='nw')
# Create a new label widget with the text "Normal Layout"
tk.Label(text="Normal Layout")
# Create a new label widget inside the scrollable_frame with the new_pic image and pack it with 20 pixels of padding on all sides
label = tk.Label(scrollable_frame, image=new_pic)
label.pack(padx=20, pady=20)

# Open an image file named "img2.png" using the Python Imaging Library (PIL)
img1 = Image.open("img2.png")
# Resize the image to a width of 1250 pixels and a height of 500 pixels using anti-aliasing for smoother edges
resized1 = img1.resize((1250, 500), Image.ANTIALIAS)
# Create a new instance of the PhotoImage class from the ImageTk module using the resized image
new_pic1 = ImageTk.PhotoImage(resized1)
# Place the canvas widget in the top-left corner of the container using the northwest anchor point
canvas.place(anchor='nw')
# Create a new label widget with the text "Grid Layout"
tk.Label(text="Grid Layout")
# Create a new label widget inside the scrollable_frame with the new_pic1 image and pack it with 20 pixels of padding on all sides
label = tk.Label(scrollable_frame, image=new_pic1)
label.pack(padx=20, pady=20)

# Open an image file named "img3.png" using the Python Imaging Library (PIL)
img2 = Image.open("img3.png")
# Resize the image to a width of 1250 pixels and a height of 500 pixels using anti-aliasing for smoother edges
resized2 = img2.resize((1250, 500), Image.ANTIALIAS)
# Create a new instance of the PhotoImage class from the ImageTk module using the resized image
new_pic2 = ImageTk.PhotoImage(resized2)
# Place the canvas widget in the top-left corner of the container using the northwest anchor point
canvas.place(anchor='nw')
# Create a new label widget with the text "Normal Layout"
tk.Label(text="Normal Layout")
# Create a new label widget inside the scrollable_frame with the new_pic2 image and pack it with 20 pixels of padding on all sides
label = tk.Label(scrollable_frame, image=new_pic2)
label.pack(padx=20, pady=20)

# Open an image file named "img4.png" using the Python Imaging Library (PIL)
img3 = Image.open("img4.png")
# Resize the image to a width of 1250 pixels and a height of 500 pixels using anti-aliasing for smoother edges
resized3 = img3.resize((1250, 500), Image.ANTIALIAS)
# Create a new instance of the PhotoImage class from the ImageTk module using the resized image
new_pic3 = ImageTk.PhotoImage(resized3)
# Place the canvas widget in the top-left corner of the container using the northwest anchor point
canvas.place(anchor='nw')
# Create a new label widget with the text "Normal Layout"
tk.Label(text="Normal Layout")
# Create a new label widget inside the scrollable_frame with the new_pic3 image and pack it with 20 pixels of padding on all sides
label = tk.Label(scrollable_frame, image=new_pic3)
label.pack(padx=20, pady=20)

# Open an image file named "img5.png" using the Python Imaging Library (PIL)
img4 = Image.open("img5.png")
# Resize the image to a width of 1250 pixels and a height of 500 pixels using anti-aliasing for smoother edges
resized4 = img4.resize((1250, 500), Image.ANTIALIAS)
# Create a new instance of the PhotoImage class from the ImageTk module using the resized image
new_pic4 = ImageTk.PhotoImage(resized4)
# Place the canvas widget in the top-left corner of the container using the northwest anchor point
canvas.place(anchor='nw')
# Create a new label widget with the text "Normal Layout"
tk.Label(text="Normal Layout")
# Create a new label widget inside the scrollable_frame with the new_pic4 image and pack it with 20 pixels of padding on all sides
label = tk.Label(scrollable_frame, image=new_pic4)
label.pack(padx=20, pady=20)

# Pack the container widget inside the root window with 20 pixels of padding on all sides
container.pack(padx=20, pady=20)
# Pack the canvas widget inside the container on the left side and fill both the x and y axis of the container while expanding to fill available space
canvas.pack(side="left", fill="both", expand=True)
# Pack the scrollbar widget inside the container on the right side and fill only the y-axis of the container
scrollbar.pack(side="right", fill="y")

root.mainloop()  # Run the main event loop of the Tkinter application

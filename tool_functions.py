# tool_functions.py
import tkinter as tk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk  # For adding images to buttons

def create_buttons(app, frame):
    """
    Create the control buttons for the drawing app and place them in the specified frame.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    frame (Frame): The frame to add the buttons to.
    """
    # Button to switch to pen (with an image)
    pen_image = ImageTk.PhotoImage(Image.open("./images/pencil_tool.gif"))
    pen_button = tk.Button(frame, image=pen_image, command=lambda: use_pen(app))
    pen_button.image = pen_image  # Keep a reference to avoid garbage collection
    pen_button.pack(pady=(10, 2))  # Adjust padding to make the button closer to the top left corner

    # Button to use eraser (with an image)
    eraser_image = ImageTk.PhotoImage(Image.open("./images/eraser_tool.gif"))
    eraser_button = tk.Button(frame, image=eraser_image, command=lambda: use_eraser(app))
    eraser_button.image = eraser_image  # Keep a reference to avoid garbage collection
    eraser_button.pack(pady=2)

    # Button to clear the canvas
    clear_button = tk.Button(frame, text='Clear', command=lambda: app.canvas.delete("all"))
    clear_button.pack(pady=2)

def create_color_picker(app, frame):
    """
    Create color picker buttons and add them to the specified frame.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    frame (Frame): The frame to add the color buttons to.
    """
    # Frame for color picker buttons
    color_frame = tk.Frame(frame)
    color_frame.pack(pady=(10, 2))

    # Button to open a color chooser dialog
    custom_color_button = tk.Button(frame, text='Custom Color', command=lambda: choose_color(app))
    custom_color_button.pack(pady=(10, 2))  # Adjust padding to place it higher in the frame

    # Add some common color buttons in a grid (2 columns, 6 rows)
    colors = ["black", "red", "blue", "green", "yellow", "purple", "orange", "brown", "pink", "cyan", "grey", "white"]
    for index, color in enumerate(colors):
        row = index // 2
        col = index % 2
        color_button = tk.Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: set_pen_color(app, c))
        color_button.grid(row=row, column=col, padx=2, pady=2)

def choose_color(app):
    """
    Open a color picker dialog to choose pen color.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    """
    app.eraser_on = False
    color = askcolor(color=app.pen_color)[1]
    if color:
        app.pen_color = color

def set_pen_color(app, color):
    """
    Set the pen color to a specific color.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    color (str): The color to set the pen to.
    """
    app.eraser_on = False
    app.pen_color = color

def use_pen(app):
    """
    Switch to pen mode for drawing.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    """
    app.eraser_on = False
    app.canvas.config(cursor="pencil")  # Change cursor to pen icon

def use_eraser(app):
    """
    Switch to eraser mode for erasing.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    """
    app.eraser_on = True
    app.canvas.config(cursor="dot")  # Change cursor to indicate eraser

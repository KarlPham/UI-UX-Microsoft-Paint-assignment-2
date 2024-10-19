# canvas_functions.py
import tkinter as tk
from draw_functions import draw

def create_canvas(root):
    """
    Create a canvas for drawing.

    Parameters:
    root (Tk): The root window to attach the canvas to.

    Returns:
    Canvas: The created canvas widget.
    """
    canvas = tk.Canvas(root, bg='white', width=600, height=400)
    canvas.pack()
    return canvas

def bind_canvas_events(canvas, app):
    """
    Bind the necessary events to the canvas for drawing.

    Parameters:
    canvas (Canvas): The canvas to bind events to.
    app (DrawingApp): The DrawingApp instance.
    """
    canvas.bind("<B1-Motion>", lambda event: draw(event, app))  # Draw when mouse is dragged with left button held
    canvas.bind("<ButtonRelease-1>", lambda event: reset(app))  # Reset pen position when left mouse button is released

def reset(app):
    """
    Reset the last position of the pen.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    """
    app.last_x, app.last_y = None, None

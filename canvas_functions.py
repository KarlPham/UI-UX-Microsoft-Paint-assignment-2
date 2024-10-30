import tkinter as tk
from draw_functions import draw, finish_shape, start_shape

def create_canvas(root):
    """
    Creates and sets up a Tkinter canvas widget.

    Parameters:
    root (Tk): The root Tkinter window or frame.

    Returns:
    Canvas: The created canvas widget.
    """
    canvas = tk.Canvas(root, bg='white', width=600, height=400)
    canvas.pack()
    return canvas

def bind_canvas_events(canvas, app):
    """
    Binds mouse events to the canvas for drawing and shape creation.

    Parameters:
    canvas (Canvas): The canvas widget to bind events to.
    app (DrawingApp): The main application instance.
    """
    # Bind left mouse drag to draw (for freehand or shape preview)
    canvas.bind("<B1-Motion>", lambda event: draw(event, app))
    
    # Bind left mouse button press to start drawing a shape
    canvas.bind("<ButtonPress-1>", lambda event: start_shape(event, app))
    
    # Bind left mouse button release to finish shape or reset for freehand
    canvas.bind("<ButtonRelease-1>", lambda event: reset_or_finish_shape(app))

def reset(app):
    """
    Resets the last x and y coordinates for freehand drawing.

    Parameters:
    app (DrawingApp): The main application instance.
    """
    app.last_x, app.last_y = None, None  # Clear last coordinates

def reset_or_finish_shape(app):
    """
    Determines whether to finalize a shape or reset for freehand drawing.

    Parameters:
    app (DrawingApp): The main application instance.
    """
    if app.shape_mode:
        finish_shape(app)  # Finalize shape drawing if in shape mode
    else:
        reset(app)  # Reset coordinates for freehand drawing

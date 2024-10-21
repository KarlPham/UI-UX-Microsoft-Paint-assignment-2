import tkinter as tk
from draw_functions import draw, finish_shape, start_shape

def create_canvas(root):
    canvas = tk.Canvas(root, bg='white', width=600, height=400)
    canvas.pack()
    return canvas

def bind_canvas_events(canvas, app):
    canvas.bind("<B1-Motion>", lambda event: draw(event, app))  # Draw when mouse is dragged with left button held
    canvas.bind("<ButtonPress-1>", lambda event: start_shape(event, app))  # Start shape drawing on button press
    canvas.bind("<ButtonRelease-1>", lambda event: reset_or_finish_shape(app))  # Finalize shape or reset pen position

def reset(app):
    app.last_x, app.last_y = None, None

def reset_or_finish_shape(app):
    if app.shape_mode:
        finish_shape(app)  # Finalize shape drawing
    else:
        reset(app)  # Reset freehand drawing

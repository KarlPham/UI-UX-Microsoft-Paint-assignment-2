import tkinter as tk

def draw(event, app):
    """
    Draws on the canvas based on the current drawing mode, either freehand or shape preview.

    Parameters:
    event (Event): The Tkinter event containing coordinates for drawing.
    app (DrawingApp): The main application instance.
    """
    x, y = event.x, event.y  # Current mouse coordinates

    # Clear any previous shape preview if it exists
    app.canvas.delete("preview_shape")
    
    # If in shape mode and shape start coordinates are set, draw a shape preview
    if app.shape_mode and app.shape_start_x is not None and app.shape_start_y is not None:
        # Draw shape outline as preview based on pen size and color
        if app.shape_mode == "rectangle":
            app.canvas.create_rectangle(app.shape_start_x, app.shape_start_y, x, y, 
                                        outline=app.pen_color, width=app.pen_size, tags="preview_shape")
        elif app.shape_mode == "oval":
            app.canvas.create_oval(app.shape_start_x, app.shape_start_y, x, y, 
                                   outline=app.pen_color, width=app.pen_size, tags="preview_shape")
    
    # For freehand drawing or erasing
    elif app.last_x is not None and app.last_y is not None:
        color = 'white' if app.eraser_on else app.pen_color  # Use white for eraser

        # Draw line segment with customizable thickness
        app.canvas.create_line(app.last_x, app.last_y, x, y, fill=color, width=app.pen_size, 
                               capstyle=tk.ROUND, smooth=True)
    
    # Update last drawn coordinates for continuous drawing
    app.last_x, app.last_y = x, y

def finish_shape(app):
    """
    Completes the shape drawing and finalizes it on the canvas.

    Parameters:
    app (DrawingApp): The main application instance.
    """
    # Draw final shape if in shape mode and start coordinates are set
    if app.shape_mode and app.shape_start_x is not None and app.shape_start_y is not None:
        x1, y1 = app.shape_start_x, app.shape_start_y
        x2, y2 = app.last_x, app.last_y
        color = 'white' if app.eraser_on else app.pen_color  # White color for eraser

        # Draw shape based on selected shape mode
        if app.shape_mode == "rectangle":
            app.canvas.create_rectangle(x1, y1, x2, y2, outline=color, width=app.pen_size)
        elif app.shape_mode == "oval":
            app.canvas.create_oval(x1, y1, x2, y2, outline=color, width=app.pen_size)
        elif app.shape_mode == "line":
            app.canvas.create_line(x1, y1, x2, y2, fill=color, width=app.pen_size)

        # Reset shape-related variables after drawing is complete
        app.shape_start_x, app.shape_start_y = None, None
        app.last_x, app.last_y = None, None
        app.shape_mode = False  # Exit shape mode

def start_shape(event, app):
    """
    Sets the initial coordinates for shape drawing.

    Parameters:
    event (Event): The Tkinter event containing the starting coordinates.
    app (DrawingApp): The main application instance.
    """
    app.shape_start_x = event.x  # Starting x-coordinate for shape
    app.shape_start_y = event.y  # Starting y-coordinate for shape
    app.last_x = event.x        # Initial last x-coordinate for smooth drawing
    app.last_y = event.y        # Initial last y-coordinate for smooth drawing

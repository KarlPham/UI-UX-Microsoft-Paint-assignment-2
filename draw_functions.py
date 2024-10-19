# draw_functions.py

def draw(event, app):
    """
    Draw on the canvas based on the current position of the mouse.

    Parameters:
    event (Event): The event triggered by moving the mouse while holding down the button.
    app (DrawingApp): The DrawingApp instance.
    """
    x, y = event.x, event.y
    if app.last_x and app.last_y:
        # Set color to white if eraser is on, otherwise use the pen color
        color = 'white' if app.eraser_on else app.pen_color
        # Draw a line between the previous and current position
        app.canvas.create_line((app.last_x, app.last_y, x, y), fill=color, width=5)

    # Update the last position to the current position
    app.last_x, app.last_y = x, y

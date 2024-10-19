# main.py (Main Application File)
import tkinter as tk
from canvas_functions import create_canvas, bind_canvas_events
from tool_functions import create_buttons, create_color_picker
from draw_functions import draw

class DrawingApp:
    def __init__(self, master, window_width=800, window_height=600):
        # Set up main window with specified size
        self.master = master
        self.master.title("Drawing App - Microsoft Clone")
        self.master.geometry(f"{window_width}x{window_height}")

        # Initialize drawing settings
        self.pen_color = 'black'  # Default pen color
        self.eraser_on = False    # Eraser mode off by default
        self.last_x, self.last_y = None, None  # Track last position for drawing

        # Create Tools Frame on the left
        tools_frame = tk.Frame(self.master, padx=5, pady=5, bg="lightgrey")
        tools_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the Canvas on the right side of the tools frame
        self.canvas = create_canvas(self.master)
        self.canvas.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Create buttons and color picker in the tools frame
        create_buttons(self, tools_frame)
        create_color_picker(self, tools_frame)

        # Bind canvas events for drawing
        bind_canvas_events(self.canvas, self)

if __name__ == "__main__":
    # Create the main application window
    master = tk.Tk()
    app = DrawingApp(master)
    master.mainloop()

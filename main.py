import tkinter as tk
from canvas_functions import create_canvas, bind_canvas_events
from tool_functions import create_buttons, create_color_picker, save_as_file, save_file, open_file, change_pen_size
from draw_functions import draw, finish_shape
from tkinter import Menu

class DrawingApp:
    def __init__(self, master, window_width=800, window_height=600):
        """
        Initializes the main application window and sets up the drawing environment.
        Args:
            master (Tk): The main Tkinter window.
            window_width (int): Width of the application window.
            window_height (int): Height of the application window.
        """
        # Set up the main window with a title and size
        self.master = master 
        self.master.title("Drawing App - Microsoft Clone")
        self.master.geometry(f"{window_width}x{window_height}")

        # Drawing tool attributes
        self.pen_color = 'black'  # Default pen color
        self.eraser_on = False    # Eraser mode off by default
        self.pen_size = 5         # Default pen size
        self.shape_mode = False   # Shape mode off by default
        self.last_x, self.last_y = None, None  # Track last coordinates for drawing
        self.shape_start_x = None # Starting x coordinate for shape drawing
        self.shape_start_y = None # Starting y coordinate for shape drawing

        # Set up the tools frame (left panel)
        tools_frame = tk.Frame(self.master, padx=5, pady=5, bg="lightgrey")
        tools_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the drawing canvas (right panel)
        self.canvas = create_canvas(self.master)
        self.canvas.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Set up tool buttons and color picker within the tools frame
        create_buttons(self, tools_frame)
        create_color_picker(self, tools_frame)

        # Bind mouse events to the canvas for drawing actions
        bind_canvas_events(self.canvas, self)

        # Add pen size slider in the tools frame
        pen_size_label = tk.Label(tools_frame, text="Pen Size", bg="lightgrey")
        pen_size_label.pack(pady=5)
        
        # Slider to adjust pen size dynamically
        self.pen_size_slider = tk.Scale(
            tools_frame, from_=1, to=20, orient=tk.HORIZONTAL, bg="lightgrey", 
            command=lambda value: change_pen_size(self, value)
        )
        self.pen_size_slider.set(self.pen_size)  # Initialize slider with default pen size
        self.pen_size_slider.pack()

        # Set up the Menu Bar at the top
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # "File" menu for opening and saving files
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=lambda: open_file(self))  # Open file command
        file_menu.add_command(label="Save", command=lambda: save_file(self))  # Save file command
        file_menu.add_command(label="Save As", command=lambda: save_as_file(self))  # Save As command

if __name__ == "__main__":
    # Initialize and run the drawing application
    master = tk.Tk()
    app = DrawingApp(master)
    master.mainloop()

import tkinter as tk
from canvas_functions import create_canvas, bind_canvas_events
from tool_functions import create_buttons, create_color_picker, save_as_file, save_file, open_file, change_pen_size
from draw_functions import draw, finish_shape
from tkinter import Menu

class DrawingApp:
    def __init__(self, master, window_width=800, window_height=600):
        # Set up the main window with the specified size
        self.master = master 
        self.master.title("Drawing App - Microsoft Clone")
        self.master.geometry(f"{window_width}x{window_height}")

        # Initialize drawing settings
        self.pen_color = 'black'
        self.eraser_on = False
        self.pen_size = 5  # Default pen size
        self.shape_mode = False
        self.last_x, self.last_y = None, None
        self.shape_start_x = None
        self.shape_start_y = None

        # Create Tools Frame on the left
        tools_frame = tk.Frame(self.master, padx=5, pady=5, bg="lightgrey")
        tools_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create Canvas on the right side of the tools frame
        self.canvas = create_canvas(self.master)
        self.canvas.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Create tool buttons and color picker in the tools frame
        create_buttons(self, tools_frame)
        create_color_picker(self, tools_frame)

        # Bind canvas events for drawing
        bind_canvas_events(self.canvas, self)

        # Add pen size slider in the tools frame
        pen_size_label = tk.Label(tools_frame, text="Pen Size", bg="lightgrey")
        pen_size_label.pack(pady=5)
        
        self.pen_size_slider = tk.Scale(tools_frame, from_=1, to=20, orient=tk.HORIZONTAL, bg="lightgrey", command=lambda value: change_pen_size(self, value))
        self.pen_size_slider.set(self.pen_size)  # Set default pen size
        self.pen_size_slider.pack()

        # Create Menu Bar
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # Create "File" Menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=lambda: open_file(self))  # Add Open command
        file_menu.add_command(label="Save", command=lambda: save_file(self))
        file_menu.add_command(label="Save As", command=lambda: save_as_file(self))

if __name__ == "__main__":
    master = tk.Tk()
    app = DrawingApp(master)
    master.mainloop()

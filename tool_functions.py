import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import Image, ImageTk  # For handling image files in Tkinter
from PIL import ImageGrab

def create_buttons(app, frame):
    """
    Creates tool buttons for the drawing app and adds them to the specified frame.

    Parameters:
    app (DrawingApp): The main application instance.
    frame (Frame): Frame to contain the buttons.
    """
    # Frame to hold tool buttons in a 2-column layout
    tools_frame = tk.Frame(frame)
    tools_frame.pack(pady=(10, 2))

    # Pen tool button
    pen_image = ImageTk.PhotoImage(Image.open("./images/pencil_tool.gif"))
    pen_button = tk.Button(tools_frame, image=pen_image, command=lambda: use_pen(app))
    pen_button.image = pen_image  # Prevent garbage collection
    pen_button.grid(row=0, column=0, padx=2, pady=2)

    # Eraser tool button
    eraser_image = ImageTk.PhotoImage(Image.open("./images/eraser_tool.gif"))
    eraser_button = tk.Button(tools_frame, image=eraser_image, command=lambda: use_eraser(app))
    eraser_button.image = eraser_image  # Prevent garbage collection
    eraser_button.grid(row=0, column=1, padx=2, pady=2)

    # Rectangle shape tool button
    rectangle_image = ImageTk.PhotoImage(Image.open("./images/shape_tool.gif"))
    rectangle_button = tk.Button(tools_frame, image=rectangle_image, command=lambda: use_shape(app, "rectangle"))
    rectangle_button.image = rectangle_image  # Prevent garbage collection
    rectangle_button.grid(row=1, column=0, padx=2, pady=2)

    # Oval shape tool button
    oval_image = ImageTk.PhotoImage(Image.open("./images/oval_tool.gif"))
    oval_button = tk.Button(tools_frame, image=oval_image, command=lambda: use_shape(app, "oval"))
    oval_button.image = oval_image  # Prevent garbage collection
    oval_button.grid(row=1, column=1, padx=2, pady=2)

    # Line shape tool button
    line_image = ImageTk.PhotoImage(Image.open("./images/line_tool.gif"))
    line_button = tk.Button(tools_frame, image=line_image, command=lambda: use_shape(app, "line"))
    line_button.image = line_image  # Prevent garbage collection
    line_button.grid(row=2, column=0, padx=2, pady=2)

    # Clear canvas button
    clear_image = ImageTk.PhotoImage(Image.open("./images/clear_tool.gif"))
    clear_button = tk.Button(tools_frame, image=clear_image, command=lambda: app.canvas.delete("all"))
    clear_button.image = clear_image  # Prevent garbage collection
    clear_button.grid(row=2, column=1, padx=2, pady=2)

    # Button for inserting images onto the canvas
    insert_image_button = tk.Button(frame, text='Insert Image', command=lambda: insert_image(app))
    insert_image_button.pack(pady=(10, 2))

def create_color_picker(app, frame):
    """
    Creates color selection buttons for choosing pen colors and adds them to the frame.
    
    Parameters:
    app (DrawingApp): The main application instance.
    frame (Frame): Frame to contain the color picker buttons.
    """
    color_frame = tk.Frame(frame)
    color_frame.pack(pady=(10, 2))

    # Button for custom color picker
    custom_color_button = tk.Button(frame, text='Custom Color', command=lambda: choose_color(app))
    custom_color_button.pack(pady=(10, 2))

    # Standard color selection buttons
    colors = ["black", "red", "blue", "green", "yellow", "purple", "orange", "brown", "pink", "cyan", "grey", "white"]
    for index, color in enumerate(colors):
        row = index // 2
        col = index % 2
        color_button = tk.Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: set_pen_color(app, c))
        color_button.grid(row=row, column=col, padx=2, pady=2)

def insert_image(app):
    """
    Opens a file dialog to select an image and inserts it into the canvas.

    Parameters:
    app (DrawingApp): The main application instance.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:  # If an image file is selected
        image = Image.open(file_path)
        image.thumbnail((app.canvas.winfo_width(), app.canvas.winfo_height()))  # Resize image to fit canvas
        photo = ImageTk.PhotoImage(image)
        
        # Place the image at the center of the canvas
        x = app.canvas.winfo_width() // 2
        y = app.canvas.winfo_height() // 2
        app.canvas.create_image(x, y, image=photo, anchor=tk.CENTER)
        app.canvas.image = photo  # Keep a reference to prevent garbage collection

def choose_color(app):
    """
    Opens a color chooser dialog to set a custom pen color.
    
    Parameters:
    app (DrawingApp): The main application instance.
    """
    app.eraser_on = False
    color = askcolor(color=app.pen_color)[1]
    if color:
        app.pen_color = color

def set_pen_color(app, color):
    """
    Sets the pen color directly from the available color options.

    Parameters:
    app (DrawingApp): The main application instance.
    color (str): The selected color.
    """
    app.eraser_on = False
    app.pen_color = color

def use_pen(app):
    """
    Switches to pen mode for freehand drawing.

    Parameters:
    app (DrawingApp): The main application instance.
    """
    app.eraser_on = False
    app.canvas.config(cursor="pencil")  # Change cursor to pencil icon

def use_eraser(app):
    """
    Switches to eraser mode to remove parts of the drawing.

    Parameters:
    app (DrawingApp): The main application instance.
    """
    app.eraser_on = True
    app.canvas.config(cursor="dot")  # Change cursor to eraser icon

def use_shape(app, shape_type):
    """
    Activates a shape-drawing mode for creating basic shapes.
    
    Parameters:
    app (DrawingApp): The main application instance.
    shape_type (str): Type of shape (rectangle, oval, or line).
    """
    app.eraser_on = False  # Disable eraser mode
    app.shape_mode = shape_type  # Set the shape mode
    app.canvas.config(cursor="cross")  # Set cursor to cross for shape mode

def save_file(app):
    """
    Saves the current canvas drawing to an existing file.

    Parameters:
    app (DrawingApp): The main application instance.
    """
    if hasattr(app, 'current_file_path'):
        # Save to the existing file path
        image = ImageGrab.grab(bbox=(app.canvas.winfo_rootx(), app.canvas.winfo_rooty(),
                                     app.canvas.winfo_rootx() + app.canvas.winfo_width(),
                                     app.canvas.winfo_rooty() + app.canvas.winfo_height()))
        image.save(app.current_file_path)
    else:
        save_as_file(app)  # If no file path, save as a new file

def save_as_file(app):
    """
    Opens a dialog to save the current canvas drawing as a new file.
    
    Parameters:
    app (DrawingApp): The main application instance.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                             filetypes=[("PNG files", "*.png"), 
                                                        ("JPEG files", "*.jpg;*.jpeg"), 
                                                        ("GIF files", "*.gif")])
    if file_path:
        image = ImageGrab.grab(bbox=(app.canvas.winfo_rootx(), app.canvas.winfo_rooty(),
                                     app.canvas.winfo_rootx() + app.canvas.winfo_width(),
                                     app.canvas.winfo_rooty() + app.canvas.winfo_height()))
        image.save(file_path)
        app.current_file_path = file_path  # Store the current file path

def open_file(app):
    """
    Opens an image file and displays it on the canvas.

    Parameters:
    app (DrawingApp): The main application instance.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        app.canvas.delete("all")  # Clear the canvas
        img = Image.open(file_path)
        app.image = ImageTk.PhotoImage(img)  # Prevent garbage collection
        app.canvas.create_image(0, 0, anchor=tk.NW, image=app.image)  # Place image at top-left
        app.image_file_path = file_path

def change_pen_size(app, value):
    """
    Adjusts the pen size based on slider input.
    
    Parameters:
    app (DrawingApp): The main application instance.
    value (str): The new pen size value from the slider.
    """
    app.pen_size = int(value)

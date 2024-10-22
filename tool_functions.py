# tool_functions.py
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import Image, ImageTk  # For adding images to buttons
from PIL import ImageGrab

def create_buttons(app, frame):
    """
    Create the control buttons for the drawing app and place them in the specified frame.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    frame (Frame): The frame to add the buttons to.
    """
    # Frame for the tool buttons (2 columns)
    tools_frame = tk.Frame(frame)
    tools_frame.pack(pady=(10, 2))

    # Button to switch to pen (with an image)
    pen_image = ImageTk.PhotoImage(Image.open("./images/pencil_tool.gif"))
    pen_button = tk.Button(tools_frame, image=pen_image, command=lambda: use_pen(app))
    pen_button.image = pen_image  # Keep a reference to avoid garbage collection
    pen_button.grid(row=0, column=0, padx=2, pady=2)

    # Button to use eraser (with an image)
    eraser_image = ImageTk.PhotoImage(Image.open("./images/eraser_tool.gif"))
    eraser_button = tk.Button(tools_frame, image=eraser_image, command=lambda: use_eraser(app))
    eraser_button.image = eraser_image  # Keep a reference to avoid garbage collection
    eraser_button.grid(row=0, column=1, padx=2, pady=2)

    # Button for rectangle shape tool (with an image)
    rectangle_image = ImageTk.PhotoImage(Image.open("./images/shape_tool.gif"))
    rectangle_button = tk.Button(tools_frame, image=rectangle_image, command=lambda: use_shape(app, "rectangle"))
    rectangle_button.image = rectangle_image  # Keep a reference to avoid garbage collection
    rectangle_button.grid(row=1, column=0, padx=2, pady=2)

    # Button for oval shape tool (with an image)
    oval_image = ImageTk.PhotoImage(Image.open("./images/oval_tool.gif"))
    oval_button = tk.Button(tools_frame, image=oval_image, command=lambda: use_shape(app, "oval"))
    oval_button.image = oval_image  # Keep a reference to avoid garbage collection
    oval_button.grid(row=1, column=1, padx=2, pady=2)

    # Button for line shape tool (with an image)
    line_image = ImageTk.PhotoImage(Image.open("./images/line_tool.gif"))
    line_button = tk.Button(tools_frame, image=line_image, command=lambda: use_shape(app, "line"))
    line_button.image = line_image  # Keep a reference to avoid garbage collection
    line_button.grid(row=2, column=0, padx=2, pady=2)

    # Button to clear the canvas (with an image)
    clear_image = ImageTk.PhotoImage(Image.open("./images/clear_tool.gif"))
    clear_button = tk.Button(tools_frame, image=clear_image, command=lambda: app.canvas.delete("all"))
    clear_button.image = clear_image  # Keep a reference to avoid garbage collection
    clear_button.grid(row=2, column=1, padx=2, pady=2)

    # Button to insert an image (placed at the bottom)
    insert_image_button = tk.Button(frame, text='Insert Image', command=lambda: insert_image(app))
    insert_image_button.pack(pady=(10, 2))

def create_color_picker(app, frame):
    color_frame = tk.Frame(frame)
    color_frame.pack(pady=(10, 2))

    custom_color_button = tk.Button(frame, text='Custom Color', command=lambda: choose_color(app))
    custom_color_button.pack(pady=(10, 2))

    colors = ["black", "red", "blue", "green", "yellow", "purple", "orange", "brown", "pink", "cyan", "grey", "white"]
    for index, color in enumerate(colors):
        row = index // 2
        col = index % 2
        color_button = tk.Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: set_pen_color(app, c))
        color_button.grid(row=row, column=col, padx=2, pady=2)

def insert_image(app):
    """
    Open a file dialog to choose an image and insert it into the canvas.

    Parameters:
    app (DrawingApp): The DrawingApp instance.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:  # If a file was selected
        image = Image.open(file_path)
        image.thumbnail((app.canvas.winfo_width(), app.canvas.winfo_height()))  # Resize image to fit canvas
        photo = ImageTk.PhotoImage(image)
        
        # Get coordinates to place the image (you can modify this as needed)
        x = app.canvas.winfo_width() // 2
        y = app.canvas.winfo_height() // 2
        
        # Create an image on the canvas
        app.canvas.create_image(x, y, image=photo, anchor=tk.CENTER)
        
        # Keep a reference to avoid garbage collection
        app.canvas.image = photo
        

def choose_color(app):
    app.eraser_on = False
    color = askcolor(color=app.pen_color)[1]
    if color:
        app.pen_color = color

def set_pen_color(app, color):
    app.eraser_on = False
    app.pen_color = color

def use_pen(app):
    app.eraser_on = False
    app.canvas.config(cursor="pencil")  # Change cursor to pen icon

def use_eraser(app):
    app.eraser_on = True
    app.canvas.config(cursor="dot")  # Change cursor to indicate eraser

# New function for using the shape tool
def use_shape(app, shape_type):
    """
    Switch to shape-drawing mode.
    
    Parameters:
    app (DrawingApp): The DrawingApp instance.
    shape_type (str): The type of shape to draw (rectangle, oval, line).
    """
    app.eraser_on = False  # Ensure eraser is off
    app.shape_mode = shape_type  # Set shape mode on to the specific shape type
    app.canvas.config(cursor="cross")  # Change cursor to indicate shape mode

def save_file(app):
    """
    Save the current drawing as a PNG file.
    
    Parameters:
    app (DrawingApp): The DrawingApp instance.
    """
    if hasattr(app, 'current_file_path'):
        # Save to the existing file path
        image = ImageGrab.grab(bbox=(app.canvas.winfo_rootx(), app.canvas.winfo_rooty(),
                                       app.canvas.winfo_rootx() + app.canvas.winfo_width(),
                                       app.canvas.winfo_rooty() + app.canvas.winfo_height()))
        image.save(app.current_file_path)
    else:
        # If no file path exists, call save_as_file
        save_as_file(app)

def save_as_file(app):
    """
    Save the current drawing as a new PNG file.
    
    Parameters:
    app (DrawingApp): The DrawingApp instance.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                               filetypes=[("PNG files", "*.png"), 
                                                          ("JPEG files", "*.jpg;*.jpeg"), 
                                                          ("GIF files", "*.gif")])
    if file_path:
        # Save the image to the specified path
        image = ImageGrab.grab(bbox=(app.canvas.winfo_rootx(), app.canvas.winfo_rooty(),
                                       app.canvas.winfo_rootx() + app.canvas.winfo_width(),
                                       app.canvas.winfo_rooty() + app.canvas.winfo_height()))
        image.save(file_path)
        app.current_file_path = file_path  # Lưu đường dẫn file hiện tại

def open_file(app):
    """Open an image file and display it on the canvas."""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        # Clear the current canvas
        app.canvas.delete("all")

        # Load the image and display it on the canvas
        img = Image.open(file_path)
        app.image = ImageTk.PhotoImage(img)  # Keep a reference to avoid garbage collection
        app.canvas.create_image(0, 0, anchor=tk.NW, image=app.image)  # Display image at top-left corner  
        app.image_file_path = file_path  # Save the path for later use if needed

def change_pen_size(app, value):
    """
    Update the pen and eraser size based on the slider value.
    
    Parameters:
    app (DrawingApp): The DrawingApp instance.
    value (str): The new size value from the slider.
    """
    app.pen_size = int(value)
    # The eraser size is also updated since it is controlled by the same slider.
    if app.eraser_on:
        app.canvas.config(cursor=f"@./images/eraser_tool_{app.pen_size}.cur")
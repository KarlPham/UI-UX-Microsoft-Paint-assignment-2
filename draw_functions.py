# draw_functions.py
import tkinter as tk
def draw(event, app):
    x, y = event.x, event.y
    if app.shape_mode and app.shape_start_x is not None and app.shape_start_y is not None:
        # Xóa hình preview trước đó nếu có
        app.canvas.delete("preview_shape")
        
        # Vẽ hình chữ nhật preview với viền có độ dày theo bút
        app.canvas.create_rectangle(app.shape_start_x, app.shape_start_y, x, y, outline=app.pen_color, width=app.pen_size, tags="preview_shape")
    
    elif app.last_x is not None and app.last_y is not None:
        # Nếu đang ở chế độ tẩy, vẽ bằng màu trắng
        color = 'white' if app.eraser_on else app.pen_color
        
        # Vẽ đường với độ dày tùy chỉnh (app.pen_size)
        app.canvas.create_line((app.last_x, app.last_y, x, y), fill=color, width=app.pen_size, capstyle=tk.ROUND, smooth=True)
    
    # Cập nhật tọa độ cuối cùng
    app.last_x, app.last_y = x, y



def finish_shape(app):
    if app.shape_mode and app.shape_start_x is not None and app.shape_start_y is not None:
        x1, y1 = app.shape_start_x, app.shape_start_y
        x2, y2 = app.last_x, app.last_y
        color = 'white' if app.eraser_on else app.pen_color

        if app.shape_mode == "rectangle":
            app.canvas.create_rectangle(x1, y1, x2, y2, outline=color, width=5)
        elif app.shape_mode == "oval":
            app.canvas.create_oval(x1, y1, x2, y2, outline=color, width=5)
        elif app.shape_mode == "line":
            app.canvas.create_line(x1, y1, x2, y2, fill=color, width=5)

        # Reset shape variables after finishing the shape
        app.shape_start_x, app.shape_start_y = None, None
        app.last_x, app.last_y = None, None
        app.shape_mode = False  # Reset shape mode after finishing the shape


def start_shape(event, app):
    app.shape_start_x = event.x
    app.shape_start_y = event.y
    app.last_x = event.x
    app.last_y = event.y



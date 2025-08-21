import tkinter as tk
from PIL import Image, ImageTk
from itertools import cycle

def animate(label, frames): # required for the gif to work
    frame = next(frames)
    label.config(image=frame)
    label.after(36, animate, label, frames) # 36 is the frame duration in milliseconds

window = tk.Tk()
window.title('feesh')
window.resizable(False, False)

window_icon = tk.PhotoImage(file="assets/fish.png")
window.iconphoto(True, window_icon)

gif = "assets/fish_spinning.gif"
gif_file = Image.open(gif)

# appends frames to the frame_index list
frame_index = []
for frame in range(gif_file.n_frames):
    gif_file.seek(frame)
    frame_index.append(ImageTk.PhotoImage(gif_file))

frames = cycle(frame_index)

window_label = tk.Label(window)
window_label.pack()

animate(window_label, frames)

window.mainloop()
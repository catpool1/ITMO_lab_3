import tkinter as tk

SIZE = 500
ALP = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def render_frames(parent, img):
    # body = tk.Frame(parent)
    # body.pack(side=tk.TOP, fill=tk.X)
    lbl = tk.Label(parent, image=img)
    lbl.pack(side=tk.TOP, fill=tk.BOTH)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(f'{SIZE}x{SIZE}')
    root.title('Viber')
    img = tk.PhotoImage(file='main_bg.png', width=SIZE, height=SIZE)

    body = render_frames(root, img)
    root.mainloop()
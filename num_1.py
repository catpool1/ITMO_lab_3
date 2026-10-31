import tkinter as tk

SIZE = 500
ALP = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def render_frames(parent):
    pass


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(f'{SIZE}x{SIZE}')
    root.title('Viber')
    body = render_frames(root)
    root.mainloop()
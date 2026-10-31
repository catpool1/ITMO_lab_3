import tkinter as tk

SIZE = 500
ALP = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def render_frames(parent, img):
    body = tk.Frame(parent, bg="#D11EB9")
    footer = tk.Frame(parent, bg="#D11EB9")

    body.pack(side=tk.TOP, fill=tk.X)
    footer.pack(side=tk.BOTTOM, fill=tk.X)

    render_image(body, img)
    render_footer(footer)


def render_image(parent, img):
    image = tk.Label(parent, image=img)
    image.pack(side=tk.TOP, fill=tk.BOTH)


def render_footer(parent, key="-"):
    button_gen = tk.Button(parent, text="Generate key", font=("", 14))
    button_random = tk.Button(parent, text="Generate first part", font=("", 14))
    lbl_part = tk.Label(parent, text="Entry first part:", font=("", 14), bg="#D11EB9")
    entry_part = tk.Entry(parent, font=("", 14))
    lbl_key = tk.Label(parent, text=f"key:{key}", font=("", 14), bg="#D11EB9")

    lbl_key.pack(side=tk.BOTTOM, fill=tk.X)
    entry_part.pack(side=tk.BOTTOM, fill=tk.X)
    lbl_part.pack(side=tk.BOTTOM, fill=tk.X)
    button_gen.pack(side=tk.LEFT, fill=tk.X, expand=True)
    button_random.pack(side=tk.RIGHT, fill=tk.X)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(f'{SIZE}x{SIZE}')
    root.title('Viber')
    img = tk.PhotoImage(file='main_bg.png')
    render_frames(root, img)
    root.mainloop()
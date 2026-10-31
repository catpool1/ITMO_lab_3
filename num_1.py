import tkinter as tk
import random

SIZE = 500
ALP = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def render_frames(parent, img):
    body = tk.Frame(parent, bg="#D11EB9")
    footer = tk.Frame(parent, bg="#D11EB9")

    footer.pack(side=tk.BOTTOM, fill=tk.X)
    body.pack(side=tk.TOP, fill=tk.X)

    render_image(body, img)
    render_footer(footer)


def render_image(parent, img):
    image = tk.Label(parent, image=img)
    image.pack(side=tk.TOP, fill=tk.BOTH)


def render_footer(parent):
    button_random = tk.Button(parent, text="Generate first part", 
                              font=("", 14))
    lbl_part = tk.Label(parent, text="Entry first part:", 
                        font=("", 14), bg="#D11EB9")
    entry_part = tk.Entry(parent, font=("", 14))
    lbl_key = tk.Label(parent, text=f"key:-", 
                       font=("", 14), bg="#D11EB9")
    button_gen = tk.Button(parent, text="Generate key", font=("", 14), 
                               command=lambda: generate_key(entry_part, lbl_key))

    lbl_key.pack(side=tk.BOTTOM, fill=tk.X)
    entry_part.pack(side=tk.BOTTOM, fill=tk.X)
    lbl_part.pack(side=tk.BOTTOM, fill=tk.X)
    button_gen.pack(side=tk.LEFT, fill=tk.X, expand=True)
    button_random.pack(side=tk.RIGHT, fill=tk.X)


def generate_key(entry, lbl):
    part_one = entry.get()
    if check_entry(part_one):
        part_two = generate_part(part_one, 3)
        part_three = generate_part(part_one, -5)
        key = f'{part_one}-{part_two}-{part_three}'
    else:
        key = 'Wrong first part'
    lbl.config(text=f'key:{key}')


def generate_part(original_part, right_shift):
    new_part = ''
    for letter in original_part:
        new_index = ALP.index(letter) + right_shift
        if new_index <= len(ALP):
            new_part += ALP[new_index]
        else:
            new_part += ALP[new_index - len(ALP)]
    return new_part


def check_entry(entry):
    if len(entry) != 5:
        return False
    for letter in entry:
        if letter not in ALP:
            break
    else:
        return True
    return False


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(f'{SIZE}x{SIZE}')
    root.title('gtaVI_freekeys.com')
    img = tk.PhotoImage(file='main_bg.png')
    img = img.subsample(2, 2)
    render_frames(root, img)
    root.mainloop()
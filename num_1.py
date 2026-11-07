import tkinter as tk
import random
import winsound

SIZE = 500
ALP = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY_PART_LENGHT = 5
KEY_PART_COUNT = 3
KEY_PART_SHIFTS = [3, -5]


key = '-'
pos = 0


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
    lbl_part = tk.Label(parent, text="Enter first part:", 
                        font=("", 14), bg="#D11EB9")
    entry_part = tk.Entry(parent, font=("", 14))
    lbl_key = tk.Label(parent, text=f"key:-", 
                       font=("", 14), bg="#D11EB9")
    button_random = tk.Button(parent, text="Generate first part", font=("", 14),
                               command=lambda: generate_first_part(entry_part))
    button_gen = tk.Button(parent, text="Generate key", font=("", 14), 
                               command=lambda: generate_key(entry_part))

    lbl_key.pack(side=tk.BOTTOM, fill=tk.X)
    entry_part.pack(side=tk.BOTTOM, fill=tk.X)
    lbl_part.pack(side=tk.BOTTOM, fill=tk.X)
    button_gen.pack(side=tk.LEFT, fill=tk.X, expand=True)
    button_random.pack(side=tk.RIGHT, fill=tk.X)

    animate(parent, lbl_key)


def generate_key(entry):
    global key, pos
    pos = 0

    part_one = entry.get()
    if check_entry(part_one):
        key = str(part_one)
        for part_num in range(KEY_PART_COUNT-1):
            part = generate_part(part_one, KEY_PART_SHIFTS[part_num])
            key += f'-{part}'
    else:
        key = 'Wrong first part'


def generate_part(original_part, right_shift):
    new_part = ''
    for letter in original_part:
        new_index = ALP.index(letter) + right_shift
        if new_index < len(ALP):
            new_part += ALP[new_index]
        else:
            new_part += ALP[new_index - len(ALP)]
    return new_part


def check_entry(entry):
    if len(entry) != KEY_PART_LENGHT:
        return False
    for letter in entry:
        if letter not in ALP:
            break
    else:
        return True
    return False


def generate_first_part(entry):
    first_part = ''
    for i in range(KEY_PART_LENGHT):
        first_part += ALP[random.randint(0, len(ALP) - 1)]
    entry.delete(0, tk.END)
    entry.insert(0, first_part)


def animate(parent, lbl):
    global key, pos

    if pos < len(key):
        pos += 1

    cur_key = key[:pos]

    lbl.config(text=f'key:{cur_key}')

    parent.after(100, lambda: animate(parent, lbl))


if __name__ == '__main__':
    winsound.PlaySound("Tom_Petty_-_Love_Is_A_Long_Road.wav", 
                       winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

    root = tk.Tk()
    root.geometry(f'{SIZE}x{SIZE}')
    root.title('gtaVI_freekeys.com')

    img = tk.PhotoImage(file='main_bg.png')
    img = img.subsample(2, 2)
    render_frames(root, img)

    root.mainloop()
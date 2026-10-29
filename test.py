import tkinter as tk
import random
import chat
import threading


SIZE = 500
OFFSET = 2
history = []


def render_frames(parent):
    header = tk.Frame(parent, bg="#ad3030")
    footer = tk.Frame(parent, bg="#612d2d")
    body = tk.Frame(parent)

    header.pack(side=tk.TOP, fill=tk.X)
    footer.pack(side=tk.BOTTOM, fill=tk.X)
    body.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    entry_name = render_header(header)
    render_footer(footer, body, entry_name)
    return body


def render_header(parent):
    lbl_name = tk.Label(parent, text="Name: ", font=("", 14))
    lbl_name.pack(side=tk.LEFT)
    entry_name = tk.Entry(parent, font=("", 14))
    entry_name.pack(side=tk.LEFT)

    name_default = f"Kotik-{random.randint(0, 1000)}"
    entry_name.insert(0, name_default)

    return entry_name


def send_msg(body, entry_msg, entry_name):
    msg_text = entry_msg.get()
    name = entry_name.get()
    msg = f"{name}:\n{msg_text}"
    entry_msg.delete(0, tk.END)
    # send
    chat.send_message(msg)
    # render_msg(body, msg)


def render_msg(body, msg):
    lbl_msg = tk.Label(body, text=msg, bg="#6fd455", 
                       padx=OFFSET, pady=OFFSET, 
                       font=("", 14), wraplength=450)
    lbl_msg.pack(side=tk.TOP, anchor=tk.NE, pady=OFFSET)
    history.append(lbl_msg)

    height = 0
    for msg in history:
        msg_height = msg.winfo_reqheight()
        height += msg_height + OFFSET

    if height > body.winfo_height():
        old_msg = history.pop(0)
        height -= (old_msg.winfo_reqheight() + OFFSET)
        old_msg.destroy()
        root.update_idletasks()


def render_footer(parent, body, entry_name):
    entry_message = tk.Entry(parent, font=("", 14))
    entry_message.pack(side=tk.LEFT, fill=tk.X, expand=True)
    btn_send = tk.Button(parent, text="Send", font=("", 14), 
                         command=lambda: send_msg(body, entry_message, entry_name))
    btn_send.pack(side=tk.RIGHT)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(f'{SIZE}x{SIZE}')
    root.title('Viber')
    body = render_frames(root)
    threading.Thread(target=chat.read_msgs, args=(render_msg, body), daemon=True).start()
    root.mainloop()
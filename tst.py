import tkinter as tk

root = tk.Tk()
c = tk.Canvas(root, width=300, height=100)
c.pack()
ball = c.create_oval(0, 25, 50, 75, fill="blue")

def animate():
    c.move(ball, 5, 0)  # Сдвиг на 5 пикселей
    root.after(33, animate) # Повторный вызов через 33 мс (~30 FPS)

animate() # Запуск анимации
root.mainloop()
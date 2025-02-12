import tkinter as tk
from tkinter import messagebox, Toplevel
import random
import os

def choose_gender(selected_gender):
    if selected_gender == "тян":
        messagebox.showerror("Что с ебалом?", "Пидор невыебуйся, выбирай нормально")
    else:
        show_choice_screen()

def show_choice_screen():
    clear_window()
    tk.Label(root, text="С кем хочешь провести День святого Валентина?",
             font=("Arial", 16), fg="#ffb6c1", bg="#ff1493").pack(pady=30)

    tk.Button(root, text="С тянкой", font=("Arial", 14), fg="white", bg="#db7093",
              width=15, height=2, command=break_program).pack(pady=10)

    global boy_btn
    boy_btn = tk.Button(root, text="с мужланом?(фу)", font=("Arial", 14), fg="white", bg="#db7093",
                        width=15, height=2)
    boy_btn.pack(pady=10)
    boy_btn.bind("<Enter>", lambda event: move_button(boy_btn))

def break_program():
    for _ in range(20):
        popup = Toplevel(root)
        popup.title("🍑🍑🍑")
        popup.geometry(f"200x100+{random.randint(100, 800)}+{random.randint(100, 600)}")
        popup.configure(bg="black")
        tk.Label(popup, text="GAY AS FUCK", font=("Arial", 12), fg="white", bg="black").pack(pady=10)
        tk.Button(popup, text="иди нахуй)))", command=popup.destroy, fg="white", bg="#db7093").pack()
    root.after(1000, lambda: os._exit(5)) # закроется через 5 сек

def move_button(button):
    new_x = random.randint(50, 400)
    new_y = random.randint(200, 450)
    button.place(x=new_x, y=new_y)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# главное окошко
root = tk.Tk()
root.title("День святого ПИДОРАСА")
root.geometry("450x450")
root.configure(bg="#ff1493")

# центрируем
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# координаты для центрирования
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# основной интерфейс
tk.Label(root, text="Твой гендер:", font=("Arial", 16), fg="#ffb6c1", bg="#ff1493").pack(pady=30)
tk.Button(root, text="мужлан", font=("Arial", 14), fg="white", bg="#db7093",
          width=15, height=2, command=lambda: choose_gender("мужлан")).pack(pady=10)
tk.Button(root, text="тян", font=("Arial", 14), fg="white", bg="#db7093",
          width=15, height=2, command=lambda: choose_gender("тян")).pack(pady=10)

root.mainloop()

import tkinter as tk

window = tk.Tk()

window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

label = tk.Label(window, text='Hello', font=("Arial Bold", 50) )
label.grid(column=0, row=0)


def buton_click():
    print(f'Ai')


btn1 = tk.Button(window, text="Don't click", command=lambda: buton_click())
btn1.grid(column=1, row=0)

window.mainloop()
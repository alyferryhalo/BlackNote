from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import tkinter as tk


def setting_window():
    win_settings = Toplevel(window)
    win_settings.title('BlackNote: Настройки')
    win_settings.geometry('380x240')
    win_settings["bg"] = "black"
    win_settings.iconphoto(False, tk.PhotoImage(file="icon.png"))

    text_use = Label(win_settings, text="Выберите и закройте окно", font=6, bg='black', fg='#8f8483')
    text_use.grid(column=0, row=1)

    text_style = Label(win_settings, text='Шрифт', font=6, bg='black', fg='#8f8483')
    text_style.grid(column=0, row=2)

    fontdict = {
        'Arial': ('Arial', 16),
        'Times New Roman': ('Times', 16),
        'Calibri': ('Calibri', 16),
        'Courier': ('Courier', 16),
    }

    var_font = StringVar()
    combo_style = Combobox(win_settings, values=list(fontdict.keys()), justify="center", textvariable=var_font)
    combo_style.bind('<<ComboboxSelected>>', lambda event: textbox.config(font=fontdict[var_font.get()]))
    combo_style.grid(column=1, row=2)
    combo_style.current(0)

    text_color = Label(win_settings, text='Цвет', font=6, bg='black', fg='#8f8483')
    text_color.grid(column=0, row=3)

    colordict = {
        'Белый': 'white',
        'Светло-серый': '#e3e8e5',
        'Тёмно-серый': '#8f8483',
        "Жёлтый": 'yellow',
        'Зелёный': 'green',
        'Голубой': 'blue',
        'Красный': 'red'}

    var_color = StringVar()
    combo_color = Combobox(win_settings, values=list(colordict.keys()), justify="center", textvariable=var_color)
    combo_color.bind('<<ComboboxSelected>>', lambda event: textbox.config(fg=colordict[var_color.get()]))
    combo_color.grid(column=1, row=3)
    combo_color.current(2)


def load_file():
    fn = filedialog.Open(window, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def save_file():
    fn = filedialog.SaveAs(window, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))


def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()


window = Tk()
window.title('BlackNote 1.0')
window.geometry('900x500')
window["bg"] = "black"
window.iconphoto(False, tk.PhotoImage(file="icon.png"))
window.bind('<Button-3>', do_popup)

popup = Menu(window, tearoff=0)
popup.add_command(label="Скопировать")
popup.add_separator()
popup.add_command(label="Вставить")

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
menu.add_cascade(label='Файл', menu=new_item)
new_item.add_command(label='Загрузить', command=load_file)
new_item.add_separator()
new_item.add_command(label='Сохранить', command=save_file)
new_item.add_separator()
new_item.add_command(label='Настройки', command=setting_window)
window.config(menu=menu)

textFrame = Frame(window, height=340, width=600, bg='black')
textFrame.pack(side='bottom', fill='both', expand=1)
textbox = Text(textFrame, font=('Arial', 16), wrap='word', bg='black', fg="#8f8483")

scrollbar = Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

window.mainloop()

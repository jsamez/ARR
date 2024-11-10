
import tkinter as tk
from tkinter import messagebox, Listbox, Toplevel, Button, Scrollbar, END, Text

def display_message(title, message):
    msg_dialog = Toplevel()
    msg_dialog.title(title)
    text_widget = Text(msg_dialog, wrap=tk.WORD)
    text_widget.insert(tk.END, message)
    text_widget.config(state=tk.DISABLED)
    scrollbar = Scrollbar(msg_dialog, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    Button(msg_dialog, text="확인", command=msg_dialog.destroy).pack()

def get_user_input(recommended_recipes, root):
    input_dialog = Toplevel(root)
    input_dialog.title("추천 요리 선택")

    scrollbar = Scrollbar(input_dialog)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = Listbox(input_dialog, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set)
    for recipe in recommended_recipes:
        listbox.insert(END, recipe)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    def on_select():
        selected_index = listbox.curselection()
        if selected_index:
            selected_recipe = listbox.get(selected_index)
            input_dialog.selected_recipe = selected_recipe
            input_dialog.destroy()

    Button(input_dialog, text="선택", command=on_select).pack()
    root.wait_window(input_dialog)
    return getattr(input_dialog, 'selected_recipe', None)
    
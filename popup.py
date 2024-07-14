import tkinter as tk
from tkinter import messagebox

def show_popup():
    messagebox.showinfo("Alerta", "Noticia Urgente!")

root = tk.Tk()
root.withdraw()

show_popup()

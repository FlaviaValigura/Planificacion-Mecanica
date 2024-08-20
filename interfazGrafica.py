import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Abrir archivo txt"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Archivo txt abierto - {filepath}")

def save_file():
    """Guardar como txt."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Archivo txt - {filepath}")

window = tk.Tk()
window.title("OFICINA DE PLANIFICACIÓN - COORDINACIÓN MECÁNICA")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Abrir", command=open_file)
btn_save = tk.Button(frm_buttons, text="Guardar", command=save_file)
btn_sector = tk.Button(frm_buttons, text="Sector")
btn_planilla = tk.Button(frm_buttons, text="Planilla")

btn_open.grid(row=0, column=0, padx=5, pady=5)
btn_save.grid(row=1, column=0, padx=5, pady=5)
btn_sector.grid(row=2, column=0, padx=5, pady=5)
btn_planilla.grid(row=4, column=0, padx=5, pady=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

"""
UN TITOLO DESCRITTIVO.

Versione Azzurra: 1.0.1
Versione Python richiesta: 3.10+
Richiede: - Tcl/Tk
          - Librerie standard Python
"""

import tkinter as tk
from tkinter import messagebox
import platform

"""
Font
"""
if platform.system() == "Windows":
    window_font = "Arial"
elif platform.system() == "Linux":
    window_font = "DejaVu Sans"
else:
    window_font = None

"""
Variabili
"""
azzurra_version = "1.0.1"

"""
Finestra
"""
window = tk.Tk()
window.geometry("600x600")
window.title(f"Strumentary - Azzurra {azzurra_version}")

"""
Funzioni
"""
def open_strumentary():
    import strumentary


"""
Elementi GUI
"""
home_label = tk.Label(window, text="Strumentary", font=(window_font, 15))
home_label.pack()

s_button = tk.Button(window, text="Inizzializza", command=lambda: messagebox.showinfo("Strumentary è in sviluppo."))
s_button.pack()


"""
Avvio
"""
window.mainloop()

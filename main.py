"""
UN TITOLO DESCRITTIVO.

Versione Azzurra: 1.0.0
Versione Python richiesta: 3.10+
Richiede: - Tcl/Tk
          - Librerie standard Python
"""

import tkinter as tk
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
azzurra_version = "1.0.0"

"""
Finestra
"""
window = tk.Tk()
window.geometry("600x600")
window.title(f"Azzurra {azzurra_version}")

"""
Funzioni
"""
def open_strumentary():
    import strumentary


"""
Elementi GUI
"""
home_label = tk.Label(window, text="Azzurra", font=(window_font, 15))
home_label.pack()

s_button = tk.Button(window, text="Strumentary", command=open_strumentary)
s_button.pack()


"""
Avvio
"""
if __name__ == "__main__":
    window.mainloop()

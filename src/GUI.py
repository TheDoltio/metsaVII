import tkinter as tk
from tkinter import ttk
import json

from gui_templates import header
from gui_templates import escaramujo

# ---------------- Configuración ----------------
VERSION = "0.1"
ESCARAMUJO_JSON_PATH = "../src/data_monitor/escaramujo_data.json"
UPDATE_INTERVAL = 60_000  # ms

# ---------------- Ventana principal ----------------
root = tk.Tk()
root.title(f"metsaVII – v{VERSION}")
root.geometry("950x420")

# Layout base
for col in range(5):
    root.columnconfigure(col, weight=1)

# ---------------- Datos compartidos ----------------
shared_data_escaramujo = {}

def update_escaramujo():
    try:
        with open(ESCARAMUJO_JSON_PATH, "r") as f:
            shared_data_escaramujo.clear()
            shared_data_escaramujo.update(json.load(f))
    except Exception as e:
        # si el JSON falla, no matamos la UI
        print("Error leyendo JSON:", e)

    root.after(UPDATE_INTERVAL, update_escaramujo)

# Arranca el updater global
update_escaramujo()

# ---------------- Bloques GUI ----------------

head = header.header(VERSION, root)

escaramujo.escaramujo(
    i=head,
    root=root,
    data_ref=shared_data_escaramujo,
    update_interval=UPDATE_INTERVAL
)

# ---------------- Mainloop ----------------
root.mainloop()


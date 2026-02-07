import tkinter as tk
from tkinter import ttk
import json

version = "0.1"
JSON_PATH = "src/data_monitor/escaramujo_data.json"
UPDATE_INTERVAL = 60_000  # 60 s en ms

# ---------------- Ventana principal ----------------
root = tk.Tk()
root.title(f"metsaVII – v{version}")
root.geometry("850x320")

# ---------------- Fuentes ----------------
title_font = ("Helvetica", 16, "bold")
header_font = ("Helvetica", 12, "bold")
value_font = ("Helvetica", 14)

# ---------------- METSA Header ----------------

header_frame = tk.Frame(root)
header_frame.grid(
    row=0,
    column=0,
    columnspan=5,
    sticky="w",
    padx=20,
    pady=(10, 2)
)


title_font_big = ("Helvetica", 24, "bold")
subtitle_font = ("Helvetica", 14, "bold")

# Colores por letra de "metsa"
metsa_letters = [
    ("m", "#fff700"),   # rojo
    ("e", "#e38800"),   # azul0
    ("t", "#e30000"),   # verde
    ("s", "#89009e"),   # naranja
    ("a", "#00129e"),   # morado
    ("V", '#2f8700'),
    ("II", '#ffffff')
]

# METSA coloreado
for char, color in metsa_letters:
    tk.Label(
        header_frame,
        text=char,
        fg=color,
        font=title_font_big
    ).pack(side="left")

# Espacio + versión
tk.Label(
    header_frame,
    text=f" v{version}",
    fg="black",
    font=("Helvetica", 20, 'bold')
).pack(side="left", padx=(8, 0))

# ---------------- Subtítulo ----------------
subtitle_label = tk.Label(
    root,
    text="Monitoreando Escaramujo en Telemetría y eStatus con Automatización",
    font=subtitle_font,
    fg="black",
    anchor="w",
    justify="left"
)
subtitle_label.grid(
    row=1,
    column=0,
    columnspan=5,
    sticky="w",
    padx=20,
    pady=(0, 6)
)

separator = ttk.Separator(root, orient="horizontal")
separator.grid(
    row=2,
    column=0,
    columnspan=5,
    sticky="ew",
    padx=20,
    pady=(0, 15)
)


# ---------------- Título ----------------
title_label = ttk.Label(
    root,
    text="Fluencia actual",
    font=title_font,
    anchor="center"
)
title_label.grid(row=3, column=0, columnspan=5, pady=15)

# ---------------- Encabezados ----------------
column_titles = [
    "Canal 0",
    "Canal 1",
    "Canal 2",
    "Canal 3",
    "Coincidencias"
]

for col, title in enumerate(column_titles):
    lbl = ttk.Label(
        root,
        text=title,
        font=header_font,
        anchor="center"
    )
    lbl.grid(row=4, column=col, padx=20, pady=5)

# ---------------- Contenedores blancos ----------------
value_labels = []

for col in range(5):
    frame = tk.Frame(
        root,
        background="white",
        relief="solid",
        borderwidth=1
    )
    frame.grid(row=5, column=col, padx=20, pady=10, sticky="nsew")

    label = tk.Label(
        frame,
        text="--",
        font=value_font,
        background="white",
        width=10,
        anchor="center"
    )
    label.pack(padx=10, pady=10)

    value_labels.append(label)

# Ajuste de columnas
for col in range(5):
    root.columnconfigure(col, weight=1)

# ---------------- Actualización desde JSON ----------------
def update_values():
    with open(JSON_PATH, "r") as f:
        data = json.load(f)

    value_labels[0].config(text=str(data["ch0"]))
    value_labels[1].config(text=str(data["ch1"]))
    value_labels[2].config(text=str(data["ch2"]))
    value_labels[3].config(text=str(data["ch3"]))
    value_labels[4].config(text=str(data["C"]))

    root.after(UPDATE_INTERVAL, update_values)

# Primera lectura
update_values()

root.mainloop()


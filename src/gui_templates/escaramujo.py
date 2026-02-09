import tkinter as tk
from tkinter import ttk

def escaramujo(i, root, data_ref, update_interval):
    COMMON_PADX = 20

    # ---------- Fuerzas de columnas (CLAVE) ----------
    for col in range(5):
        root.columnconfigure(col, weight=1, uniform="escaramujo")

    fuente_ID = ("Helvetica", 16, "bold")
    fuente_titulo = ("Helvetica", 16, "bold")
    fuente_name_canales = ("Helvetica", 12, "bold")
    fuente_valores = ("Helvetica", 14)
    fuente_estatus = ("Helvetica", 12, "bold")

    ID_label = ttk.Label(
        root,
        text="ID de adquisición: --",
        font=fuente_ID
    )
    ID_label.grid(
        row=i + 1, column=0, columnspan=5,
        sticky="w", padx=COMMON_PADX, pady=5
    )

    separator = ttk.Separator(root, orient="horizontal")
    separator.grid(
        row=i+2,
        column=0,
        columnspan=5,
        sticky="ew",
        padx=20,
        pady=(0, 15)
    )


    title_label = ttk.Label(
        root,
        text="Conteo actual de eventos",
        font=fuente_titulo
    )
    title_label.grid(
        row=i + 3, column=0, columnspan=5,
        sticky="w", padx=COMMON_PADX, pady=5
    )

    column_titles = [
        "Canal 0", "Canal 1", "Canal 2", "Canal 3", "Coincidencias"
    ]

    for col, title in enumerate(column_titles):
        ttk.Label(
            root,
            text=title,
            font=fuente_name_canales,
            anchor="center"
        ).grid(row=i + 4, column=col, padx=COMMON_PADX, pady=5, sticky="ew")

    value_labels = []

    for col in range(5):
        frame = tk.Frame(
            root,
            background="white",
            relief="solid",
            borderwidth=1
        )
        frame.grid(
            row=i + 5, column=col,
            padx=COMMON_PADX,
            sticky="nsew"
        )

        label = tk.Label(
            frame,
            text="--",
            font=fuente_valores,
            background="white",
            anchor="center"
        )
        label.pack(expand=True, fill="both", padx=10, pady=10)

        value_labels.append(label)

    read_label = ttk.Label(
        root,
        text="Última lectura (UTC):",
        font=fuente_titulo
    )
    read_label.grid(
        row=i + 6, column=2, columnspan=2,
        sticky="e", padx=COMMON_PADX, pady=(25, 0)
    )

    read_data_label = ttk.Label(
        root,
        text="--",
        font=fuente_valores
    )
    read_data_label.grid(
        row=i + 6, column=4,
        sticky="e", padx=COMMON_PADX, pady=(25, 0)
    )

    update_label = ttk.Label(
        root,
        text="Última actualización (UTC):",
        font=fuente_titulo
    )
    update_label.grid(
        row=i + 7, column=2, columnspan=2,
        sticky="e", padx=COMMON_PADX
    )

    update_data_label = ttk.Label(
        root,
        text="--",
        font=fuente_valores
    )
    update_data_label.grid(
        row=i + 7, column=4,
        sticky="e", padx=COMMON_PADX
    )

    status_label = ttk.Label(
        root,
        text="Estado",
        font=fuente_name_canales
    )
    status_label.grid(
        row=i + 6, column=1,
        padx=COMMON_PADX, pady=(22, 0)
    )
    
    median_label = ttk.Label(
        root,
        text="      Mediana de\nlas coincidencias",
        font=fuente_name_canales
    )
    median_label.grid(
        row=i+6, column=0,
        padx=COMMON_PADX, pady=(12, 0)
    )    

    # Mediana de las coincidencias
    median_frame = tk.Frame(
        root,
        background="white",
        relief="solid",
        borderwidth=1
    )
    median_frame.grid(
        row=i+7, column=0,
        padx=COMMON_PADX,
        sticky="nsew"    
    )
    median = tk.Label(
        median_frame,
        text="--",
        font=fuente_valores,
        bg="white",
        anchor="center"
    )
    median.pack(expand=True, fill="both", padx=10, pady=10)

    # Reporte de estatus
    status_frame = tk.Frame(
        root,
        background="yellow",
        relief="solid",
        borderwidth=1
    )
    status_frame.grid(
        row=i + 7, column=1,
        padx=COMMON_PADX,
        sticky="nsew"
    )

    status = tk.Label(
        status_frame,
        text="INICIALIZANDO",
        font=fuente_estatus,
        bg="yellow",
        anchor="center"
    )
    status.pack(expand=True, fill="both", padx=10, pady=10)

    def refresh():
        ID_label.config(
            text=f"ID de adquisición: {data_ref.get('ID', '--')}"
        )

        update_data_label.config(
            text=data_ref.get("refresh", "--")
        )

        read_data_label.config(
            text=f"{data_ref.get('date', '--')} {data_ref.get('utc', '--')}"
        )

        value_labels[0].config(text=data_ref.get("ch0", "--"))
        value_labels[1].config(text=data_ref.get("ch1", "--"))
        value_labels[2].config(text=data_ref.get("ch2", "--"))
        value_labels[3].config(text=data_ref.get("ch3", "--"))
        value_labels[4].config(text=data_ref.get("C", "--"))
        median.config(text=data_ref.get("median", "--"))

        if data_ref.get("status") == "OPERATIVO":
            status_frame.config(background="lime")
            status.config(text="OPERATIVO", bg="lime", fg="black")
        else:
            status_frame.config(background="red")
            status.config(text=data_ref.get("status", "--"), bg="red", fg="yellow")

        root.after(update_interval, refresh)

    refresh()


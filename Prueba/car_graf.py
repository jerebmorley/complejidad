import tkinter as tk
from tkinter import messagebox, ttk
import time
import threading

# ---------- Funciones matemáticas ----------
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def potencia_mod(a, b, mod):
    resultado = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            resultado = (resultado * a) % mod
        a = (a * a) % mod
        b //= 2
    return resultado

def criba_primos(hasta):
    primos = [True] * (hasta + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(hasta ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, hasta + 1, i):
                primos[j] = False
    return primos

def es_carmichael(n):
    for a in range(2, n):
        if gcd(a, n) == 1:
            if potencia_mod(a, n - 1, n) != 1:
                return False
    return True

def buscar_carmichael_con_progreso(inicio, fin, progreso_callback):
    primos = criba_primos(fin)
    resultado = []
    total = fin - inicio + 1
    procesados = 0

    for n in range(inicio, fin + 1):
        if not primos[n]:
            if es_carmichael(n):
                resultado.append(n)
        procesados += 1
        progreso_callback(int((procesados / total) * 100))

    return resultado

# ---------- Función que ejecuta la búsqueda en un hilo ----------
def ejecutar_busqueda():
    try:
        inicio = int(entry_inicio.get())
        fin = int(entry_fin.get())

        if inicio >= fin or inicio < 2:
            raise ValueError

        progress_bar["value"] = 0
        output_text.delete("1.0", tk.END)
        btn_buscar.config(state="disabled")
        output_text.insert(tk.END, "Buscando números de Carmichael... esto puede tardar unos segundos/minutos.\n\n")

        def run():
            t0 = time.time()
            resultado = buscar_carmichael_con_progreso(inicio, fin, lambda p: progress_bar.after(0, progress_bar.config, {'value': p}))
            t1 = time.time()

            resultado_text = (
                f"⏱ Tiempo de ejecución: {t1 - t0:.3f} segundos\n\n"
                f"🔢 Números de Carmichael encontrados:\n{resultado if resultado else 'Ninguno encontrado.'}"
            )

            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, resultado_text)
            btn_buscar.config(state="normal")

        threading.Thread(target=run).start()

    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese valores enteros válidos y coherentes.")

# ---------- Interfaz gráfica ----------
ventana = tk.Tk()
ventana.title("Buscador de Números de Carmichael")

# Introducción
intro = (
    "🔍 ¿Qué son los números de Carmichael?\n\n"
    "Son números compuestos que cumplen con una propiedad similar a la del pequeño teorema de Fermat:\n"
    "Para todo entero a coprimo con n, se cumple a^(n-1) ≡ 1 mod n.\n\n"
    "Se utilizan en criptografía como ejemplos de falsos positivos en tests de primalidad.\n"
)

tk.Label(ventana, text=intro, justify="left", wraplength=500, padx=10, pady=10).pack()

# Entradas
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=5)

tk.Label(frame_entrada, text="Número inicial:").grid(row=0, column=0, padx=5, pady=5)
entry_inicio = tk.Entry(frame_entrada, width=10)
entry_inicio.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="Número final:").grid(row=0, column=2, padx=5)
entry_fin = tk.Entry(frame_entrada, width=10)
entry_fin.grid(row=0, column=3, padx=5)

btn_buscar = tk.Button(ventana, text="Buscar números de Carmichael", command=ejecutar_busqueda)
btn_buscar.pack(pady=10)

# Barra de progreso
progress_bar = ttk.Progressbar(ventana, length=400, mode="determinate")
progress_bar.pack(pady=5)

# Salida
output_text = tk.Text(ventana, height=15, width=70)
output_text.pack(padx=10, pady=10)

# Ejecutar la interfaz
ventana.mainloop()

import requests
import time
import tkinter as tk
import socket
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Variables globales para almacenar los datos de las gráficas
download_speeds = []
upload_speeds = []
ping_times = []

# Función para medir el ping
def test_ping(host="8.8.8.8", port=80, timeout=2):
    try:
        start_time = time.time()
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        end_time = time.time()
        ping_time = (end_time - start_time) * 1000  # Convertir a milisegundos
        return ping_time
    except Exception as e:
        return None

# Función para medir la velocidad de descarga
def test_download_speed():
    url = "https://speed.hetzner.de/10MB.bin"  # Enlace a un archivo de 10 MB
    file_size = 10 * 1024 * 1024  # 10 MB en bytes
    
    start_time = time.time()  # Tiempo de inicio
    response = requests.get(url, stream=True)
    
    total_downloaded = 0
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            total_downloaded += len(chunk)
    
    end_time = time.time()  # Tiempo de fin

    duration = end_time - start_time
    download_speed = (file_size / duration) / 10**6  # Velocidad en Mbps
    return download_speed

# Función para medir la velocidad de subida
def test_upload_speed():
    url = "http://www.google.com"  # Se usa una URL como referencia
    data = b'x' * 1024 * 1024  # Datos de 1 MB
    
    start_time = time.time()
    response = requests.post(url, data=data)
    end_time = time.time()

    duration = end_time - start_time
    upload_speed = (len(data) / duration) / 10**6  # Convertir a Mbps
    return upload_speed

# Función para actualizar los resultados y gráficos en tiempo real
def update_results():
    # Obtener y mostrar la velocidad de descarga
    download_speed = test_download_speed()
    download_label.config(text=f"Descarga (Mbps): {download_speed:.2f}")
    download_speeds.append(download_speed)

    # Obtener y mostrar la velocidad de subida
    upload_speed = test_upload_speed()
    upload_label.config(text=f"Subida (Mbps): {upload_speed:.2f}")
    upload_speeds.append(upload_speed)

    # Obtener y mostrar el ping
    ping_time = test_ping()
    if ping_time is not None:
        ping_label.config(text=f"Ping (ms): {ping_time:.2f}")
        ping_times.append(ping_time)
    else:
        ping_label.config(text="Ping: Error")

    # Limitar los datos a los últimos 20 valores para no sobrecargar las gráficas
    if len(download_speeds) > 20:
        download_speeds.pop(0)
    if len(upload_speeds) > 20:
        upload_speeds.pop(0)
    if len(ping_times) > 20:
        ping_times.pop(0)

    # Actualizar las gráficas
    update_graphs()

    # Volver a ejecutar la prueba después de 2 segundos (2000 ms)
    root.after(2000, update_results)

# Función para actualizar los gráficos
def update_graphs():
    # Limpiar y redibujar las gráficas
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # Gráfica de velocidad de descarga
    ax1.plot(download_speeds, label="Descarga (Mbps)", color="blue")
    ax1.set_title("Velocidad de Descarga")
    ax1.set_ylim(0, max(download_speeds) * 1.2 if download_speeds else 0)  # Evitar error si la lista está vacía

    # Gráfica de velocidad de subida
    ax2.plot(upload_speeds, label="Subida (Mbps)", color="green")
    ax2.set_title("Velocidad de Subida")
    ax2.set_ylim(0, max(upload_speeds) * 1.2 if upload_speeds else 0)  # Evitar error si la lista está vacía

    # Gráfica de ping
    ax3.plot(ping_times, label="Ping (ms)", color="red")
    ax3.set_title("Ping")
    ax3.set_ylim(0, max(ping_times) * 1.2 if ping_times else 0)  # Evitar error si la lista está vacía

    # Actualizar el canvas con las nuevas gráficas
    canvas.draw()

# Crear la ventana principal
root = tk.Tk()
root.title("Test de Velocidad WiFi - Optimización para Juegos")

# Crear etiquetas para mostrar los resultados
download_label = tk.Label(root, text="Descarga (Mbps): ---")
download_label.pack(pady=10)

upload_label = tk.Label(root, text="Subida (Mbps): ---")
upload_label.pack(pady=10)

ping_label = tk.Label(root, text="Ping (ms): ---")
ping_label.pack(pady=10)

# Crear la figura de matplotlib para las gráficas
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(5, 8))

# Insertar la figura en tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Iniciar la primera actualización de resultados
update_results()

# Iniciar el loop de la ventana
root.mainloop()
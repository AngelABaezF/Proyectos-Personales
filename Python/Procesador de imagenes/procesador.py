# Angel Alexander Baez Flores - A01425613 
# Osmar Enrique Sanches Martinez - A01425521 
# Angel Emiliano Vargas Carreto - A01425478

import cv2
import tkinter as tk
from tkinter import filedialog, font, ttk, messagebox
from PIL import Image, ImageTk
import os
import numpy

class ImageProcessorApp:
    image = None
    original_image = None
    file_path = None

    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de Imágenes")

        # Definición de colores inspirados en Tron
        tron_blue = "#6ff9ff"
        tron_light_blue = "#6ff9ff"
        tron_dark_blue = "#6ff9ff"
        tron_gray = "black"
        tron_light_gray = "black"

        # Estilo personalizado para botones
        style = ttk.Style()
        style.configure('TButton', foreground='blue', background='black', bordercolor='blue', relief='raised')

        # Configuración del fondo de la ventana
        root.configure(bg="black")

        # Configuración de columnas y filas para que se expandan
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        frame_left = tk.Frame(root)
        frame_left.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)

        y_scrollbar = tk.Scrollbar(frame_left, orient="vertical")
        y_scrollbar.pack(side="right", fill="y")

        x_scrollbar = tk.Scrollbar(frame_left, orient="horizontal")
        x_scrollbar.pack(side="bottom", fill="x")

        # Canvas para la imagen principal
        self.canvas = tk.Canvas(frame_left, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set, bd=2, relief="solid", bg="black", highlightbackground="#6ff9ff", highlightthickness=3)
        self.canvas.pack(expand=True, fill="both")
        self.canvas.bind("<Motion>", self.on_mouse_move)

        y_scrollbar.config(command=self.canvas.yview)
        x_scrollbar.config(command=self.canvas.xview)

        frame_right = tk.Frame(root, bg=tron_gray)  # Ajuste del color de fondo
        frame_right.grid(row=0, column=1, sticky="nsew", padx=25, pady=25)

        # Label para mostrar el nombre del archivo
        self.file_name_label = tk.Label(frame_right, text="", bg="black")
        self.file_name_label.grid(row=0, column=1, columnspan=2 , sticky="w", padx=25, pady=5)

        # Frame para mostrar la imagen original a una escala menor
        self.original_image_frame = tk.Frame(frame_right, bg=tron_gray, highlightbackground="#6ff9ff", highlightthickness=3) 
        self.original_image_frame.grid(row=2, column=0, columnspan=3, padx=25, pady=5)

        # Labels para los valores RGB
        self.red_label = tk.Label(frame_right, text="R", fg='#6ff9ff', font=("Arial", 12, "bold"), bg="black")
        self.red_label.grid(row=3, column=0, sticky="w", padx=25, pady=5)

        self.green_label = tk.Label(frame_right, text="G", font=("Arial", 12, "bold"), fg='#6ff9ff', bg="black")
        self.green_label.grid(row=3, column=1, sticky="w", padx=25, pady=5)

        self.blue_label = tk.Label(frame_right, text="B", font=("Arial", 12, "bold"), fg='#6ff9ff', bg="black")
        self.blue_label.grid(row=3, column=2, sticky="w", padx=25, pady=5)

        tk.Label(frame_right, text="", bg="black").grid(row=4, column=0, columnspan=3)  # Separación

        # Botones para aplicar filtros
        self.smooth_button = ttk.Button(frame_right, text="Suavizado", command=self.smooth_image, style='Custom.TButton')
        self.smooth_button.grid(row=5, column=0, sticky="ew", padx=25, pady=5)
        self.smooth_button.bind("<Enter>", lambda event, button=self.smooth_button: button.config(background='black', fg='#6ff9ff'))
        self.smooth_button.bind("<Leave>", lambda event, button=self.smooth_button: button.config(bg='black', fg='blue'))

        self.negative_button = ttk.Button(frame_right, text="Negativo", command=self.negative_filter, style='Custom.TButton')
        self.negative_button.grid(row=5, column=1, sticky="ew", padx=25, pady=5)
        self.negative_button.bind("<Enter>", lambda event, button=self.negative_button: button.config(bg='black', fg='#6ff9ff'))
        self.negative_button.bind("<Leave>", lambda event, button=self.negative_button: button.config(bg='black', fg='blue'))

        self.grayscale_button = ttk.Button(frame_right, text="Escala de grises", command=self.grayscale_image, style='Custom.TButton')
        self.grayscale_button.grid(row=5, column=2, sticky="ew", padx=25, pady=5)
        self.grayscale_button.bind("<Enter>", lambda event, button=self.grayscale_button: button.config(bg='black', fg='#6ff9ff'))
        self.grayscale_button.bind("<Leave>", lambda event, button=self.grayscale_button: button.config(bg='black', fg='blue'))

        self.binarize_button = ttk.Button(frame_right, text="Binarizado", command=self.binarize_image, style='Custom.TButton')
        self.binarize_button.grid(row=7, column=0, sticky="ew", padx=25, pady=5)
        self.binarize_button.bind("<Enter>", lambda event, button=self.binarize_button: button.config(bg='black', fg='#6ff9ff'))
        self.binarize_button.bind("<Leave>", lambda event, button=self.binarize_button: button.config(bg='black', fg='blue'))

        self.dynamic_binarize_button = ttk.Button(frame_right, text="Binarizado Dinámico", command=self.dynamic_binarize_image, style='Custom.TButton')
        self.dynamic_binarize_button.grid(row=7, column=1, sticky="ew", padx=25, pady=5)
        self.dynamic_binarize_button.bind("<Enter>", lambda event, button=self.dynamic_binarize_button: button.config(bg='black', fg='#6ff9ff'))
        self.dynamic_binarize_button.bind("<Leave>", lambda event, button=self.dynamic_binarize_button: button.config(bg='black', fg='blue'))

        self.filter_button = ttk.Button(frame_right, text="Bilateral", command=self.bilateral_filter, style='Custom.TButton')
        self.filter_button.grid(row=7, column=2, sticky="ew", padx=25, pady=5)
        self.filter_button.bind("<Enter>", lambda event, button=self.filter_button: button.config(bg='black', fg='#6ff9ff'))
        self.filter_button.bind("<Leave>", lambda event, button=self.filter_button: button.config(bg='black', fg='blue'))

        tk.Label(frame_right, text="", bg=tron_gray).grid(row=8, column=0, columnspan=3)  # Separación

        # Botones para aplicar distintos bordes
        self.border1_button = ttk.Button(frame_right, text="Sobel", command=self.sobel_edge_detection, style='Custom.TButton')
        self.border1_button.grid(row=9, column=0, sticky="ew", padx=25, pady=5)
        self.border1_button.bind("<Enter>", lambda event, button=self.border1_button: button.config(bg='black', fg='#6ff9ff'))
        self.border1_button.bind("<Leave>", lambda event, button=self.border1_button: button.config(bg='black', fg='blue'))

        self.border2_button = ttk.Button(frame_right, text="Prewit", command=self.prewit_edge_detection, style='Custom.TButton')
        self.border2_button.grid(row=9, column=1, sticky="ew", padx=25, pady=5)
        self.border2_button.bind("<Enter>", lambda event, button=self.border2_button: button.config(bg='black', fg='#6ff9ff'))
        self.border2_button.bind("<Leave>", lambda event, button=self.border2_button: button.config(bg='black', fg='blue'))
        
        self.delete_image_button = ttk.Button(frame_right, text="Delete", command=self.delete_image_confirmation, style='Custom.TButton')
        self.delete_image_button.grid(row=9, column=2, sticky="ew", padx=25, pady=5)
        self.delete_image_button.bind("<Enter>", lambda event, button=self.delete_image_button: button.config(bg='black', fg='#6ff9ff'))
        self.delete_image_button.bind("<Leave>", lambda event, button=self.delete_image_button: button.config(bg='black', fg='blue'))

        self.border3_button = ttk.Button(frame_right, text="Roberts", command=self.roberts_edge_detection, style='Custom.TButton')
        self.border3_button.grid(row=10, column=0, sticky="ew", padx=25, pady=5)
        self.border3_button.bind("<Enter>", lambda event, button=self.border3_button: button.config(bg='black', fg='#6ff9ff'))
        self.border3_button.bind("<Leave>", lambda event, button=self.border3_button: button.config(bg='black', fg='blue'))

        self.border4_button = ttk.Button(frame_right, text="Canny", command=self.canny_edge_detection, style='Custom.TButton')
        self.border4_button.grid(row=10, column=1, sticky="ew", padx=25, pady=5)
        self.border4_button.bind("<Enter>", lambda event, button=self.border4_button: button.config(bg='black', fg='#6ff9ff'))
        self.border4_button.bind("<Leave>", lambda event, button=self.border4_button: button.config(bg='black', fg='blue'))
        
        self.reset_image_button = ttk.Button(frame_right, text="Reset", command=self.reset_image_confirmation, style='Custom.TButton')
        self.reset_image_button.grid(row=10, column=2, sticky="ew", padx=25, pady=5)
        self.reset_image_button.bind("<Enter>", lambda event, button=self.reset_image_button: button.config(bg='black', fg='#6ff9ff'))
        self.reset_image_button.bind("<Leave>", lambda event, button=self.reset_image_button: button.config(bg='black', fg='blue'))
        
        tk.Label(frame_right, text="", bg=tron_gray).grid(row=11, column=0, columnspan=3)  # Separación

        # Canvas para la previsualización panorámica
        self.preview_canvas = tk.Canvas(frame_right, width=300, height=150, bd=2, relief="solid", bg="black", highlightbackground="#6ff9ff", highlightthickness=3)
        self.preview_canvas.grid(row=13, column=0, columnspan=3, padx=25, pady=5)

        # Label para indicar que es la previsualización actual
        self.actual_label = tk.Label(frame_right, text="Actual", font=("Arial", 12, "bold"), fg='#6ff9ff', bg="black")
        self.actual_label.grid(row=12, column=1)

        # Barra de progreso
        self.progress_bar = ttk.Progressbar(frame_right, orient='horizontal', length=300, mode='determinate', style='Horizontal.TProgressbar')
        self.progress_bar.grid(row=14, column=0, columnspan=3, padx=25, pady=5)

        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.load_image)
        file_menu.add_command(label="Save", command=self.save_image)

        menubar.add_cascade(label="File", menu=file_menu)

        root.config(menu=menubar)

    def change_button_color(self, event, button, bg_color, fg_color):
        button.config(bg=bg_color, fg=fg_color)

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Seleccionar Imagen", filetypes=[("Archivos PNG", "*.png"), ("Archivos JPG", "*.jpg"), ("Archivos JPEG", "*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.file_name_label.config(text="Archivo: " + os.path.basename(file_path), font=("Arial", 12, "bold"), fg='#6ff9ff', bg="black")
            self.image = cv2.imread(file_path)
            self.original_image = self.image.copy()
            self.display_image()
            if hasattr(self, 'original_image_label'):
                self.original_image_label.grid_forget()
            self.display_original_image()
            self.update_preview()

    def display_image(self):
        if self.image is not None:
            img_rgb = cv2.cvtColor(self.image.astype(numpy.uint8), cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.canvas.image = img_tk
            self.canvas.config(scrollregion=self.canvas.bbox("all")) 
            
    def display_original_image(self):
        if self.original_image is not None:
            scale_factor = min(1.0, 300.0 / self.original_image.shape[1], 200.0 / self.original_image.shape[0])
            resized_image = cv2.resize(self.original_image, (int(self.original_image.shape[1] * scale_factor), int(self.original_image.shape[0] * scale_factor)))
            img_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(img)
            self.original_image_label = tk.Label(self.original_image_frame, image=img_tk)
            self.original_image_label.image = img_tk
            self.original_image_label.grid(row=0, column=0)

    def on_mouse_move(self, event):
        if self.image is None:
            return
        x_canvas = event.x
        y_canvas = event.y
        if y_canvas < len(self.image) and x_canvas < len(self.image[0]):
            self.red_label.config(text="R: " + str(self.image[y_canvas][x_canvas][2]))
            self.green_label.config(text="G: " + str(self.image[y_canvas][x_canvas][1]))
            self.blue_label.config(text="B: " + str(self.image[y_canvas][x_canvas][0]))

    # Filtro de Escala de Grises
    def grayscale_image(self):
        if self.image is not None:
            self.progress_bar["value"] = 0
            filas, columnas, canales = self.image.shape
            for f in range(filas):
                for c in range(columnas):
                    color = self.image[f,c]
                    pro = (numpy.uint16(color[0]) + color[1] + color[2]) // 3
                    pro = numpy.uint8(pro)
                    self.image[f,c] = [pro, pro, pro]
                self.progress_bar["value"] = (f + 1) * 100 / filas
                self.root.update()  # Actualizar la interfaz gráfica
            self.display_image()
            self.update_preview()
        else:
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")

    # Filtro de Binarizado
    def binarize_image(self):
        if self.image is None: 
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return
        self.progress_bar["value"] = 0
        filas, columnas, canales = self.image.shape
        for f in range(filas):
            for c in range(columnas):
                if self.image[f,c,0] >= 128: valor = 255
                else : valor=0
                self.image[f,c] = [valor, valor, valor]
            self.progress_bar["value"] = (f + 1) * 100 / filas
            self.root.update()  # Actualizar la interfaz gráfica
        self.display_image()
        self.update_preview()

    # Filtro de Binarizado Dinamico
    def dynamic_binarize_image(self):
        if self.image is None: 
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return
        self.progress_bar["value"] = 0
        filas, columnas, canales = self.image.shape
        pro = 0
        for f in range(filas):
            for c in range(columnas):
                pro += self.image[f,c,0]
        pro = pro // (filas*columnas)

        print("Umbral"+str(pro))
        for f in range(filas):
            for c in range(columnas):
                if self.image[f,c,0] >= pro: valor = 255
                else : valor=0
                self.image[f,c] = [valor, valor, valor]
            self.progress_bar["value"] = (f + 1) * 100 / filas
            self.root.update()
        self.display_image()
        self.update_preview()

    # Filtro Negativo
    def negative_filter(self):
        if self.image is None: 
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return
        self.progress_bar["value"] = 0
        filas, columnas, canales = self.image.shape
        for f in range(filas):
            for c in range(columnas):
                self.image[f,c,0] = 255-self.image[f,c,0] 
                self.image[f,c,1] = 255-self.image[f,c,1] 
                self.image[f,c,2] = 255-self.image[f,c,2] 
            self.progress_bar["value"] = (f + 1) * 100 / filas
            self.root.update()
        self.display_image()
        self.update_preview()

    # Filtro de Suavizado
    def smooth_image(self):
        if self.image is None: 
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return
        self.progress_bar["value"] = 0
        filas, columnas, canales = self.image.shape
        new_image = numpy.ndarray(shape=self.image.shape, dtype = numpy.uint8) 
        for f in range(filas):
            for c in range(columnas):
                f1, f2 = f-1, f+1
                c1, c2 = c-1, c+1
                if f1<0: f1=0
                if c1<0: c1=0
                if f2>filas-1: f2 = filas-1
                if c2>columnas-1: c2 = columnas-1
                region = self.image[f1:f2+1,c1:c2+1]
                valor = region.mean()
                new_image[f,c] = [numpy.uint8(valor), numpy.uint8(valor),numpy.uint8(valor)] 
            self.progress_bar["value"] = (f + 1) * 100 / filas
            self.root.update()
        self.image = new_image
        self.display_image()
        self.update_preview()
        
    # Convolución manual entre una imagen y un nucleo
    def manual_convolution(self, image, kernel):
        m, n = kernel.shape
        offset_m = m // 2
        offset_n = n // 2
        padded_image = numpy.pad(image, ((offset_m, offset_m), (offset_n, offset_n)), mode='reflect')
        result = numpy.zeros_like(image)
        
        for i in range(offset_m, padded_image.shape[0] - offset_m):
            for j in range(offset_n, padded_image.shape[1] - offset_n):
                image_patch = padded_image[i - offset_m:i + offset_m + 1, j - offset_n:j + offset_n + 1]
                result[i - offset_m, j - offset_n] = numpy.sum(image_patch * kernel)
        return result
    
    # Detección de bordes Sobel
    def sobel_edge_detection(self):
        if self.image is None:
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return

        # Núcleos Sobel para bordes horizontales y verticales
        sobel_x = numpy.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = numpy.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

        gray_image = self.image.mean(axis=2) if len(self.image.shape) == 3 else self.image

        Ix = self.manual_convolution(gray_image, sobel_x)
        Iy = self.manual_convolution(gray_image, sobel_y)

        magnitude = numpy.sqrt(Ix**2 + Iy**2)

        self.image = numpy.dstack((magnitude, magnitude, magnitude)).astype(numpy.uint8)
        self.display_image()
        self.update_preview()
    
    # Detección de bordes Prewit
    def prewit_edge_detection(self):
        if self.image is None:
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return

         # Núcleos Prewit para bordes horizontales y verticales
        sobel_x = numpy.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        sobel_y = numpy.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

        gray_image = self.image.mean(axis=2) if len(self.image.shape) == 3 else self.image

        Ix = self.manual_convolution(gray_image, sobel_x)
        Iy = self.manual_convolution(gray_image, sobel_y)

        magnitude = numpy.sqrt(Ix**2 + Iy**2)

        magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min()) * 255

        self.image = numpy.dstack((magnitude, magnitude, magnitude)).astype(numpy.uint8)
        self.display_image()
        self.update_preview()
    
    # Detección de bordes Roberts
    def roberts_edge_detection(self):
        if self.image is None:
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return

         # Núcleos Roberts para bordes horizontales y verticales
        sobel_x = numpy.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]])
        sobel_y = numpy.array([[0, 0, -1], [0, 1, 0], [0, 0, 0]])

        gray_image = self.image.mean(axis=2) if len(self.image.shape) == 3 else self.image

        Ix = self.manual_convolution(gray_image, sobel_x)
        Iy = self.manual_convolution(gray_image, sobel_y)

        magnitude = numpy.sqrt(Ix**2 + Iy**2)

        magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min()) * 255

        self.image = numpy.dstack((magnitude, magnitude, magnitude)).astype(numpy.uint8)
        self.display_image()
        self.update_preview()
        
    # Función para generar un Nucleo Gaussiano
    def gaussian_kernel(self, size, sigma):
        # Eccuacion de gauss
        kernel_1D = numpy.linspace(-(size // 2), size // 2, size)
        for i in range(size):
            kernel_1D[i] = numpy.exp(-0.5 * (kernel_1D[i] / sigma) ** 2)
        kernel_2D = numpy.outer(kernel_1D.T, kernel_1D.T)
        kernel_2D *= 1.0 / kernel_2D.max()
        return kernel_2D

    # Función para aplicar desenfoque gaussiano a una imagen
    def gaussian_blur(self, image, kernel_size=5, sigma=1.4):
        kernel = self.gaussian_kernel(kernel_size, sigma)
        blurred_image = numpy.zeros_like(image, dtype=float)
        for channel in range(image.shape[2]):
            blurred_image[:, :, channel] = self.manual_convolution(image[:, :, channel], kernel)
        return blurred_image.astype(numpy.uint8)

    # Sobel
    def sobel_filters(self, img, kernel_size, sigma):
        if len(img.shape) == 3:
            img = numpy.mean(img, axis=2)
        elif len(img.shape) != 2:
            raise ValueError("La imagen debe ser 2D o 3D (imagen a color)")
                
        # Definir los Núcleos de Sobel
        Kx = numpy.array([[-1, 0, 1],
                          [-2, 0, 2],
                          [-1, 0, 1]])
        Ky = numpy.array([[-1, -2, -1],
                          [ 0,  0,  0],
                          [ 1,  2,  1]])

        Ix = self.manual_convolution(img, Kx)
        Iy = self.manual_convolution(img, Ky)

        G = numpy.hypot(Ix, Iy)
        G = G / G.max() * 255
        theta = numpy.arctan2(Iy, Ix)

        return (G, theta)

    # Función para realizar supresión de no máximos en la detección de bordes
    def non_max_suppression(self, img, D):
        # Eccuacion de gauss
        M, N = img.shape
        Z = numpy.zeros((M,N), dtype=numpy.int32)
        angle = D * 180. / numpy.pi
        angle[angle < 0] += 180

        for i in range(1,M-1):
            for j in range(1,N-1):
                try:
                    q = 255
                    r = 255
                    
                    if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                        q = img[i, j+1]
                        r = img[i, j-1]
                    elif (22.5 <= angle[i,j] < 67.5):
                        q = img[i+1, j-1]
                        r = img[i-1, j+1]
                    elif (67.5 <= angle[i,j] < 112.5):
                        q = img[i+1, j]
                        r = img[i-1, j]
                    elif (112.5 <= angle[i,j] < 157.5):
                        q = img[i-1, j-1]
                        r = img[i+1, j+1]

                    if (img[i,j] >= q) and (img[i,j] >= r):
                        Z[i,j] = img[i,j]
                    else:
                        Z[i,j] = 0
                except IndexError as e:
                    pass
        
        return Z

    # Función para aplicar umbralización y detección de bordes mediante el algoritmo de Canny
    def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
        # Eccuacion de gauss
        # Calcular los umbrales alto y bajo
        highThreshold = img.max() * highThresholdRatio
        lowThreshold = highThreshold * lowThresholdRatio
        
        # Obtener dimensiones de la imagen
        M, N = img.shape
        # Inicializar matriz de resultado
        res = numpy.zeros((M,N), dtype=numpy.int32)
        
        # Definir valores para píxeles débiles y fuertes
        weak = numpy.int32(25)
        strong = numpy.int32(255)
        
        # Encontrar ubicaciones de píxeles fuertes y débiles
        strong_i, strong_j = numpy.where(img >= highThreshold)
        zeros_i, zeros_j = numpy.where(img < lowThreshold)
        weak_i, weak_j = numpy.where((img <= highThreshold) & (img >= lowThreshold))
        
        # Asignar valores de píxeles fuertes y débiles a la matriz de resultado
        res[strong_i, strong_j] = strong
        res[weak_i, weak_j] = weak
        
        return (res, weak, strong)

    # Función para aplicar histeresis en la detección de bordes
    def hysteresis(self, img, weak, strong=255):
        M, N = img.shape  
        # Recorrer la imagen
        for i in range(1, M-1):
            for j in range(1, N-1):
                # Si el píxel es débil
                if (img[i,j] == weak):
                    try:
                        # Verificar si algún vecino es un píxel fuerte
                        if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                            or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                            or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                            img[i, j] = strong
                        else:
                            img[i, j] = 0
                    except IndexError as e:
                        pass
        return img 

    # Detección de bordes Canny
    def canny_edge_detection(self, kernel_size=5, sigma=0.4, low_threshold=50, high_threshold=150):
        if self.image is None:
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return
        if self.image is not None:
            # Paso 1: Suavizado de la imagen
            smoothed_image = self.gaussian_blur(self.image, kernel_size, sigma)
            
            # Paso 2: Detección de gradientes
            gradient_magnitude, gradient_direction = self.sobel_filters(smoothed_image, kernel_size, sigma)
            
            # Paso 3: Supresión de no máximos
            suppressed_gradient = self.non_max_suppression(gradient_magnitude, gradient_direction)
            
            # Paso 4: Umbralización por histéresis
            new_image = self.hysteresis(suppressed_gradient, low_threshold, high_threshold)
            self.image = new_image
            self.display_image()
    
    # Filtro Bilateral
    def bilateral_filter(self, mask=3, sigma_distance=1, sigma_intensity=1):
        if self.image is None:
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return
        
        mask_radius = mask // 2
        rows, columns, _ = self.image.shape
        new_image = numpy.zeros((rows, columns, 3), dtype=numpy.uint8)

        for row in range(rows):
            for column in range(columns):
                # Establece los límites de la máscara
                first_row = max(row - mask_radius, 0)
                last_row = min(row + mask_radius + 1, rows)
                first_column = max(column - mask_radius, 0)
                last_column = min(column + mask_radius + 1, columns)

                # Se establece la matriz de colores
                patch = self.image[first_row:last_row, first_column:last_column, 0]
                intensity_difference = self.image[row, column, 0] - patch  # Se calcula la diferencia de intensidad

                # Calcula el peso basado en la diferencia de intensidad
                intensity_weight = numpy.exp(-(intensity_difference**2) / (2 * sigma_intensity**2))  # Función gausseana

                # Calcula el peso basado en la distancia
                distance_weight = numpy.zeros((last_row - first_row, last_column - first_column))
                for r in range(first_row, last_row):
                    for c in range(first_column, last_column):
                        distance = numpy.sqrt((r - row)**2 + (c - column)**2)
                        distance_weight[r - first_row, c - first_column] = numpy.exp(-(distance**2) / (2 * sigma_distance**2))  # Función gausseana

                # Calcula la intensidad final de ambas matrices
                weight = intensity_weight * distance_weight

                # Aplica el filtro bilateral multiplicando cada píxel por su peso correspondiente
                filtered_value = numpy.sum(patch * weight) / numpy.sum(weight)

                # Se asigna el nuevo valor al píxel
                new_image[row, column, 0] = filtered_value
                new_image[row, column, 1] = filtered_value
                new_image[row, column, 2] = filtered_value

        self.image = new_image
        self.display_image()
        self.update_preview()

    def save_image(self):
        if self.image is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                cv2.imwrite(save_path, self.image)

    def delete_image_confirmation(self):
        if self.image is None:
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return
        if self.image is not None:
            confirmation = messagebox.askyesno("Eliminar Imagen", "¿Estás seguro de que quieres eliminar la imagen?")
            if confirmation:
                self.delete_image()

    def reset_image_confirmation(self):
        if self.image is None:
            messagebox.showinfo("Alerta", "No hay ninguna imagen abierta")
            return
        if self.image is not None:
            confirmation = messagebox.askyesno("Reiniciar Imagen", "¿Estás seguro de que quieres reiniciar la imagen?")
            if confirmation:
                self.reset_image()

    def delete_image(self):
        if self.image is not None:
            self.canvas.delete("all")
            self.image = None
            self.original_image_label.grid_forget()
            self.file_name_label.config(text="Sin Archivo")
            self.reset_preview()
            self.progress_bar["value"] = 0
            
            self.original_image_label = tk.Canvas(self.original_image_frame, width=300, height=100, bg="black", highlightbackground="#6ff9ff", highlightthickness=3)
            self.original_image_label.grid(row=0, column=0)

    def reset_image(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.display_image()
            self.update_preview()
            self.progress_bar["value"] = 0

    def update_preview(self):
        if self.image is not None:
            preview_image = cv2.resize(self.image, (300, 150))
            preview_image = cv2.cvtColor(preview_image, cv2.COLOR_BGR2RGB)
            preview_image = Image.fromarray(preview_image)
            preview_image_tk = ImageTk.PhotoImage(preview_image)
            self.preview_canvas.create_image(0, 0, anchor=tk.NW, image=preview_image_tk)
            self.preview_canvas.image = preview_image_tk

    def reset_preview(self):
        self.preview_canvas.delete("all")
        self.preview_canvas.create_text(150, 75, text="Sin Imagen", font=("Arial", 12), fill="#6ff9ff")

root = tk.Tk()
app = ImageProcessorApp(root)
root.mainloop()
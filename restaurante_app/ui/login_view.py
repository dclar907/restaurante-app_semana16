import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio


class LoginView:
    def __init__(self, root, abrir_principal):
        self.root = root
        self.abrir_principal = abrir_principal
        self.servicio = RestauranteServicio()

        self.root.title("Restaurante App - Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        contenedor = ttk.Frame(root, padding=30)
        contenedor.pack(expand=True)

        ttk.Label(
            contenedor,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        ttk.Label(contenedor, text="Usuario").pack(anchor="w")
        self.usuario_entry = ttk.Entry(contenedor, width=35)
        self.usuario_entry.pack(pady=5)

        ttk.Label(contenedor, text="Contraseña").pack(anchor="w")
        self.contrasena_entry = ttk.Entry(
            contenedor,
            width=35,
            show="*"
        )
        self.contrasena_entry.pack(pady=5)

        ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        ).pack(pady=20)

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning(
                "Advertencia",
                "Complete todos los campos."
            )
            return

        resultado = self.servicio.validar_usuario(
            usuario,
            contrasena
        )

        if resultado:
            self.root.destroy()
            self.abrir_principal(resultado)
        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )
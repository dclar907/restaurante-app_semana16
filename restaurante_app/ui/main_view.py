import tkinter as tk
from tkinter import ttk, messagebox

from servicios.restaurante_servicio import RestauranteServicio


class MainView:

    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.servicio = RestauranteServicio()

        self.ventana.title("Restaurante App")
        self.ventana.geometry("950x650")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = ttk.Label(
            self.ventana,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=20)

        bienvenida = ttk.Label(
            self.ventana,
            text=f"Bienvenido, {self.usuario}",
            font=("Arial", 12)
        )
        bienvenida.pack(pady=5)

        notebook = ttk.Notebook(self.ventana)
        notebook.pack(fill="both", expand=True, padx=20, pady=20)

        self.tab_usuarios = ttk.Frame(notebook)
        self.tab_productos = ttk.Frame(notebook)
        self.tab_ventas = ttk.Frame(notebook)

        notebook.add(self.tab_usuarios, text="Usuarios")
        notebook.add(self.tab_productos, text="Productos")
        notebook.add(self.tab_ventas, text="Ventas")

        self.crear_usuarios()
        self.crear_productos()
        self.crear_ventas()

    # =====================================================
    # USUARIOS
    # =====================================================

    def crear_usuarios(self):

        ttk.Label(
            self.tab_usuarios,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        columnas = ("id", "nombre", "correo")

        self.tabla_usuarios = ttk.Treeview(
            self.tab_usuarios,
            columns=columnas,
            show="headings"
        )

        self.tabla_usuarios.heading("id", text="ID")
        self.tabla_usuarios.heading("nombre", text="Nombre")
        self.tabla_usuarios.heading("correo", text="Correo")

        self.tabla_usuarios.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.cargar_usuarios()

    def cargar_usuarios(self):

        for item in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(item)

        usuarios = self.servicio.obtener_usuarios()

        for usuario in usuarios:

            self.tabla_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.get("id_usuario", ""),
                    usuario.get("nombre", ""),
                    usuario.get("correo", "")
                )
            )

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def crear_productos(self):

        ttk.Label(
            self.tab_productos,
            text="Productos registrados",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        columnas = ("codigo", "nombre", "precio", "stock")

        self.tabla_productos = ttk.Treeview(
            self.tab_productos,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading("codigo", text="Código")
        self.tabla_productos.heading("nombre", text="Producto")
        self.tabla_productos.heading("precio", text="Precio")
        self.tabla_productos.heading("stock", text="Stock")

        self.tabla_productos.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.cargar_productos()

    def cargar_productos(self):

        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = self.servicio.obtener_productos()

        for producto in productos:

            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.get("codigo", ""),
                    producto.get("nombre", ""),
                    producto.get("precio", ""),
                    producto.get("stock", "")
                )
            )

    # =====================================================
    # VENTAS
    # =====================================================

    def crear_ventas(self):

        ttk.Label(
            self.tab_ventas,
            text="Registrar venta",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        formulario = ttk.Frame(self.tab_ventas)
        formulario.pack(pady=10)

        # -------------------------
        # USUARIO
        # -------------------------

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.combo_usuario = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.combo_usuario.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # -------------------------
        # PRODUCTO
        # -------------------------

        ttk.Label(
            formulario,
            text="Producto:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.combo_producto = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.combo_producto.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # -------------------------
        # BOTÓN
        # -------------------------

        boton = ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta
        )

        boton.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=15
        )

        self.cargar_combos()

        # -------------------------
        # TABLA DE VENTAS
        # -------------------------

        ttk.Label(
            self.tab_ventas,
            text="Ventas registradas",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        columnas = (
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            self.tab_ventas,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.cargar_ventas()

    # =====================================================
    # COMBOS
    # =====================================================

    def cargar_combos(self):

        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        self.usuarios_data = usuarios
        self.productos_data = productos

        usuarios_combo = []

        for usuario in usuarios:
            usuarios_combo.append(
                f"{usuario.get('id_usuario')} - "
                f"{usuario.get('nombre', '')}"
            )

        productos_combo = []

        for producto in productos:
            productos_combo.append(
                f"{producto.get('codigo')} - "
                f"{producto.get('nombre', '')}"
            )

        self.combo_usuario["values"] = usuarios_combo
        self.combo_producto["values"] = productos_combo

    # =====================================================
    # CALLBACK DE VENTA
    # =====================================================

    def registrar_venta(self):

        usuario_seleccionado = self.combo_usuario.get()
        producto_seleccionado = self.combo_producto.get()

        if not usuario_seleccionado:
            messagebox.showwarning(
                "Aviso",
                "Seleccione un usuario."
            )
            return

        if not producto_seleccionado:
            messagebox.showwarning(
                "Aviso",
                "Seleccione un producto."
            )
            return

        id_usuario = usuario_seleccionado.split(" - ")[0]
        codigo_producto = producto_seleccionado.split(" - ")[0]

        # La interfaz delega la operación al servicio
        resultado, mensaje = self.servicio.registrar_venta(
            id_usuario,
            codigo_producto
        )

        if resultado:

            messagebox.showinfo(
                "Venta",
                mensaje
            )

            self.cargar_ventas()
            self.cargar_productos()
            self.cargar_combos()

            self.combo_usuario.set("")
            self.combo_producto.set("")

        else:

            messagebox.showerror(
                "Error",
                mensaje
            )

    # =====================================================
    # CARGAR VENTAS
    # =====================================================

    def cargar_ventas(self):

        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        ventas = self.servicio.obtener_ventas()

        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        for venta in ventas:

            nombre_usuario = venta.get("id_usuario", "")
            nombre_producto = venta.get("codigo_producto", "")

            for usuario in usuarios:
                if str(usuario.get("id_usuario")) == str(
                    venta.get("id_usuario")
                ):
                    nombre_usuario = usuario.get(
                        "nombre",
                        venta.get("id_usuario")
                    )
                    break

            for producto in productos:
                if str(producto.get("codigo")) == str(
                    venta.get("codigo_producto")
                ):
                    nombre_producto = producto.get(
                        "nombre",
                        venta.get("codigo_producto")
                    )
                    break

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    nombre_usuario,
                    nombre_producto,
                    venta.get("fecha", "")
                )
            )
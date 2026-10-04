from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):
        self.archivo = ArchivoServicio()

        self.usuarios = self.archivo.cargar_usuarios()
        self.productos = self.archivo.cargar_productos()
        self.ventas = self.archivo.cargar_ventas()

    # =========================
    # USUARIOS
    # =========================

    def obtener_usuarios(self):
        return self.usuarios

    def buscar_usuario_por_id(self, id_usuario):
        for usuario in self.usuarios:
            if str(usuario.id_usuario) == str(id_usuario):
                return usuario
        return None

    def buscar_usuario_por_nombre_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.usuario == nombre_usuario:
                return usuario
        return None

    def autenticar_usuario(self, nombre_usuario, contrasena):
        for usuario in self.usuarios:
            if (
                usuario.usuario == nombre_usuario
                and usuario.contrasena == contrasena
            ):
                return usuario
        return None

    def registrar_usuario(self, id_usuario, nombre, usuario, contrasena, rol):
        if not id_usuario or not nombre or not usuario or not contrasena:
            return False, "Todos los campos son obligatorios."

        if self.buscar_usuario_por_id(id_usuario):
            return False, "El identificador ya existe."

        if self.buscar_usuario_por_nombre_usuario(usuario):
            return False, "El nombre de usuario ya existe."

        if rol not in ["Administrador", "Empleado", "Cliente"]:
            return False, "Seleccione un rol válido."

        nuevo_usuario = Usuario(
            id_usuario,
            nombre,
            usuario,
            contrasena,
            rol
        )

        self.usuarios.append(nuevo_usuario)
        self.archivo.guardar_usuarios(self.usuarios)

        return True, "Usuario registrado correctamente."

    def actualizar_usuario(
        self,
        id_usuario,
        nombre,
        usuario,
        contrasena,
        rol
    ):
        usuario_obj = self.buscar_usuario_por_id(id_usuario)

        if usuario_obj is None:
            return False, "Usuario no encontrado."

        if not nombre or not usuario:
            return False, "El nombre y usuario son obligatorios."

        otro_usuario = self.buscar_usuario_por_nombre_usuario(usuario)

        if otro_usuario and str(otro_usuario.id_usuario) != str(id_usuario):
            return False, "El nombre de usuario ya existe."

        usuario_obj.nombre = nombre
        usuario_obj.usuario = usuario

        if contrasena:
            usuario_obj.contrasena = contrasena

        usuario_obj.rol = rol

        self.archivo.guardar_usuarios(self.usuarios)

        return True, "Usuario actualizado correctamente."

    def eliminar_usuario(self, id_usuario, usuario_actual=None):
        usuario_obj = self.buscar_usuario_por_id(id_usuario)

        if usuario_obj is None:
            return False, "Usuario no encontrado."

        if (
            usuario_actual is not None
            and str(usuario_obj.id_usuario) == str(usuario_actual.id_usuario)
        ):
            return False, "No puede eliminar al usuario administrador actualmente autenticado."

        self.usuarios.remove(usuario_obj)
        self.archivo.guardar_usuarios(self.usuarios)

        return True, "Usuario eliminado correctamente."

    # =========================
    # PRODUCTOS
    # =========================

    def obtener_productos(self):
        return self.productos

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if str(producto.codigo) == str(codigo):
                return producto
        return None

    def registrar_producto(self, codigo, nombre, precio, stock, categoria):
        if self.buscar_producto(codigo):
            return False, "El código del producto ya existe."

        producto = Producto(
            codigo,
            nombre,
            precio,
            stock,
            categoria
        )

        self.productos.append(producto)
        self.archivo.guardar_productos(self.productos)

        return True, "Producto registrado correctamente."

    def actualizar_producto(
        self,
        codigo,
        nombre,
        precio,
        stock,
        categoria
    ):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.categoria = categoria

        self.archivo.guardar_productos(self.productos)

        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        self.productos.remove(producto)
        self.archivo.guardar_productos(self.productos)

        return True, "Producto eliminado correctamente."

    # =========================
    # VENTAS
    # =========================

    def registrar_venta(self, id_usuario, codigo_producto, cantidad):
        usuario = self.buscar_usuario_por_id(id_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None:
            return False, "Usuario no encontrado."

        if producto is None:
            return False, "Producto no encontrado."

        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que cero."

        if producto.stock < cantidad:
            return False, "Stock insuficiente."

        producto.stock -= cantidad

        venta = Venta(
            id_usuario,
            codigo_producto,
            cantidad
        )

        self.ventas.append(venta)

        self.archivo.guardar_productos(self.productos)
        self.archivo.guardar_ventas(self.ventas)

        return True, "Venta registrada correctamente."

    def obtener_ventas(self):
        return self.ventas
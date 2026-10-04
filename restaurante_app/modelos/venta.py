from datetime import datetime


class Venta:
    def __init__(self, id_usuario, codigo_producto, fecha=None):
        self.id_usuario = id_usuario
        self.codigo_producto = codigo_producto
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "codigo_producto": self.codigo_producto,
            "fecha": self.fecha
        }
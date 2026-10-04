class Producto:
    def __init__(self, id_producto, nombre, precio, categoria, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria
        self.stock = int(stock)

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }
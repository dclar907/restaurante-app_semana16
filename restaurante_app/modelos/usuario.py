class Usuario:
    def __init__(self, id_usuario, nombre, usuario, contrasena, rol="Cliente"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "rol": self.rol
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos.get("id_usuario"),
            datos.get("nombre", ""),
            datos.get("usuario", ""),
            datos.get("contrasena", ""),
            datos.get("rol", "Cliente")
        )
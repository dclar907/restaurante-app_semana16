# Restaurante App

## Semana 16

En esta semana se amplió el sistema de gestión del restaurante incorporando la administración completa de usuarios y roles.

## Funciones implementadas

- Registro de usuarios.
- Consulta de usuarios.
- Actualización de usuarios.
- Eliminación de usuarios.
- Gestión de roles.
- Roles disponibles:
  - Administrador
  - Empleado
  - Cliente
- Protección del usuario administrador actualmente autenticado.
- Persistencia de usuarios mediante `usuarios.json`.
- Visualización de usuarios mediante `Treeview`.
- Selección de usuarios mediante `<<TreeviewSelect>>`.
- Selección de roles mediante `<<ComboboxSelected>>`.
- Registro mediante la tecla `Enter`.
- Limpieza mediante la tecla `Escape`.
- Botones mediante `command=`.

## Arquitectura

```text
restaurante_app/
│
├── assets/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
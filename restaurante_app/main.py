import tkinter as tk
from ui.login_view import LoginView
from ui.main_view import MainView


def abrir_principal(usuario):
    ventana = tk.Tk()
    MainView(ventana, usuario)
    ventana.mainloop()


def main():
    ventana = tk.Tk()
    LoginView(ventana, abrir_principal)
    ventana.mainloop()


if __name__ == "__main__":
    main()
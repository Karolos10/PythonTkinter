from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

cuadroComentarios = Text(miFrame, width=16, height=5)
cuadroComentarios.grid(row=4, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=cuadroComentarios.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")

cuadroComentarios.config(yscrollcommand=scrollVert.set)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

def funcionEnviar():
    print("Nombre: " + cuadroNombre.get())
    print("Contraseña: " + cuadroPass.get())
    print("Apellido: " + cuadroApellido.get())
    print("Dirección: " + cuadroDireccion.get())
    print("Comentarios: " + cuadroComentarios.get("1.0", END))

botonEnvio=Button(raiz, text="Enviar", command=funcionEnviar)
botonEnvio.pack()

raiz.mainloop()
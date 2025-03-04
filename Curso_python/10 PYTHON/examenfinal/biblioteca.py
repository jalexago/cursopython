# imprimo la bienvenida#
print("Bienvenido al sistema de gestion de biblioteca")
#muestro las opciones para el usuario #
print("1. Agregar libro")
print("2. Prestar libro")
print("3. Devolver libro")
print("4. Mostrar libros")
print("5. Buscar")
print("6. Salir")
#pido al usuario que elija una opcion#
opcion = int(input("Elige una opción: "))
# si la opcion es 1#
if opcion == 1:
    #pido los datos del libro#
    # en el titulo digo que es un string#
    titulo =str(input("Introduce el titulo: "))
    # en el autor digo que es un string#
    autor =str(input("Introduce el autor: "))
    # en el isbn digo que es un string#
    isbn =str(input("Introduce el ISBN: "))
    # le pongo atributo a disponible como booleano y valor true #
    disponible =bool(True) 
    #abro un diccionario para guardar los datos#
    libro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "disponible": disponible
    }
    # actualizo el diccionario de libro con el nuevo libro #
    libro.update(libro)
    # imprimo que el libro se ha agregado#
    print("Libro agregado con Exito")
    # si la opcion es 2#
elif opcion == 2:
    # pido el isbn del libro a prestar#
    isbn = input("Introduce el ISBN del libro a prestar: ")
    # busco el libro por el isbn#
    libro = libro.get(isbn)
    # si el libro esta disponible#
    if libro["disponible"] == True:
        # cambio el valor de disponible a false#
        libro["disponible"] = False
        # imprimo que el libro se ha prestado#
        print("Libro prestado con Exito")
    else:
        # si el libro no esta disponible imprimo que no se puede prestar#
        print("El libro no esta disponible")
    # si la opcion es 3#
   
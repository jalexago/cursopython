#defino la clase libro#
class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        #defino el estado del libro con un bool true para disponible y false para no disponible#
        self.disponible = True
        #defino la clase biblioteca#
class Biblioteca:
    def __init__(self):
        self.libros = []
        #defino la opcion agregar libro#
    def agregar_libro(self,):
        #pido los datos de libro y le digo que es tipo string#
        titulo = str(input("Ingrese el titulo: "))
        #pido los datos del autor y le digo que es tipo string#
        autor = str(input("Ingrese el autor: "))
        #pido los datos del isbn y le digo que es tipo string#
        isbn = str(input("Ingrese el ISBN: "))
        #creo un objeto de la clase libro#
        libro = Libro(titulo, autor, isbn, True)
        #agrego el libro a la lista de libros#
        self.libros.append(libro)
        #defino la opcion prestar libro#
    def prestar_libro(self):
        isbn = input("Ingrese el ISBN : ")
        #busco el libro con el isbn ingresado con el condicional for y if#
        for libro in self.libros:
            #si el libro es encontrado y esta disponible se cambia el estado a no disponible#
            if libro.isbn == isbn:
                if libro.disponible:
                    # cambio el estado con el bool false y envio un mensaje de libro prestado con exito#
                    libro.disponible = False
                    print("Libro prestado con exito")
                else:
                    #si el libro no esta disponible se imprime un mensaje#
                    print("Libro no disponible")
                return
        #si el libro no es encontrado se imprime un mensaje#        
        print("Libro no encontrado")
    def devolver_libro(self):
        isbn = input("Ingrese el ISBN : ")
        #busco el libro con el isbn ingresado con el bucle y condicional for y if#
        for libro in self.libros:
            #si el libro es encontrado se cambia el estado a disponible con el bool true
            # y envio un mensaje de libro devuelto #
            if libro.isbn == isbn:
                if not libro.disponible:
                    libro.disponible = True
                    print("Libro devuelto con exito")
                return
        #si el isbn no es encontrado se imprime un mensaje#
        print("Libro no encontrado con ese isbn ")
    #defino la opcion de mostrar libros#
    def mostrar_libros(self):
        #pongo condicional if para ver si la lista esta vacia#
        if not self.libros:
            print("No hay libros en la biblioteca")
        else:
            #si la lista no esta vacia se imprime los libros con el bucle for#
            for libro in self.libros:
                print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Disponible: {libro.disponible}")
    #defino la opcion buscar#
    def buscar_libro(self):
        isbn = input("Ingrese el ISBN : ")
        #busco el libro con el isbn ingresado con el bucle y condicional for y if#
        for libro in self.libros:
            #si el libro es encontrado se imprime los datos del libro#
            if libro.isbn == isbn:
                print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Disponible: {libro.disponible}")
                return
        #si el libro no es encontrado se imprime un mensaje#
        print("Libro no encontrado")   
#defino el menu que mostarra las opciones#
def menu():
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro")
    print("6. Salir")
    opcion = int(input("Elige una opcion: "))
    return opcion  
#defino el main con los condicionales if para las opciones del menu#
#y el bucle while para que el menu se repita hasta que se elija la opcion salir#
def main():
    biblioteca = Biblioteca()
    while True:
        opcion = menu()
        #le digo que si elegen 1 se ejecute la opcion agregar libro#
        if opcion == 1:
            biblioteca.agregar_libro()
        # le digo que si eligen la opcion 2 se ejecute la opcion prestar libro#
        elif opcion == 2:
            biblioteca.prestar_libro()
        #le digo que si eligen la opcion 3 se ejecute la opcion devolver libro#
        elif opcion == 3:
            biblioteca.devolver_libro()
        #le digo que si eligen la opcion 4 se ejecute la opcion mostrar libros#
        elif opcion == 4:
            biblioteca.mostrar_libros()
        #le digo que si eligen la opcion 5 se ejecute la opcion buscar libro#
        elif opcion == 5:
            biblioteca.buscar_libro()
        elif opcion == 6:
            #si se elige la opcion salir se imprime un mensaje y se rompe el bucle while#
            print("Gracias por usar el sistema degestion que tenga un buen dia ")
            break
        #si digitalizan una opcion no contemplada se imprime el mensaje#
        else:
            print("Opcion no valida")  
#condicional para que se ejecute el main#
if __name__ == "__main__":
    main()                     

                    
                   

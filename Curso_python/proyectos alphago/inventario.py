import datetime

# Lista para almacenar los datos del inventario
inventario = []

def agregar_cantidad():
    referencia = input("Ingresa la referencia: ")
    lote = input("Ingresa el lote: ")
    cantidad = int(input("Ingresa la cantidad: "))
    fecha = datetime.date.today()
    
    encontrado = False
    for item in inventario:
        if item['referencia'] == referencia and item['lote'] == lote:
            item['cantidad'] += cantidad
            encontrado = True
            break

    if not encontrado:
        inventario.append({'referencia': referencia, 'lote': lote, 'cantidad': cantidad, 'fecha': fecha})

def descontar_cantidad():
    referencia = input("Ingresa la referencia: ")
    cantidad = int(input("Ingresa la cantidad a descontar: "))
    
    stock_total = sum(item['cantidad'] for item in inventario if item['referencia'] == referencia)
    if stock_total < cantidad:
        print(f"Stock insuficiente. Te faltan {cantidad - stock_total} unidades.")
        return
    
    cantidad_restante = cantidad
    for item in inventario:
        if item['referencia'] == referencia:
            if item['cantidad'] >= cantidad_restante:
                item['cantidad'] -= cantidad_restante
                break
            else:
                cantidad_restante -= item['cantidad']
                item['cantidad'] = 0
    
    print("Operación completada con éxito.")

def ver_cantidades_disponibles():
    referencia = input("Ingresa la referencia: ")
    encontrado = False
    
    for item in inventario:
        if item['referencia'] == referencia and item['cantidad'] > 0:
            print(f"Lote: {item['lote']}, Cantidad: {item['cantidad']}, Fecha: {item['fecha']}")
            encontrado = True
    
    if not encontrado:
        print("No se encontró la referencia o no tiene cantidad disponible.")

def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar cantidad")
        print("2. Descontar cantidad")
        print("3. Ver cantidades disponibles")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_cantidad()
        elif opcion == "2":
            descontar_cantidad()
        elif opcion == "3":
            ver_cantidades_disponibles()
        elif opcion == "4":
            print("Gracias por usar el sistema de gestión de inventario. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

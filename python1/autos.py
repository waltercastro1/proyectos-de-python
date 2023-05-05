# Definir un diccionario para almacenar los modelos de auto disponibles y sus precios
autos_disponibles = {"Ford": 20000, "Chevrolet": 25000, "Toyota": 30000}

# Definir una variable para el carrito del cliente y otra para el precio total
carrito = []
precio_total = 0

# Imprimir los modelos de auto disponibles y sus precios
print("Modelos de auto disponibles y sus precios:")
for modelo, precio in autos_disponibles.items():
    print(modelo, "-", "${:,.2f}".format(precio))

# Pedir al usuario que seleccione un modelo de auto
while True:
    modelo_seleccionado = input("Seleccione un modelo de auto para comprar: ")
    if modelo_seleccionado in autos_disponibles:
        carrito.append(modelo_seleccionado)
        precio_total += autos_disponibles[modelo_seleccionado]
        print("El modelo de auto", modelo_seleccionado, "se ha agregado al carrito.")
        continuar_comprando = input("¿Desea seguir comprando? (S/N): ")
        if continuar_comprando.lower() == "n":
            break
    else:
        print("El modelo de auto seleccionado no está disponible.")

# Imprimir el carrito y el precio total
print("Carrito de compras:")
for modelo in carrito:
    print(modelo)
print("Precio total: ${:,.2f}".format(precio_total))


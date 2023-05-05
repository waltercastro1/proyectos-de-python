# Definimos las variables globales
transacciones = []
libro_iva_ventas = []
libro_iva_compras = []


# Función para agregar una transacción
def agregar_transaccion():
    tipo = input('Tipo de transacción (venta/compra): ')
    fecha = input('Fecha (YYYY-MM-DD): ')
    concepto = input('Concepto: ')
    importe = float(input('Importe: '))
    iva = importe * 0.21
    transacciones.append({
        'tipo': tipo,
        'fecha': fecha,
        'concepto': concepto,
        'importe': importe,
        'iva': iva
    })
    print('Transacción agregada.')
    if tipo == 'venta':
        libro_iva_ventas.append({
            'fecha': fecha,
            'importe': importe,
            'iva': iva
        })
    elif tipo == 'compra':
        libro_iva_compras.append({
            'fecha': fecha,
            'importe': importe,
            'iva': iva
        })


# Función para ver las transacciones
def ver_transacciones():
    print('ID\tTipo\tFecha\t\tConcepto\t\tImporte\t\tIVA')
    for i, t in enumerate(transacciones):
        print(f'{i+1}\t{t["tipo"]}\t{t["fecha"]}\t{t["concepto"]}\t{t["importe"]}\t{t["iva"]}')


# Función para calcular el balance
def calcular_balance():
    ventas = sum([t['importe'] for t in transacciones if t['tipo'] == 'venta'])
    compras = sum([t['importe'] for t in transacciones if t['tipo'] == 'compra'])
    iva_ventas = sum([t['iva'] for t in transacciones if t['tipo'] == 'venta'])
    iva_compras = sum([t['iva'] for t in transacciones if t['tipo'] == 'compra'])
    iva_total = iva_ventas - iva_compras
    balance = ventas - compras
    print(f'Ventas: {ventas}')
    print(f'Compras: {compras}')
    print(f'IVA ventas: {iva_ventas}')
    print(f'IVA compras: {iva_compras}')
    print(f'IVA total: {iva_total}')
    print(f'Balance: {balance}')


# Función para generar el libro de IVA de ventas
def generar_iva_ventas():
    print('Fecha\t\tImporte\t\tIVA')
    for t in libro_iva_ventas:
        print(f'{t["fecha"]}\t{t["importe"]}\t{t["iva"]}')


# Función para generar el libro de IVA de compras
def generar_iva_compras():
    print('Fecha\t\tImporte\t\tIVA')
    for t in libro_iva_compras:
        print(f'{t["fecha"]}\t{t["importe"]}\t{t["iva"]}')


# Función para mostrar el menú y ejecutar las opciones
def mostrar_menu():
    while True:
        print('\n--- MENU ---')
        print('1. Agregar transacción')
        print('2. Ver transacciones')
        print('3. Calcular balance')
        print('4. Generar libro IVA ventas')
        print('5. Generar libro IVA compras')
        print('0. Salir del sistema')
        opcion = input('Seleccione una opción: ')
        if opcion == '1':
            agregar_transaccion()
        elif opcion == '2':
            ver_transacciones()
        elif opcion == '3':
            calcular_balance()
        elif opcion == '4':
            generar_iva_ventas()
        elif opcion == '5':
            generar_iva_compras()
        elif opcion == '0':
            break
        else:
            print('Opción inválida. Intente nuevamente.')
            

        # Ejecutamos el programa
mostrar_menu()
 


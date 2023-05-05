import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema Contable")

# Crear widgets
titulo = tk.Label(ventana, text="Sistema Contable", font=("Arial", 20))
titulo.pack(pady=20)

# Variables de seguimiento
fecha_var = tk.StringVar()
descripcion_var = tk.StringVar()
tipo_var = tk.StringVar()
monto_var = tk.StringVar()
lista_transacciones = []

# Funciones para manejar eventos
def agregar_transaccion():
    # Obtener los valores de las variables de seguimiento
    fecha = fecha_var.get()
    descripcion = descripcion_var.get()
    tipo = tipo_var.get()
    monto = float(monto_var.get())
    
    # Agregar la transacción a la lista
    lista_transacciones.append({
        'fecha': fecha,
        'descripcion': descripcion,
        'tipo': tipo,
        'monto': monto
    })
    
    # Limpiar los campos de entrada
    fecha_var.set('')
    descripcion_var.set('')
    tipo_var.set('')
    monto_var.set('')
    
import csv

def eliminar_transaccion(id_transaccion):
    # Leer las transacciones actuales del archivo
    with open("transacciones.csv", "r") as archivo:
        lector_csv = csv.reader(archivo)
        transacciones = list(lector_csv)

    # Buscar la transacción con el ID especificado
    for i, transaccion in enumerate(transacciones):
        if transaccion[0] == id_transaccion:
            # Eliminar la transacción de la lista
            del transacciones[i]
            break

    # Escribir las transacciones actualizadas al archivo
    with open("transacciones.csv", "w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        for transaccion in transacciones:
            escritor_csv.writerow(transaccion)
202

def ver_transacciones():
    # Crear una nueva ventana para mostrar las transacciones
    ventana_transacciones = tk.Toplevel(ventana)
    ventana_transacciones.title("Transacciones")
    
    # Crear una tabla para mostrar las transacciones
    tabla = tk.Label(ventana_transacciones, text='Fecha\tDescripción\tTipo\tMonto', font=('Arial', 12))
    tabla.pack(pady=10)
    
    for transaccion in lista_transacciones:
        fila = tk.Label(ventana_transacciones, text=f"{transaccion['fecha']}\t{transaccion['descripcion']}\t{transaccion['tipo']}\t{transaccion['monto']:.2f}", font=('Arial', 12))
        fila.pack()
    
def calcular_balance():
    # Calcular el balance a partir de la lista de transacciones
    total_ingresos = 0
    total_egresos = 0
    
    for transaccion in lista_transacciones:
        if transaccion['tipo'] == 'Ingreso':
            total_ingresos += transaccion['monto']
        else:
            total_egresos += transaccion['monto']
    
    balance = total_ingresos - total_egresos
    
    # Mostrar el balance en una nueva ventana
    ventana_balance = tk.Toplevel(ventana)
    ventana_balance.title("Balance")
    
    texto = tk.Label(ventana_balance, text=f'Total ingresos: {total_ingresos:.2f}\nTotal egresos: {total_egresos:.2f}\nBalance: {balance:.2f}', font=('Arial', 12))
    texto.pack(pady=10)

def generar_iva_ventas():
    # Obtener las transacciones que corresponden al IVA de ventas
    transacciones_iva_ventas = [t for t in lista_transacciones if t['tipo'] == 'Venta']
    
    # Calcular el IVA de ventas
    iva_ventas = sum([t['monto'] * 0.21 for t in transacciones_iva_ventas])
    
    # Mostrar el IVA de ventas en una nueva ventana
    ventana_iva_ventas = tk.Toplevel(ventana)
    ventana_iva_ventas.title("IVA de Ventas")
    
    texto = tk.Label(ventana_iva_ventas, text=f'IVA de ventas: {iva_ventas:.2f}', font=('Arial', 12))
    texto.pack(pady=10)
    
def generar_iva_compras():
    # Obtener las transacciones que corresponden al IVA de compras
    transacciones_iva_compras = [t for t in lista_transacciones if t['tipo'] == 'Compra']
    
    # Calcular el IVA de compras
    iva_compras = sum([t['monto'] * 0.21 for t in transacciones_iva_compras])
    
    # Mostrar el IVA de compras en una nueva ventana
    ventana_iva_compras = tk.Toplevel(ventana)
    ventana_iva_compras.title("IVA de Compras")
    
    texto = tk.Label(ventana_iva_compras, text=f'IVA de compras: {iva_compras:.2f}', font=('Arial', 12))
    texto.pack(pady=10)

# Crear los widgets de entrada de datos
frame_entrada = tk.Frame(ventana)
frame_entrada.pack()

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
tk.Entry(frame_entrada, textvariable=fecha_var).grid(row=0, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0)
tk.Entry(frame_entrada, textvariable=descripcion_var).grid(row=1, column=1)

tk.Label(frame_entrada, text="Tipo:").grid(row=2, column=0)
tk.OptionMenu(frame_entrada, tipo_var, "Ingreso", "Egreso").grid(row=2, column=1)

tk.Label(frame_entrada, text="Monto:").grid(row=3, column=0)
tk.Entry(frame_entrada, textvariable=monto_var).grid(row=3, column=1)

# Crear los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

tk.Button(frame_botones, text="Agregar Transacción", command=agregar_transaccion).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Ver Transacciones", command=ver_transacciones).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Calcular Balance", command=calcular_balance).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Generar IVA de Ventas", command=generar_iva_ventas).grid(row=1, column=0, pady=10)
tk.Button(frame_botones, text="Generar IVA de Compras", command=generar_iva_compras).grid(row=1, column=1, pady=10)

# Ejecutar la ventana
ventana.mainloop()

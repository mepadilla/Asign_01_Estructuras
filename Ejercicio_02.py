#Ejercicio 1: Gestión de Inventario
#Descripción: Dado un archivo de texto inventario.txt con la siguiente estructura:
#código; categoría; producto; stock; precio; proveedor; fecha_ingreso
#Ejemplo:
#INV-001; Electrónica; Laptop HP; 15; 1200.50; TechSupplies; 2023-10-05
#INV-002; Oficina; Silla ergonómica; 30; 199.99; OfficePro; 2023-09-15
#Desarrollar un script en Python que:
#1. Liste los productos por categoría.
#2. Determine el producto con mayor stock.
#3. Calcule el valor total del inventario (stock × precio).
#4. Identifique al proveedor con más productos en inventario.
#5. Genere un informe de productos con stock menor a un umbral dado.
#6. Implemente un menú interactivo para acceder a cada función.
lectura = 0
seleccion = 0
lst_txt_b = []
# SECCION DE DEFINICION DE FUNCIONES
#
# FUNCION PARA LEER ARCHIVO TXT
def leer_txt(archivo):
    with open(archivo) as archivo:
        for linea in archivo:
            str_txt_a = linea
            lst_txt_b.append(str_txt_a.split(';'))
    # print(lst_txt_b)
    print('\n')
    print("LISTA CON LINEAS CARGADAS DEL ARCHIVO DE TEXTO\n")
    for elemento in lst_txt_b:
        print(elemento)
    return lst_txt_b
    print('ARCHIVO DE TEXTO CARGADO')
#
while seleccion != 9:
    print('\n')
    print('* * * MENU DE OPCIONES PARA ANALISIS DE INVENTARIO * * *')
    print('Introduzca el numero de la opcion requerida.')
    print('1 - Lectura del Archivo txt')
    print('2 - Liste los productos por categoría')
    print('3 - Determine el producto con mayor stock')
    print('4 - Calcule el valor total del inventario (stock × precio)')
    print('5 - Identifique al proveedor con más productos en inventario')
    print('6 - enere un informe de productos con stock menor a un umbral dado')
    print('9 - Finalizar ejecucion del programa\n')
    seleccion = int(input("INTRODUZCA LA OCION REQUERIDA: "))
    #INICIO DE OPERACIONES
    if lectura == 0 or seleccion == 1:
        leer_txt("horarios.txt")
        lectura = 1
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 2:
        print('OPCION DOS TOMADA')
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 3:
        print('OPCION TRES TOMADA')
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 4:
        print('OPCION CUATRO TOMADA')
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 5:
        print('OPCION CINCO TOMADA')
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 6:
        print('OPCION SEIS TOMADA')
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 7:
        print('OPCION SIETE TOMADA')
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 8:
        print('OPCION OCHO TOMADA')
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 9:
        print('OPCION NUEVE TOMADA')
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))


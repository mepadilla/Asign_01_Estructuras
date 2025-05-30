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
lst_txt_b = []      #Lista con lineas del txt
lst_cat_prod = []   #Lista con categorias de productos y productos
lst_cat =[]         #Lista con categorias de producto
dic_cat_prod = {}   #Diccionario con categoria como indice y productos como elementos
lst_prod_aux = []   #Lista auxiliar de productos
#
# SECCION DE DEFINICION DE FUNCIONES
#
#FUNCION PARA IMPRIMIR LISTAS
def print_list(lista_in):
    for elemento in lista_in:
        print(elemento)
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
    print_list(lst_txt_b)
    return lst_txt_b
    print('ARCHIVO DE TEXTO CARGADO')
# Esta funcion lee una lista de listas dada y retorna una lista con los elementos internos de cada lista en las
# dos posiciones dadas
def list_append_two(listatxt,posicion1,posicion2):
    lst_aux=[]
    for indice in range(len(listatxt)):
        lst_aux.append(listatxt[indice][posicion1])
        lst_aux.append(listatxt[indice][posicion2])
    return lst_aux
# Esta funcion lee una lista de listas dada y retorna una lista con los elementos internos de cada lista en la
# posicion dada
def list_append_one(listatxt,posicion1):
    lst_aux=[]
    for indice in range(len(listatxt)):
        lst_aux.append(listatxt[indice][posicion1])
    return lst_aux
#
while seleccion != 7:
    print('\n')
    print('* * * MENU DE OPCIONES PARA ANALISIS DE INVENTARIO * * *')
    print('Introduzca el numero de la opcion requerida.')
    print('1 - Lectura del Archivo txt')
    print('2 - Liste los productos por categoría')
    print('3 - Determine el producto con mayor stock')
    print('4 - Calcule el valor total del inventario (stock × precio)')
    print('5 - Identifique al proveedor con más productos en inventario')
    print('6 - Genere un informe de productos con stock menor a un umbral dado')
    print('7 - Finalizar ejecucion del programa\n')
    seleccion = int(input("INTRODUZCA LA OPCION REQUERIDA: "))
    #INICIO DE OPERACIONES
    if lectura == 0 or seleccion == 1:
        leer_txt("inventario.txt")
        lectura = 1
        continuar = str(input("* * PRESIONE ENTER PARA CONTINUAR * * \n"))
    if  seleccion == 2:
        lst_cat_prod=list_append_two(lst_txt_b,1,2)
        lst_cat=list(set(list_append_one(lst_txt_b,1)))
        print(lst_cat_prod)
        print(lst_cat)
        #dic_cat_prod = {'clave1':lst_prod_aux[]
        for indice in range(len(lst_cat)):
            #print(lst_cat[indice])
            flag=0
            for indice2 in range(len(lst_cat_prod)):
                if lst_cat[indice] == lst_cat_prod[indice2]:
                    if flag == 0:
                        print('Categoria de producto: ' + str(lst_cat[indice]))
                        flag=1
                    else:
                        print('\t' + str(lst_cat_prod[indice2+1]))
        print(dic_cat_prod)
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
        print("* * * SISTEMA TERMINADO * * *")





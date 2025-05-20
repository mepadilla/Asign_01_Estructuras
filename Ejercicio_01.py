# Ejercicio 0: Gestión de horarios.
#Descripción:
#Dado un archivo de texto “horarios.txt” con la siguiente información:
#año; departamento; código; asignatura; sección; profesor; LU0800 SD1 LU0850 SD1 MI0800 SD1 MI0850 SD1
#El horario tiene la misma estructura de la presentada en la página de control de estudios, la misma contiene el
#día, la hora y el aula. Utilice datos estructurados para la elaboración del script.
#Realice funciones para:
#1. Profesores por departamento.
#2. Determinar el horario más frecuente.
#3. El día más frecuente.
#4. La hora más frecuente.
#5. Cantidad de secciones por cátedra de cada departamento.
#6. Cantidad de asignaturas de Estudios Básicos por semestre, el tercer carácter del código representa el
#semestre y el cuarto indica que es de Estudia Básicos si es el carácter B.
#7. Aula más utilizada cada día.
#8. Menú de opciones.
lst_txt_b=[]
with open("horarios.txt") as archivo:
    for linea in archivo:
        str_txt_a = linea
        lst_txt_b.append(str_txt_a.split(';'))
#print(lst_txt_b)
for elemento in lst_txt_b:
    print(elemento)
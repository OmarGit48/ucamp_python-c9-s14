# f_archivo = open('archivo1.txt', 'w') # w = crite (escribir) escribir nuevo archivo o sogre escribir el archivo
# print(f_archivo)
# f_archivo.write('hola munndo!')
# f_archivo.close()

# #sobre escribiendo, se borra lo que estaba escrito
# f_archivo = open('archivo1.txt', 'w')
# f_archivo.write('Este es mi primero archivo')
# f_archivo.close()

# f_lectura = open('archivo1.txt', 'r') # r = read (leer) leer el archivo
# print(f_lectura.read())
# f_lectura.close()

# print(f_archivo)
# print(f_lectura)

#################################################
# Sentencias with y as

# f_lectura = open('archivo1.txt', 'r')
# print(f_lectura.closed)
# f_lectura.close()
# print(f_lectura.closed)

# with open('archivo1.txt', 'r') as f_lectura:
#     print(f_lectura.closed)
# print(f_lectura.closed)    

# para seguir escribiendo al final del archivo
# with open('archivo1.txt', 'a') as f_archivo: # a = append (agregar) agregar al final del archivio
#     f_archivo.write('\nEste archivo es mi primer archivo 2')
#     f_archivo.write('Este archivo es el primer archivo 3')
#     f_archivo.write('\n')
#     f_archivo.write('\tEste es el rpimer archivo 4')
# with open('archivo1txt', 'r') as f_lectura:
#     contenido = f_lectura.read()
#     print(f'****{contenido}****')
#     contenido = f_lectura.read()
#     print(f'****{contenido}****')
#     # print(f_lectura.read())
    
   #######################################
   # Lectura dearchivos linea a linea
   
# with open('archivo1.txt', 'r')  as f_lectura:
#     numero_de_lineas = 0
#     for i in f_lectura:
#         numero_de_lineas += 1
#         print (f'linea a{numero_de_lineas}: {i}')
#     print(f'El archivo tiene {numero_de_lineas} lineas')

#  Creando una lista a partir de un archivo

with open('archivo1.txt', 'r') as f_archivo:
    lista_archivo = f_archivo.readline()
    print(lista_archivo)
 
# print(lista_archivo)   
    
lista_archivo[1] = 'Este es mi primer archivo 2\n' 
lista_archivo.insert(2, 'Este es mi primer archivo 3\n')
    
print(lista_archivo)

with open('archivo1.txt', 'w') as f_archivo:
    f_archivo.writelines(lista_archivo)
        
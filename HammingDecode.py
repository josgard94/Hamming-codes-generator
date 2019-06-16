"""
	Centro de Investigacion y Estudios Avanzados del IPN

	Codificacion y compresion de datos.

	Edgard Jose Diaz Tipcamu.
	ediaz@tamps.convestav.mx
	04 - abril - 2019

"""

import numpy as np

######################################################################
#	Matriz transpuesta  construida apartir de la matrix Hamming 7
######################################################################
H = np.array([[0,1,1],
			  [1,0,1],
			  [1,1,0],
			  [1,1,1],
			  [1,0,0],
			  [0,1,0],
			  [0,0,1]],dtype=np.int32)

lista = np.array(np.zeros((1,7)),dtype=np.int32)


###############################################################################################
#	En este metodo se calcula el sindrome,  para saber si existe un error en la palabra codigo.
###############################################################################################
def sindrome(array):
	a = np.array(array,dtype=np.int32)
	aux = [0,0,0]#np.array(np.zeros((1,3)),dtype=np.int32);
	
	for i in range(0,3):
		suma = 0;
		for j in range(0,7):
			suma = suma + (a[0,j] * H[j][i])
		aux[i] = int(suma%2)

	return aux

###############################################################################################
#	En este metodo se realiza la decodificacion de las palabras quitando los bit de redundancia
###############################################################################################
def decodificar(array):
	palabra_decodificada=[0,0,0,0]
	for i in range(0,4):
		palabra_decodificada[i] = array[0,i]

	return palabra_decodificada;

##############################################################################################
###	 En este metodo se verifica si la palabra que se esta evalueando tiene errores
###	 de ser asi se corrige y se guarda en un archivo de salida.
##############################################################################################

def verificar_palabra(res,lista):

	x1 = np.array(np.zeros((1,4)),dtype= np.int32)
	bandera = 0;
	indice = 0;
	a = np.array(lista,dtype=np.int32)
	for i in range(0,7):
		if((res[0] == H[i][0]) and (res[1] == H[i][1]) and (res[2] == H[i][2] )):
			indice = i; 
			bandera = 1;

	if(bandera == 1):
		print "Se decto un error en la palabra "+ str(lista) +" en el bit "+str(indice)+" y se corrigio."
		if(lista[0,indice]== 1):
			lista[0,indice] = 0
			print (str(lista) + " palabra corregida")
		else:
			lista[0,indice] = 1
			print (str(lista) + " palabra corregida")
	
	x1 = decodificar(lista)
	return x1;


###################################################################################
###										main									###
###################################################################################

file = open("Hamming.txt","r")
txt = (file.read().rstrip())
file.close()
con = 0;
x = np.array(np.zeros((1,4)),dtype= np.int32)
file2 = open("decodificacion.txt","w")
for ch in txt:
	if ch != '\n':
		lista[0,con] = ch
		con = con + 1
		if con == 7:
			res = sindrome(lista)
			con = 0;
			x = verificar_palabra(res,lista)
			for i in range(0,4):
				file2.write(str(x[i]));	
			file2.write("\n");


file2.close()

"""
	Autor: Edgard Jose Diaz Tipcamu.
	e.diaz@nartsoft.com.mx
	04 - abril - 2019
"""

import numpy as np
###############################################################################
#			Matriz generadora de Hamming H7 en su forma sistematica			  #
###############################################################################

G = np.array([[1,0,0,0,0,1,1], 
	 		  [0,1,0,0,1,0,1],
	 		  [0,0,1,0,1,1,0], 
	 		  [0,0,0,1,1,1,1]],dtype=np.int32)
k = 0;

################################################################################
#	En este metodo se realiza la codificacion de las palabras				   #
################################################################################

def Hammin_code(array):
	a = np.array(array,dtype=np.int32)
	aux = np.array(np.zeros((1,7)),dtype=np.int32);
	for i in range(0,7):
		suma = 0
		for j in range(0,4):
			suma = suma +(a[0,j] * G[j][i]);
		aux[0,i] = int(suma%2);
	return aux

##############################################################################
#    						Inicia main										 #
##############################################################################
lista = np.array(np.zeros((1,4)),dtype=np.int32)
file = open("codigos.txt","r")
txt = (file.read().rstrip())
file.close() 
palabra = ""
con = 0;
res = np.array(np.zeros((1,7)),dtype= np.int32)
file2 = open("Hamming.txt","w");
for ch in txt:
	if ch != '\n':
		lista[0,con] = ch
		con = con + 1
		if con == 4:
			res = Hammin_code(lista)
			for i in range(0,7):
				file2.write(str(res[0,i]))
			file2.write("\n")
			k = k + 1;
			con = 0
file2.close()
print "Codigos de Hamming";
file3 = open("Hamming.txt","r")
txt3 = (file3.read().rstrip())
file3.close() 
print txt3

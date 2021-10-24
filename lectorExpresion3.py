import string
from typing import List


file = open("expresion.txt", "r")
oracion = file.readlines()[0]
file.close()

list_parentesis=[]
list_suma = []
list_asterisco = []

print(oracion)


def cargar_expresion():
    print(len(oracion))
    valor = 0
    general = []
    aux_array = []
    while(valor < len(oracion)):
        if(oracion[valor] == "("):
            if(len(aux_array)>0):
                general.append(aux_array.copy())
                aux_array.clear()       ##comprobar si el bloque grande esta elevado a algo 
            valor,bloque = parentesis(valor+1)
            print("este es el bloque final final",bloque)
            if(valor+1 <len(oracion)):
                if(oracion[valor+1] == "^"):
                    aux = [bloque,oracion[valor+1] +oracion[valor+2]]
                    general.append(aux)
                    valor+=3 
                else:
                    general.append(bloque)  
            else:
                general.append(bloque)  
        else:
            if(oracion[valor] == "^"):
                aux_array.append(oracion[valor]+oracion[valor+1])
                valor+=2
            else:
                if(oracion[valor]!= ")" and oracion[valor]!= "("):
                    aux_array.append(oracion[valor])
                valor+=1
            if(valor>= len(oracion) and len(aux_array)>0):
                    general.append(aux_array)

    print("este es el arreglo general \n",general)
    return general


    
def parentesis(valor):
    inicio = 0 ## que es una varieable que te permite saber si encutre mas parentesis adentro 
    new_array = [] ## arreglo que contreda todo el bloque en listas (lista de listas)
    bandera = True ## te dejara salir del while una vez cerrado el bloque 
    aux_array = [] ## aux te permite guardar todo lo de los bloque chicos que se integrara  a new array 
    aux_aux = []
    while(bandera):
        if(oracion[valor] == "^"):
            if(oracion[valor+1] == "+"):
                aux_array.append(oracion[valor] + oracion[valor+1])
                if (valor +2 >= len(oracion)-1):
                    # aqui termina
                    bandera = False
                else:
                    valor +=2
            else:
                aux_array.append(oracion[valor] + oracion[valor+1])
                if (valor +2 >= len(oracion)-1):
                    # aqui termina
                    bandera = False
                else:
                    valor +=2
                # encontro una elevacion de cero a mas
            new_array.append(aux_array)
            print("este es el arreglo final",new_array)
            
        elif(oracion[valor]== "("):
            if(len(aux_array) >0):
                valor, bloque = parentesis(valor+1)

                aux_array.append(bloque)
            else:
                valor +=1
            inicio +=1
        
        elif(oracion[valor]==")"):
            if(inicio != 0):
                # acabo el bloque chico 
                if( oracion[valor +1]== "^"):
                    # aux_array.append(oracion[valor+1] + oracion[valor+2])
                    if(len(new_array)==0):
                        new_array = [aux_array.copy(),oracion[valor+1] + oracion[valor+2]]
                    else:
                        new_array.append(aux_array.copy())
                        new_array.append(oracion[valor+1] + oracion[valor+2])
                    aux_array.clear()
                    valor +=3
                else:    
                    if(len(new_array)==0):
                        new_array = aux_array.copy()
                    else:
                        new_array.append(aux_array.copy())
                    aux_array.clear()
                    valor +=1
                inicio -= 1
            else:
                if(len(new_array) == 0):
                    new_array = aux_array.copy()
                bandera = False
        else:
            aux_array.append(oracion[valor])
            valor +=1
    print("este es el arreglo final",new_array)
    return valor,new_array

def leerBloquesSimples(lista:list):
    
    for i in range(len(lista)):
        tieneLista = False
        for j in range(len(lista[i])):
            if(type(lista[i][j])==list):
                tieneLista = True


        if(not tieneLista):
            print("es un bloque simple",lista[i])
            listaAuxiliar = []
            cadenaAuxiliar = ""
            for j in range(len(lista[i])):
            
                if(lista[i][j]=="+" ):
                    if(j==0):
                        print("es un bloque anidado con un or")
                    else:
                        # print("entro a la lista con el valor",cadenaAuxiliar)
                        listaAuxiliar.append([cadenaAuxiliar])
                        cadenaAuxiliar=""
                else:
                    # print("entroa agregar la letra", lista[i][j])
                    # if(lista[i][j]=="^*"):  
                    cadenaAuxiliar += lista[i][j]
                    if(j==len(lista[i])-1):
                        listaAuxiliar.append([cadenaAuxiliar])

            print(listaAuxiliar)
            


general = cargar_expresion()
print("\n")
leerBloquesSimples(general)
import string

# simbologia 
# 0 = se repite 0 o mas veces
# 1 = se repite una o mas veces 
# 2 = aparece awebo 1 vex
# 3 = es un or 

file = open("expresion.txt", "r")
oracion = file.readlines()[0]
file.close()

# def leerArchivo(path):
#     global oracion
#     file = open(path, "r")
#     oracion = file.readlines()
#     file.close()

# list_abecedario = list(string.ascii_lowercase);
# list_numeros= [str(x) for x in range(10)]
# list_simbolos = ["@","-","_",",","."]

list_parentesis=[]
list_suma = []
list_asterisco = []

print(oracion)


def lector_expresion():
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
            if(oracion[valor+1] == "^"):
                bloque.append(oracion[valor+1] +oracion[valor+2])
                general.append(bloque)
                valor+=2 
            else:
                general.append(bloque)
        else:
            aux_array.append(oracion[valor])
        valor+=1
    print(general)


    
def parentesis(valor):
    inicio = 0 ## que es una varieable que te permite saber si encutre mas parentesis adentro 
    new_array = [] ## arreglo que contreda todo el bloque en listas (lista de listas)
    bandera = True ## te dejara salir del while una vez cerrado el bloque 
    aux_array = [] ## aux te permite guardar todo lo de los bloque chicos que se integrara  a new array 
    aux_aux = []
    while(bandera):
        print(valor,oracion[valor-1])
        if(oracion[valor] == "^"):
            if(oracion[valor+1] == "+"):
                print("entre a la elevacion")
                aux_array.append(oracion[valor] + oracion[valor+1])
                if (valor +2 >= len(oracion)-1):
                    # aqui termina
                    print("aqui termino")
                    bandera = False
                else:
                    valor +=2
            else:
                aux_array.append(oracion[valor] + oracion[valor+1])
                print("entre a la elevacion dos")
                if (valor +2 >= len(oracion)-1):
                    # aqui termina
                    print("aqui termino")
                    bandera = False
                else:
                    valor +=2
                # encontro una elevacion de cero a mas
            new_array.append(aux_array)
            print("este es el arreglo final",new_array)
            
        elif(oracion[valor]== "("):
            print("encontre otro bloque")
            if(len(aux_array) >0):
                print("entre a recursividad")
                valor, bloque = parentesis(valor+1)
                print("sali de recursividad")

                aux_array.append(bloque)
            else:
                valor +=1
            inicio +=1
        
        elif(oracion[valor]==")"):
            if(inicio != 0):
                # acabo el bloque chico 
                print("acabe un bloque que encontre") 
                if( oracion[valor +1]== "^"):
                    aux_array.append(oracion[valor+1] + oracion[valor+2])
                    new_array.append(aux_array.copy())
                    aux_array.clear()
                    valor +=3
                else:    
                    print("pa saber que hay ",aux_array)
                    new_array.append(aux_array.copy())
                    aux_array.clear()
                    valor +=1
                inicio -= 1
            else:
                if(len(new_array) == 0):
                    new_array.append(aux_array.copy())
                print("ya termmine toodoooo")
                bandera = False
        else:
            aux_array.append(oracion[valor])
            print("encontre una letra",aux_array)
            valor +=1
    print("este es el arreglo final",new_array)
    return valor,new_array
        
def limpiar_array(array):
    for i in range(len(array)):
        if(len(array) > 1):
            if(type(array[i])== list):
                array[i] =limpiar_array(array[i])
        else:
            return array[i]
            


lector_expresion()
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
    global list_parentesis

    for valor in range(len(oracion)):
        if(oracion[valor] == "("):
            list_parentesis.append(["inicio",valor])
        if(oracion[valor] == ")"):
            list_parentesis.append(["cierre",valor])
    list_parentesis = union_arrelgo(list_parentesis)
    print(list_parentesis)
    extraer(list_parentesis)

    
def union_arrelgo(arreglo):
    i =0
    new_array = []
    while(i<len(arreglo)):
        inicio =0
        valor = arreglo[i]
        if(valor[0]=="inicio"):
            for j in range(i+1,len(arreglo)):
                if(arreglo[j][0] == valor[0]):
                    inicio+=1
                else:
                    if(inicio != 0):
                        inicio-=1
                    else:
                        valor += arreglo[j]
                        # i =j
                        break
            new_array.append(valor)
        i+=1
    return new_array
    
def extraer(list_extraer):
    aux = []
    for valor in list_extraer:
        aux.append(oracion[valor[1]:valor[3]+1])
    print(aux)



lector_expresion()
import string

# simbologia 
# 0 = se repite 0 o mas veces
# 1 = se repite una o mas veces 
# 2 = aparece awebo 1 vex
# 3 = es un or 

file = open("expresion.txt", "r")
oracion = file.readlines()[0]
file.close()

def leerArchivo(path):
    global oracion
    file = open(path, "r")
    oracion = file.readlines()
    file.close()

list_abecedario = list(string.ascii_lowercase);
list_numeros= [str(x) for x in range(10)]
list_simbolos = ["@","-","_",",","."]
list_general = []
print(list_numeros)
print(oracion)
print(len(oracion))
contador=0


def lector_expresion():
    global contador
    while(contador < len(oracion)):
        # simple rango 
        if(oracion[contador] == "["):
            if(oracion[contador+2] == "-"):
                print("encontre el inicio de un corchete ")
                contador+=1
                obtenerRango(contador)
            else:
                print("encontre el inicio de un corchete no es rango")
                contador+=1
                obtenerUnicos(contador)
        # bloque
        if(oracion[contador] == "("):
            print("encontre el inicio del bloque ")
            contador+=1
            bloque(contador)
            list_general.append([4,"bloque"])
        contador+=1
        print(contador)
        # break
    print(list_general)


def obtenerRango(contador):
    bandera = True
    list_rango=[]

    while(bandera):
        if(oracion[contador + 1] == "-"):
            primer_valor = oracion[contador]
            segundo_valor = oracion[contador+2]
            if(list_abecedario.__contains__(primer_valor)):
                list_rango.append(list_abecedario[list_abecedario.index(primer_valor):list_abecedario.index(segundo_valor)+1])
            if(list_numeros.__contains__(primer_valor)):
                list_rango.append(list_numeros[list_numeros.index(primer_valor):list_numeros.index(segundo_valor)+1])
            contador +=3
        if(oracion[contador] == "]"):
            union = []
            for valor in list_rango:
                union += valor
            if(oracion[contador+1] == "*"):
                list_general.append([0,union])
                contador +=1
                # se repite cero o mas de 
            else:
                if(oracion[contador+1] == "+"):
                    list_general.append([1,union])
                    contador +=1
                # se repite una o mas  o mas d
                else:
                    list_general.append([2,union])
                    # unica vez
            bandera = False

def obtenerUnicos(contador):
    bandera = True
    list_rango=[]

    while(bandera):
        if(list_abecedario.__contains__(oracion[contador])):
            list_rango.append(list_abecedario[oracion[contador]])
        if(list_numeros.__contains__(oracion[contador])):
            list_rango.append(oracion[contador])
        if(list_simbolos.__contains__(oracion[contador])):
            list_rango.append(oracion[contador])
        contador+=1
        if(oracion[contador]== "]"):
            bandera = False
    union = []
    for valor in list_rango:
        union += valor
    list_general.append([2,union])

def bloque(contador):
    bandera = True
    while(bandera):
        if(oracion[contador] == ")"):
            bandera = False
        contador +=1

lector_expresion()
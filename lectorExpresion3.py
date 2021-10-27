import re

er:str

def adaptarExprecionRegular(exprecionRegular:str):
    global er
    print(exprecionRegular)
    er = exprecionRegular.replace(" ","").replace("^*","*").replace("+","|").replace("^|","+").replace(".","")
    


def comprobarER(exprecion,cadena):
    adaptarExprecionRegular(exprecion)
    valdator = re.compile(er)
    match =valdator.match(cadena)
    try:
        valida = match.group()==cadena
    except (TypeError, AttributeError):
        valida = False
    return  valida




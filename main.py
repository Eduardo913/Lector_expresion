import lectorExpresion3 as er
import tkinter as tk
window = tk.Tk()
window.title("sintaxis")
window.geometry("500x500")
window.resizable(False, False)
window.config(bg="#D3C3C3")

# entrysvalue
exprecionR = tk.StringVar()
cadena = tk.StringVar()
resultado = tk.StringVar()

# functions
def comprobar():
    resultado.set("hola")    

# labels
tk.Label(window,text="escribe la ER y despues la cadena a verificar",font=('Calibri', 14),background="#D3C3C3").place(x=90,y=50)
tk.Label(window,text="ejemplo: abcd^*+((a+b)^++(a+c+#))^*",font=('Calibri', 14),background="#D3C3C3").place(x=130,y=100)
tk.Label(window,text="escribe la ER",font=('Calibri', 14),background="#D3C3C3").place(x=205,y=150)
tk.Label(window,text="escribe la cadena a verificar",font=('Calibri', 14),background="#D3C3C3").place(x=140,y=250)
tk.Label(window,textvariable=resultado,font=('Calibri', 14),background="#D3C3C3").place(x=200,y=390)

# entrys
tk.Entry(window,textvariable=exprecionR,font=('Calibri', 14)).place(x=150,y=200)
tk.Entry(window,textvariable=cadena,font=('Calibri', 14)).place(x=150,y=310)

# buton
tk.Button(window,font=('Calibri', 14),text="comprobar",command=comprobar,).place(x=200,y=430)

window.mainloop()
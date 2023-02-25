from tkinter import *
from tkinter import messagebox

BelongTo = True
counter_values = 0
Preanalisis = ""
Expression = ""

#------------------------------------------------
#------------- PRESIONAR BOTON ------------------
#------------------------------------------------
def Button_Consult():
    global Expression, counter_values, BelongTo
    set_Values()
    Expr()
    if BelongTo and counter_values == len(Expression) - 1:
        messagebox.showinfo("Sintaxis","Pertenece al lenguaje")
    else:
        messagebox.showerror("Error", "Error: No pertenece al lenguaje")
    initial_values()

def set_Values():
    global Preanalisis, Expression
    Expression = value.get() + " "
    Preanalisis = Expression[0]

def initial_values():
    global counter_values, BelongTo, txtExpression
    counter_values = 0
    BelongTo = True

# ------------------------------------------------
# ----------------- COINCIDIR --------------------
# ------------------------------------------------

def Coincidir(t):
    global Preanalisis, counter_values, Expression
    counter_values = counter_values + 1
    if (Preanalisis == t and counter_values < len(Expression)):   
        Preanalisis = Expression[counter_values]

# ------------------------------------------------
# ------------------ REGLAS ----------------------
# ------------------------------------------------

def Expr():
    Term()
    Resto_Expr()

def Resto_Expr():
    if (Preanalisis == '+'):
        Coincidir('+')
        Term()
        Resto_Expr()
    elif (Preanalisis == '-'):
        Coincidir('-')
        Term()
        Resto_Expr()
    else:
        pass

def Term():
    Factor()
    Resto_Term()

def Resto_Term():
    if (Preanalisis == '*'):
        Coincidir('*')
        Factor()
        Resto_Term()
    elif (Preanalisis == '/'):
        Coincidir('/')
        Factor()
        Resto_Term()
    else:
        pass

def Factor():
    global BelongTo
    if (Preanalisis == '0'):
        Coincidir('0')
    elif (Preanalisis == '1'):
        Coincidir('1')
    elif (Preanalisis == '2'):
        Coincidir('2')
    elif (Preanalisis == '3'):
        Coincidir('3')
    elif (Preanalisis == '4'):
        Coincidir('4')
    elif (Preanalisis == '5'):
        Coincidir('5')
    elif (Preanalisis == '6'):
        Coincidir('6')
    elif (Preanalisis == '7'):
        Coincidir('7')
    elif (Preanalisis == '8'):
        Coincidir('8')
    elif (Preanalisis == '9'):
        Coincidir('9')
    elif (Preanalisis == "("):
        Coincidir('(')
        Expr()
        Coincidir(')')
    else:
        BelongTo = False

# ------------------------------------------------
# ----------------- INTERFAZ ---------------------
# ------------------------------------------------

root = Tk()
root.title("Analizador SDP")
root.geometry("300x150")
root.config(bg="gray85")

lblExpression = Label(root, text="Expresion: ",bg="gray85").place(x=20, y=20)
value = StringVar()
txtExpression = Entry(root,textvariable=value ,width=20).place(x=100, y=20)

btnConsult = Button(root, text="Consultar",command=Button_Consult, bd="5").place(x=40, y=60)

root.mainloop()

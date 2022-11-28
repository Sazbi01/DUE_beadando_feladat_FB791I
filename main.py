from tkinter import *
from calculating import *

calc = operation()
isClearable = [False]

#függvények
def insert(value):
    current = lbl_result['text']
    if (isClearable[0]):
        if (value == '.'):
            return
        else:
            current = ''
            isClearable[0] = False
    if (int(str(len(current))) < 12):
        if (value == '.' and '.' in current):
            return
        if (current == '0' and value == '0'):
            return
        elif (current == '0' and value != '0'):
            if value != '.':
                current = ''
        lbl_result.config(text=current + value)


def insertPi():
    lbl_result.config(text=str(calc.pi())[0:12])

def clear():
    if (isClearable[0]):
        clearAll()
    else:
        current = lbl_result['text']
        length = int(str(len(current)))
        if current == '0':
            return
        elif length == 1:
            lbl_result.config(text='0')
        else:
            lbl_result.config(text=current[0:length-1])

def clearAll():
    lbl_result.config(text='0')
    calc.o = ''
    calc.x = 0
    calc.y = 0

def showNegate():
    value = lbl_result['text']
    if(value != '0' and value[-1] != '.'):
        if(value[0] == '-'):
            value = value[1:]
        else:
            value = '-' + value

        lbl_result.config(text=value)

def enterOperation(o):
    value = lbl_result['text']
    if(value[-1] != '.' and calc.x == 0):
        calc.o = o
        calc.x = float(value)
        isClearable[0] = True
    elif(calc.x != 0):
        showResult(o)

def showResult(o):
    value = lbl_result['text']
    if (value[-1] != '.' and calc.o != ''):
        calc.y = float(value)
        result = calc.result()
        if (int(result) == result):
            result = int(result)
            result = str(result)
        else:
            result = str(result)
            while (result[-1] == '0'):
                result -= result[-1]
        isClearable[0] = True
        if (o != ''):
            calc.o = o
            calc.x = float(result)
            calc.y = 0
        else:
            calc.o = ''
            calc.x = 0
            calc.y = 0
        lbl_result.config(text=result[0:12])

def showSqrt():
    value = lbl_result['text']
    if (value[-1] != '.' and value != '0'):
        result = calc.sqrt(float(value))
        if (int(result) == result):
            result = int(result)
            result = str(result)
        else:
            result = str(result)
            while (result[-1] == '0'):
                result -= result[-1]
        isClearable[0] = True
        lbl_result.config(text=result[0:12])

#ablak felépítése
window = Tk()
window.title('Számológép')
window.resizable(False, False)
window.geometry('429x639')
window.configure(bg='#101010')

lbl_result = Label(window, width=14, height=2, text='0', font=('Verdana', 38), bg='#E3E3E3', anchor='e')
lbl_result.pack()

Button(window, text='CE', width=4, height=1, font=('arial', 28), bd=1, fg='#000000', bg='#E6790E', command=lambda: clearAll()).place(x=10, y=145)
Button(window, text='M+', width=4, height=1, font=('arial', 28), bd=1, fg='#000000', bg='#FBFBFB').place(x=115, y=145)
Button(window, text='M-', width=4, height=1, font=('arial', 28), bd=1, fg='#000000', bg='#FBFBFB').place(x=220, y=145)
Button(window, text='MR', width=4, height=1, font=('arial', 28), bd=1, fg='#000000', bg='#FBFBFB').place(x=325, y=145)

Button(window, text='C', width=4, height=1, font=('arial', 28), bd=1, fg='#000000', bg='#A35508', command=lambda: clear()).place(x=10, y=227)
Button(window, text='π', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insertPi()).place(x=115, y=227)
Button(window, text='√', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: showSqrt()).place(x=220, y=227)
Button(window, text='/', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: enterOperation('/')).place(x=325, y=227)

Button(window, text='7', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('7')).place(x=10, y=309)
Button(window, text='8', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('8')).place(x=115, y=309)
Button(window, text='9', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('9')).place(x=220, y=309)
Button(window, text='*', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: enterOperation('*')).place(x=325, y=309)

Button(window, text='4', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('4')).place(x=10, y=391)
Button(window, text='5', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('5')).place(x=115, y=391)
Button(window, text='6', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('6')).place(x=220, y=391)
Button(window, text='-', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: enterOperation('-')).place(x=325, y=391)

Button(window, text='1', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('1')).place(x=10, y=473)
Button(window, text='2', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('2')).place(x=115, y=473)
Button(window, text='3', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('3')).place(x=220, y=473)
Button(window, text='+', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: enterOperation('+')).place(x=325, y=473)

Button(window, text='+/-', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: showNegate()).place(x=10, y=555)
Button(window, text='0', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('0')).place(x=115, y=555)
Button(window, text='.', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#4C4C4C', command=lambda: insert('.')).place(x=220, y=555)
Button(window, text='=', width=4, height=1, font=('arial', 27, 'bold'), bd=1, fg='#000000', bg='#AD1717', command=lambda: showResult('')).place(x=325, y=555)

window.mainloop()

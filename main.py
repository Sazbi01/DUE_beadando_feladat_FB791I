from tkinter import *
from calculating import *

#függvények
def insert(value):
    current = lbl_result['text']
    if int(str(len(current))) < 12:
        if current == '0' and value == '0':
            return
        elif current == '0' and value != '0':
            if value != '.':
                current = ''
        lbl_result.config(text=current + value)

def clear():
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

def showNegate():
    value = lbl_result['text']
    if value != '0' and value != '0.':
        lbl_result.config(text=negate(value))

#ablak felépítése
window = Tk()
window.title('Számológép')
window.resizable(False, False)
window.geometry('429x639')
window.configure(bg='#101010')

lbl_result = Label(window, width=14, height=2, text='0', font=('Verdana', 38), bg='#E3E3E3', anchor='e')
lbl_result.pack()

Button(window, text='M+', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=10, y=145)
Button(window, text='M-', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=115, y=145)
Button(window, text='MR', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=220, y=145)
Button(window, text='√', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=145)

Button(window, text='C', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: clear()).place(x=10, y=227)
Button(window, text='CE', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: clearAll()).place(x=115, y=227)
Button(window, text='π', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=220, y=227)
Button(window, text='/', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=227)

Button(window, text='7', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('7')).place(x=10, y=309)
Button(window, text='8', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('8')).place(x=115, y=309)
Button(window, text='9', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('9')).place(x=220, y=309)
Button(window, text='*', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=309)

Button(window, text='4', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('4')).place(x=10, y=391)
Button(window, text='5', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('5')).place(x=115, y=391)
Button(window, text='6', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('6')).place(x=220, y=391)
Button(window, text='-', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=391)

Button(window, text='1', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('1')).place(x=10, y=473)
Button(window, text='2', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('2')).place(x=115, y=473)
Button(window, text='3', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('3')).place(x=220, y=473)
Button(window, text='+', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=473)

Button(window, text='+/-', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: showNegate()).place(x=10, y=555)
Button(window, text='0', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('0')).place(x=115, y=555)
Button(window, text='.', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040', command=lambda: insert('.')).place(x=220, y=555)
Button(window, text='=', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=555)

window.mainloop()

from tkinter import *

#ablak felépítése
window = Tk()
window.title('Számológép')
window.resizable(False, False)
window.geometry('429x639')
window.configure(bg='#101010')

lbl_result = Label(window, width=16, height=2, text='', font=('Verdana', 38), bg='#E3E3E3', anchor='e')
lbl_result.pack()

Button(window, text='M+', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=10, y=145)
Button(window, text='M-', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=115, y=145)
Button(window, text='MR', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=220, y=145)
Button(window, text='√', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=145)

Button(window, text='C', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=10, y=227)
Button(window, text='CE', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=115, y=227)
Button(window, text='π', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=220, y=227)
Button(window, text='/', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=227)

Button(window, text='7', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=10, y=309)
Button(window, text='8', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=115, y=309)
Button(window, text='9', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=220, y=309)
Button(window, text='*', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=309)

Button(window, text='4', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=10, y=391)
Button(window, text='5', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=115, y=391)
Button(window, text='6', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=220, y=391)
Button(window, text='-', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=391)

Button(window, text='1', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=10, y=473)
Button(window, text='2', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=115, y=473)
Button(window, text='3', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=220, y=473)
Button(window, text='+', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=473)

Button(window, text='+/-', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=10, y=555)
Button(window, text='0', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=115, y=555)
Button(window, text='.', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=220, y=555)
Button(window, text='=', width=4, height=1, font=('arial', 28), bd=1, fg='#FFFFFF', bg='#404040').place(x=325, y=555)

window.mainloop()
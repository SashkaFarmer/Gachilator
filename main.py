from tkinter import *
from tkinter import messagebox
from math import sqrt
from PIL import ImageTk, Image
from tkinter import ttk
from pictures import *
from winsound import *

PlaySound('sounds\\gachi_ost.wav', SND_FILENAME | SND_ASYNC | SND_LOOP)


def add_digit(digit):
    value = calc.get()
    if value == '0':
        value = value[1:]
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value+digit)
    calc['state'] = DISABLED

def add_operation(operation):
    value = calc.get()
    if value[-1] in '/*-+':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value+operation)
    calc['state'] = DISABLED

def add_float(float):
    value = calc.get()
    if value[-1] == float:
        value = value[:-1]
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value+float)
    calc['state'] = DISABLED

def add_square():
    value = calc.get()
    try:
       value = float(value)
       value = sqrt(value)
    except ValueError:
        messagebox.showinfo('ОшибОчка', 'Сначала нажми равно или хз как ты сюда попал')
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value)
    calc['state'] = DISABLED

def add_pow():
    value = calc.get()
    try:
       value = float(value)
       value = (value**2)
    except OverflowError:
        messagebox.showinfo('ОшибОчка', 'Слишком больше число')
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value)
    calc['state'] = DISABLED


def calculate():
    value = calc.get()
    if value[-1] in '/*-+':
        value = value+value[:-1]
    calc['state'] = NORMAL
    calc.delete(0, END)
    try:
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo('Ты чё?', 'На нолье вообще-то нельзя делить', icon='warning')
        calc.insert(0, 0)
    except SyntaxError:
        messagebox.showinfo('Нельзя использовать две точки',
                            'Я пока не знаю как это решить, поэтому пусть будет так')
        calc.insert(0, 0)
    calc['state'] = DISABLED

def clear():
    value = calc.get()
    value = value[:-1]
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value)
    calc['state'] = DISABLED


def clear_all():
    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, 0)
    calc['state'] = DISABLED

def press_number(butt):
    print(repr(butt.char))
    if butt.char.isdigit():
        add_digit(butt.char)
    elif butt.char in '/*-+':
        add_operation(butt.char)
    elif butt.char == '\r':
        calculate()


root = Tk()
root.title('♂Гачилятор♂')
root.iconphoto(False, PhotoImage(file='pictures\\billy.png'))
root['bg'] = '#78c6cf'
root.geometry('450x600+1050+200')
root.resizable(False, False)
root.bind('<Key>', press_number)


calc = Entry(root, justify=RIGHT, width=19, font=('ProductSans', 20))
calc.insert(0, 0)
calc.place(x=80, y=60)
calc['state'] = DISABLED


def song_on():
    PlaySound('sounds\\gachi_ost.wav', SND_FILENAME | SND_ASYNC | SND_LOOP)

def song_off():
    PlaySound('sounds\\fuck_you.wav', SND_FILENAME | SND_ASYNC)

var = IntVar()
var.set(0)

check_on = Radiobutton(text='🔊', value=0, command=song_on, variable=var, bg='#78c6cf',
                        activebackground='#78c6cf', font='ProductSans 15')
check_on.place(x=5, y=570)

check_off = Radiobutton(text='🔈', value=1, command=song_off, variable=var, bg='#78c6cf',
                        activebackground='#78c6cf', font='ProductSans 15')
check_off.place(x=55, y=570)


# Я пытался засунуть эти кнопки в функции, что бы сократить код и не нарушать принцип DRY,
# но в таком случае не отображаются картинки, пытался найти решение, но не смог

image = ImageTk.PhotoImage(img)
btn = Button(root, image=image, text='a^2', compound='center', command=add_pow,
             fg='White', activeforeground='#78c6cf', font='ProductSans 19',
             height=48, width=48, borderwidth=0)
btn.place(x=80, y=120)

image1 = ImageTk.PhotoImage(img1)
btn1 = Button(root, image=image1, text='√', compound='center', command=add_square,
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
              height=48, width=48, borderwidth=0)
btn1.place(x=160, y=120)

image2 = ImageTk.PhotoImage(img2)
btn2 = Button(root, image=image2, text='CE', compound='center', command=clear,
              fg='White', activeforeground='#78c6cf', font='ProductSans 23',
              height=48, width=48, borderwidth=0)
btn2.place(x=240, y=120)

image3 = ImageTk.PhotoImage(img3)
btn3 = Button(root, image=image3, text='AC', compound='center', command=clear_all,
              fg='White', activeforeground='#78c6cf', font='ProductSans 23',
              height=48, width=48, borderwidth=0)
btn3.place(x=320, y=120)

image4 = ImageTk.PhotoImage(img4)
btn4 = Button(root, image=image4, text='7', compound='center', command=lambda: add_digit('7'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
              height=48, width=48, borderwidth=0)
btn4.place(x=80, y=200)

image5 = ImageTk.PhotoImage(img5)
btn5 = Button(root, image=image5, text='8', compound='center', command=lambda: add_digit('8'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
              height=48, width=48, borderwidth=0)
btn5.place(x=160, y=200)

image6 = ImageTk.PhotoImage(img6)
btn6 = Button(root, image=image6, text='9', compound='center', command=lambda: add_digit('9'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
              height=48, width=48, borderwidth=0)
btn6.place(x=240, y=200)

image7 = ImageTk.PhotoImage(img7)
btn7 = Button(root, image=image7, text='÷', compound='center', command=lambda: add_operation('/'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
              height=48, width=48, borderwidth=0)
btn7.place(x=320, y=200)

image8 = ImageTk.PhotoImage(img8)
btn8 = Button(root, image=image8, text='4', compound='center', command=lambda: add_digit('4'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
              height=48, width=48, borderwidth=0)
btn8.place(x=80, y=280)

image9 = ImageTk.PhotoImage(img9)
btn9 = Button(root, image=image9, text='5', compound='center', command=lambda: add_digit('5'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
              height=48, width=48, borderwidth=0)
btn9.place(x=160, y=280)

image10 = ImageTk.PhotoImage(img10)
btn10 = Button(root, image=image10, text='6', compound='center', command=lambda: add_digit('6'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn10.place(x=240, y=280)

image11 = ImageTk.PhotoImage(img11)
btn11 = Button(root, image=image11, text='×', compound='center', command=lambda: add_operation('*'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn11.place(x=320, y=280)

image12 = ImageTk.PhotoImage(img12)
btn12 = Button(root, image=image12, text='1', compound='center', command=lambda: add_digit('1'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn12.place(x=80, y=360)

image13 = ImageTk.PhotoImage(img13)
btn13 = Button(root, image=image13, text='2', compound='center', command=lambda: add_digit('2'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn13.place(x=160, y=360)

image14 = ImageTk.PhotoImage(img14)
btn14 = Button(root, image=image14, text='3', compound='center',command=lambda: add_digit('3'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn14.place(x=240, y=360)

image15 = ImageTk.PhotoImage(img15)
btn15 = Button(root, image=image15, text='–', compound='center', command=lambda: add_operation('-'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn15.place(x=320, y=360)

image16 = ImageTk.PhotoImage(img16)
btn16 = Button(root, image=image16, text='0', compound='center', command=lambda: add_digit('0'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn16.place(x=80, y=440)

image17 = ImageTk.PhotoImage(img17)
btn17 = Button(root, image=image17, text='•', compound='center', command=lambda: add_float('.'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn17.place(x=160, y=440)

image18 = ImageTk.PhotoImage(img18)
btn18 = Button(root, image=image18, text='=', compound='center', command=calculate,
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn18.place(x=240, y=440)

image19 = ImageTk.PhotoImage(img19)
btn19 = Button(root, image=image19, text='+', compound='center', command=lambda: add_operation('+'),
              fg='White', activeforeground='#78c6cf', font='ProductSans 28',
               height=48, width=48, borderwidth=0)
btn19.place(x=320, y=440)


root.mainloop()
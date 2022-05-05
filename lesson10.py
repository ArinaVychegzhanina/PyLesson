import tkinter #подкючаем модуль
window = tkinter.Tk()

label = tkinter.Label(window, text = "Это текст в окне!") #текст в окно
label.pack()
label1 = tkinter.Label(window,text = "Привет, мир!") #текст в окно
label1.pack()
window.mainloop() #открывается окно

import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
first = tkinter.Label(frame, text='First label')# групируем диджеты с помощью frame, можно менять параметры
first.pack()
second = tkinter.Label(frame, text='Second label')
second.pack()
third = tkinter.Label(frame, text='Third label')
third.pack()

window.mainloop()

import tkinter
window = tkinter.Tk()
data = tkinter.StringVar()
data.set('Данные в окне')

label = tkinter.Label(window, textvariable=data)
label.pack()

window.mainloop()


# mytk06.py
import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()
var = tkinter.StringVar()
label = tkinter.Label(frame, textvariable=var)
label.pack()
entry = tkinter.Entry(frame, textvariable=var)
entry.pack()
window.mainloop()

# mytk07.py
import tkinter

# Контроллер
def click():
    counter.set(counter.get() + 1)

if __name__ == '__main__':
    window = tkinter.Tk()
    # Модель
    counter = tkinter.IntVar()
    counter.set(0)
    # Вид
    frame = tkinter.Frame(window)
    frame.pack()

    button = tkinter.Button(frame, text='Click', command=click) #в окне кликаем, и +1 в итоге
    button.pack()

    label = tkinter.Label(frame, textvariable=counter)
    label.pack()

    window.mainloop()

# mytk08.py
import tkinter

window = tkinter.Tk()

# Модель
counter = tkinter.IntVar()
counter.set(0)

# Контроллеры
def click_up():
    counter.set(counter.get() + 1)
def click_down():
    counter.set(counter.get() - 1)

# Виды
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=click_up)
button.pack()
button = tkinter.Button(frame, text='Down', command=click_down)
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()

window.mainloop()

# mytk09.py
import tkinter

window = tkinter.Tk()
button = tkinter.Button(window, text='Hello',
                        font=('Courier', 14, 'bold italic'))
button.pack()
window.mainloop()

# mytk10.py
import tkinter

window = tkinter.Tk()
button = tkinter.Label(window, text='Hello', bg='green', fg='white')
button.pack()
window.mainloop()

# mytk12.py
import tkinter


def click():
    label.config(text=entry.get())


window = tkinter.Tk()

window.title('Простое окно')

frame = tkinter.Frame(window)
frame.pack()

entry = tkinter.Entry(frame)
entry.pack()

label = tkinter.Label(frame)
label.pack()

button = tkinter.Button(frame, text='Печать!', command=click)
button.pack()

window.mainloop()

import random


def try_div(x, y):
    if y:
        return x / y
    else:
        raise ZeroDivisionError
try:
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    op = input('Введите оператор: ')
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '/':
        try_div(a, b)
    else:
        print('Ошибка')

except ValueError:  # попадаем сюда, если ошибка (если введем букву)
    print("Ошибка преобразования типов")
except ZeroDivisionError:  # попадаем сюда, если ошибка (если введем 0)
    print("Ошибка деления на ноль")


import requests
r = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat')
#print(r.text)
c = r.text.split('\n')
del c[-1]
lst = [float(c[n]) for n in range(len(c))]
from statistics import mean
print('Максимальное значение:', max(lst))
print('Минимальное значение:', min(lst))
print('Среднее значение:', float('{:.3f}'.format(mean(lst))))
print(len(set(lst)))
from matplotlib import pyplot as plt
plt.plot(lst)
plt.show()



import requests
r = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt')
rt = r.text
intab = "QWERTYUIOPASDFGHJKLZXCVBNM"
outtab = "qwertyuiopasdfghjklzxcvbnm"
trantab = str.maketrans(intab, outtab)
rt1 = rt.translate(trantab)
trant = str.maketrans({'.': None, ';': None, ',': None, '-': ' '})
rt2 = rt1.translate(trant)
for word in rt2.split():
    print(word)
with open("moby_clean.txt", "w") as f:
    for word in rt2.split():
        f.writelines(word + "\n")



text = open("moby_clean.txt","r")
d = dict()
for line in text:
    line = line.strip()
    if line in d:
        d[line] += 1
    else:
        d[line] = 1
print(sorted(d.items(), key=lambda x: x[1])[0:5])
print(sorted(d.items(), key=lambda x: x[1])[-5:-1],sorted(d.items(), key=lambda x: x[1])[-1])



q = 0
import requests
r = requests.get('https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt')
rt = r.text
while q != "Да":
    v = input("Задайте вопрос")
    print(random.choice(rt.split("\n")))
    q = input("Вы готовы закончить сеанс?")

import requests
r = requests.get('http://dfedorov.spb.ru/python3/src/romeo.txt')
rt = list(r.text.split())
d = dict()
for words in rt:
    if words in d:
        d[words] += 1
    else:
        d[words] = 1
for key in list(d.keys()):
    print(key, ":", d[key])


import requests
r = requests.get('https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt')
rt = r.text
print(rt)


c = 0; d = 0; e = 0
for i in rt:
    if i == " ":
        c += 1
    if i in ("Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"):
        e += 1
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
rt1 = rt.replace(",", ".")
rt2 = rt1.replace("-", " ")
for i in list(rt2.split()):
    if is_digit(i):
        d += 1
print("Букв в верхнем регистре:",e, ",чисел:", d, ",пробелов:", c)

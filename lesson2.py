s='привет мир'
print(s[0]) #п
print(s[2:5]) #иве
print(s[0]+'d'+s[1:]) #пdривет мир
print(s[1:5:2]) #рв
print(s[::-1]) #рим тевирп
print(s[-1]) #р
s1=s[:]
s1=s
print(id(s1)) #2747460863680
print(id(s))#2747460863680
import copy
s1=copy.copy(s)
print(id(s)) #тот же
print(id(s1))
s="wbefbewufberu urwfuwrb"
print(id(s)) #другой
s1=s[:]
id(s1) #тот же
#import copy
s1=copy.deepcopy(s) #id тот же
s='efwwegreeghrw'
s1=s[3:2]
print(id(s1)) #другой

name="Арина"
name=name[-1]+name[1:-1]+name[0] #name=name[-1]+name[1:len(name)-1]+name[0] (аринА)
print(name)

print(4>1) #True
print(True+True) #2
print(True+False) #1
print(4>1 and 4<5) #True
print(False and True) #False
print(True or False) #True
print(5 and 0) #0
print(5 or 0) #5
print(bool(True)) #True
print(bool("renwjfkjnw")) #True
print(bool(4)) #True
bool(False) #False
bool("") #False
bool(0) #False
bool(None) #False
print(bool(-1)) #True
print(5 and 6) #6, потому что всё правда, но надо что-то вернуть, возвращает последний объект
print(-4 and 0) #0
print(-4 and True) #True
print(-4 and None) #0
print('a' and '') #''
print('' or 'a') #'a'
print('' or False) #False
print('dasa' or False) #dasa

to_be = False
print(to_be or not to_be) #True

x=0
print(-5<x<10) #True
print("a" in "aaaa") #True
print("a" in "rgrfd") #False

s='hello'
if len(s)>2: print(">2") #>2
else: print("<=2")

s='hello'
if len(s)>2: print(">2") #>2
elif len(s)==2: print("==2")
else: print("<2")

#x=float(input())
#if (-2.4<=x<=5.7): print(x**2)
#else: print(4)

#a=input()
#if a==a[::-1]: print('True')
#else: print('False')

x=50
y=25
small=x if x<y else y #тернарный if

#w = int(input("Введите массу тела "))
#r = int(input("Введите рост "))
#ind=w / (r ** 2)
#if ind<=16: print("Выраженный дефицит массы тела")
#elif 16<ind<=18.5: print("Недостаточная масса тела (дефицит)")
#elif 18.5<ind<=24: print("Нормальная масса тела")
#elif 25<=ind<=30: print("Избыточная масса тела (предожирение)")
#elif 30<ind<=35: print("Ожирение I степени")
#elif 35<ind<=40: print("Ожирение II степени")
#elif 40<ind: print("Ожирение III степени")

import math #модуль
#help(math)
print(math.sqrt(4)) #2
math.sin(3)
math.pi #3.14
#print(dir(math))
from math import sqrt
print(sqrt(4)) #2

#from math import factorial as fact #название
#fact(n)/(fact(k)*fact(n-k))

#from math import sin
#x=float(input())
#if 0.2<=x<=0.9: print(sin(x))
#else: print(1)

#import this #философия питона
#pip3 install <имя модуля> для командной строки в пакете
import random
random.random()
random.seed(10)
print(random.random()) #у всех вывелось 0.5714025946899135
print(random.randint(3,6))#случайное от 3 до 6
print(random.choice("gndet")) #случайный символ
print(random.uniform(1,11)) #случайное вещественное


#import random
#x=random.randint(1,4)
#y=int(input('Введите число от 1 до 4'))
#if x==y: print('Победа')
#elif x>y: print('Число меньше')
#else: ('Число больше')



#import random
#h="орел"
#t="решка"
#c=[h,t]
#x=random.sample(c,1)
#y=input('Орел или решка?')
#if x==y: print(f'You win, было загадано {x}')
#else: print(f'Bad luck, было загадано {x}')


print('hello'.upper().lower()) #hello
print('hello hello'.title()) #Hello Hello
print('hello'.find('l')) #2, на второй позиции
print('hello'.find('d')) #-1, не находится
print('hello'.find('e',1,3)) #1, находится
print('hello'.count('e')) #1
print('hello'.replace('h','o')) #oello
print('a'.isalpha()) #True
print('ab'.isalpha()) #True
print('ab3'.isalpha()) #False
s="     \n MMMM \n    "
print(s)
print(s.strip())

s='<[у озера ]>'
print(s.strip('<>][')) #у озера
print('hello {0} {1}'.format(3,3)) #hello 3 3
a=3
b=3
print(f'hello {a} {b}') #hello 3 3
s='2019.py'
print(s.endswith('.py')) #True
#import  os


s = "У лукоморья 123 дуб зеленый 456"
print(s.find('я'))
print(s.count('у'))
if not s.isalpha():
    print(s.title())
print(len(s))
if len(s)>4:
    print(s.upper().lower())
print(s.replace(s[0],'О'))
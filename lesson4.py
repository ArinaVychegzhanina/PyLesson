lst = [3, 4, 3, 2, '4', 4.3]
for item in lst:
    print(item, end=' ') #выводим на экран каждый из item в строку через пробел
s="hello"
for item in s:
    print(item, end=' ') #h e l l o
#summa = 0
#for item in lst:
 #   if isinstance(item, str): #проверяет, одинаковый ли тип
  #      summa += item
   #     print(summa)
total = 0
for i in range(1, 101):
    total += i
print(total)

for i in range(1, 250, 3):
   if i % 2 == 0: #четные числа с шагом 3
       print(i, end = ', ')

sum = 0
for i in range(10, 150, 5):
   if i % 2 == 0:
       sum += i
print(sum)

total = 0
for i in range(5):
   x = int(input('Введите любое число: '))
   if input('Включить это число в суммирование?: ').title() == 'Да':
       total += x
print(x)

num = input('Введите Ваш номер телефона через дефис: ')
print(num.replace('-','').replace(' ','')) #выводит номер телефона без дефисов и пробелов


list_ = {1, 3, 5, 7, 8 ,90}
x = int(input('Введите число: '))
min = max(list_) #for i in range(len(lst)):
for i in list_:
   if abs(i - x) < min:
       min = abs(i - x)
       otvet_ = i
print(otvet_)

countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
for i in range(len(countries_temperature)):
       print(countries_temperature[i][0], str(sum(countries_temperature[i][1])/len(countries_temperature[i][1])))
#Thailand  -  23.9 С
#Germany  -  13.8 С
#Russia  -  3.7 С
#Poland  -  12.0 С

lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 14, 46, 273, 22, 99, 15, 1000]
s=0
for i in lst:
    if ((i>10 and i<100) or (i>200 and i<500)):
        s += i;
print (s)


def function(x): # функция
    return x + 1

print(function(3)) #x=3, результат 4

def function(x): # функция
    if isinstance(x, list):
        return len(x)
    return None
print(function("hello")) #None
print(function([4,3,4])) #3

def function(x, z): # функция от 2х аргументов
    return x + z

print(function(1, 3)) #x=1, z=3, результат 4

s = 6
print(s)
def function(x, z):
    global s
    s = 5
    return x + z +s
print(function(1, 3)) #s = 5, результат 9


def summ(x, z): #чистые функции
    return x + z
print(summ(1, summ(3, 3)))

def summ(x=0, z=0):
    """
    Result #описание функции, отображается если вызвать help
    int x
    int y
    """
    return x + z
print(summ(1, summ(4,3)))

def summa(x: int,y: int) -> int: #аргументы  результат типа данных int
    return x+y
print(summa('3','10'))
print(summa(3,'10'))
print(summa(3,10))
print(summa(3.1,10))

def ZP(hours: float, pay_rate: float) -> float: #расчет зп, pay = hours * pay_rate
   return hours * pay_rate


def is_palindrome(word: str)->bool: #проверка слова на полиндром
   if word == word[::-1]:
       return True
   else:
       return False

def my_abs (x): #модуль, абсолютное значение
   if str(x)[0] == '-':
       return str(x)[1::]
   else:
       return x
print(my_abs(-5676.9))

def str_lower(str_: str)->list: #получает строку и выводит в виде списка (split) в нижнем регистре (lower)
   return str_.lower().split()

def common(lst1: list, lst2: list) -> list: #список общих элементов из двух списков
   lst3 = []
   for i in lst1:
       for j in lst2:
           if i == j:
               lst3.append(i) #добавляет в конец списка
   return lst3

def common(v: list, u: list) -> list:
    return list(set(v) & set(u)) #тоже самое

def countElemKR(stroke: str):
   countUpper = 0
   countLower = 0
   for symbol in stroke:
       if symbol.islower(): # islower проверяет нижний ли регистр
           countLower += 1
       else:
           countUpper +=1
   return countLower, countUpper

def sort_words(words: str) -> str:
    return '-'.join(sorted(words.split('-')))

#Каким образом можно упорядочить строки по количеству символов?
#>>> x = ["The", "Python", "1"]
#>>> x.sort(key=len)
#>>> x
#['1', 'The', 'Python']

def f(x): #отсортировать по второму символу списки
    return x[1]
x.sort(key=f)




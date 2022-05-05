print(range(10))
print(list(range(3, 10, 2))) #создаем список от 3 до 10 с шагом 2
lst = []
for item in range(10):
    lst.append(item)
print(lst) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([item for item in range(10)])# вместо append, добавляем item, тот же рузультат, создать список

lst = []
for item in range(10):
    if item % 2 == 1:
        lst.append(item)
print(lst) #список нечетных: [1, 3, 5, 7, 9]
print([item for item in range(10) if item % 2 == 1]) #то же самое

lst = []
for item in range(10):
    if item % 2 == 1:
        lst.append(item ** 2)
print(lst) #список нечетных в квадрате: [1, 9, 25, 49, 81]
print([item ** 2 for item in range(10) if item % 2 == 1]) #то же самое

print([item + 4 for item in [1, 3, 4]]) #новый список, где эл. увеличены на 4: [5, 7, 8]

print(map(len, [1, 2, 3])) #<map object at 0x00000254AFCB6B50> странные объекты типа мап, итератор, генератор можно задать в список
import math
print(list(map(math.sqrt, [1, 3, 4]))) # [1.0, 1.7320508075688772, 2.0] список

def f(x):
    return x + 4
import math
print(list(map(f, [1, 3, 4]))) #[5, 7, 8]

print(list(map(lambda x: x + 4, [1, 3, 4]))) #[5, 7, 8] лямбда функция, то же самое

print([x.lower() for x in ['I', 'AM', 'GROOT']]) #['i', 'am', 'groot']

from random import randint
A = [randint(1, 9) for _ in range(5)] #слуйчайный список длины 5 от 1 до 9, напр.: [1, 4, 7, 1, 2]
print(A)

lst = [4,'5','6',8]
print("".join([str(item) for item in lst])) #объединяет список в 4568, делая все элементы типа string
print("".join(list(map(str, lst)))) #то же самое

import math
print(list(map(math.sqrt, [2, 4, 9, 16, 25]))) #корни списка
print([math.sqrt(num) for num in [2, 4, 9, 16, 25]])#то же

import random
lst = [random.randint(-100, 100) for _ in range(100)]
lst.sort()
print((lst[49] + lst[50]) / 2) #медиана списка
import statistics
print(statistics.median([randint(-100, 100) for _ in range(100)])) #то же самое

lst = [random.randint(100, 200) for _ in range(1000)]
print(sum(1 if 170 < i < 195 else 0 for i in lst)) #количество чисел от 170 до 195
print(sum(i if 170 < i < 195 else 0 for i in lst)) #сумма таких чисел
print([1 for item in lst if 170  < item < 195].count(1)) #количество чисел от 170 до 195

lst = ['aba', 12321, 'aaccdccaa']
print(all(map(lambda x: x == x[::-1], list(map(str, lst))))) #True, проверяет все ли элементы палиндромы


text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
import re
print(re.sub(r'\b\w{1,3}\b', '', text))








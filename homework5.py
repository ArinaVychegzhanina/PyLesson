#Задание 1
def my_log(lst: list):
    import math
    return list([math.log(i) if i > 0 else "None" for i in lst])

print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))

#Задание 2
import random
arr = [random.randint(0, 100) for _ in range(10)]
a = min(arr); b = max(arr)
c = arr.index(a); d = arr.index(b)
print(arr)
print('Минимальный элемент:', a, ', максимальный:', b)
import statistics
if c == d + 1 or d == c + 1:
    print(arr)
elif c < d:
    c += 1
    print('Среднее значение:', statistics.mean(arr[c:d]))
else:
    d += 1
    s = statistics.median(arr[d:c])
    i = d
    while i < c:
        arr[i] = s
        i += 1
    print(arr)

#Задание 3
import statistics
ls = [1, 5, 6.3, 6, None, 2.0, -4, None]
for i in range(len(ls)):
    if ls[i] == None:
        ls[i] = 0
c = statistics.mean(ls)
for i in range(len(ls)):
    if ls[i] == 0:
        ls[i] = c
print(ls)

#Задание 4, способ 1
text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
l = [line for line in text.split() if len(line) > 3]
w = text.split('\n')
ls = []
for i in w:
    ls1 = []
    for j in i.split(' '):
        if j in l:
            ls1.append(j)
    ls.append(ls1)
print(ls)

#способ 2
w = text.split('\n')
ls = []
for i in w:
    ls2 = []
    [ls2.append(j) for j in i.split() if len(j) > 3]
    ls.append(ls2)
print(ls)



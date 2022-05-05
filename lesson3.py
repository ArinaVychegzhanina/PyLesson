a = [1, 3, 3, 4]
a = ['3', 3, 4.3, [3, 2, 2]]
print(a[0]) #'3'
print(a[-1]) #[3, 2, 2]
print(a[-1][2]) #2
print(len(a)) #4
print('d' in 'webcfhwd') #True
print(2 in [2, 4, 2, 3]) #True
x = y = [1, 2]
print(x) #[1, 2]
print(y) #[1, 2]
print(id(x) == id(y)) #True
print(x is y) #True

x = [1, 2]
y = [1, 2]
print(id(x) == id(y)) #False
print(x is y) #False

colors = ['red', 'orange', 'green']
colors.extend(['black', 'blue']) #добавляет
print(colors)
colors.append('purpure') #добавляет в конец
print(colors)
colors.insert(2, 'yellow')
print(colors) #['red', 'orange', 'yellow', 'green', 'black', 'blue', 'purple']
colors.remove('black') # Перед использованием remove проверять наличие элемента в списке
print(colors) #['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(colors.count('red')) #1
print(colors.index('green')) #3
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(colors.pop()) #'purple' удалаяет
print(colors) #['red', 'orange', 'yellow', 'green', 'blue']
colors.reverse()
print(colors) #['blue', 'green', 'yellow', 'orange', 'red']
colors.sort()
print(colors) #['blue', 'green', 'orange', 'red', 'yellow']
colors.clear()
print(colors) #[]

#итераторы
xs = [1, 2, 3]
xs.reverse()
print(xs) #[3, 2, 1]
reversed(xs)
list(reversed(xs)) #[1, 2, 3]
iter_xs = reversed(xs)
next(iter_xs) #1
next(iter_xs) #2
next(iter_xs) #3

s='hello'
list(s)
lst = list(s)
lst[1]="E"
print(lst) #['h', 'E', 'l', 'l', 'o']

b='Hello'
print('_____'.join(b)) #H_____e_____l_____l_____o

L = [3, 6, 7, 4, -5, 4, 3, -1]
s = sum(L)
if s > 2:
   print(len(L))
r = max(L) - min(L)
print(r)
if r > 10:
   print(sorted(L, reverse=True)) #[7, 6, 4, 4, 3, 3, -1, -5], отсортированный по убыванию
else:
   print('Разность меньше 10')

favorites = [3, 7, 11, 23, 18, 48, 81]
x = int(input('Введите целое число: '))
if x in favorites:
   print('Мое любимое число!')
else:
   print('Эх, ну почему?')

line = ["Автово", "Кировский завод", "Нарвская", "Балтийская",  "Технологический институт 1", "Пушкинская", "Владимирская", "Площадь Восстания"]
s = input("Текущая станция: ")
ind = line.index(s)
print(f"Следующая станция {line[ind+1]}")

num = input('Введите Ваш номер телефона через дефис: ')
print(num.replace('-','').replace(' ',''))
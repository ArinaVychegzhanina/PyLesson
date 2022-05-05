print(type(())) #<class 'tuple'>
print((3)) #3
print(type((3))) #<class 'int'>
print((3,)) #(3,)
print(3,) #3
print(3,4,3) #3 4 3
(x,y)=(1,3)
print(x) #1
print(y) #3
animals = ['cat','dog','bird']
for index, value in enumerate(animals):
    print(index,value)
    #0 cat, 1 dog, 2 bird

import statistics

student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

print(f"Студент: { {student[0].split()[1]}, {student[0].split()[0]} }")

print(f"Возраст: в 2021 {2021 - student[1]}")

print(f"Оценки: {tuple(student[2])}")

a = round(statistics.mean(student[2]), 1)
print(f"Cредний балл {a}")

if a >= 8 and student[-1]:
   print(True)
else:
   print(False)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp.get('four', 'нет перевода'))
print(eng2sp.setdefault('four', 'нет перевода'))
print(eng2sp) #{'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'нет перевода'}


user = {'Камин комплект Старый Замок':
{'count': 1, 'price': 28490},
'Полусапоги Betsy':{'count': 2, 'price': 2399},
'Семь навыков высокоэффективных людей':{'count': 1, 'price': 437}}

total=0
for item in user:
    print(item) #вывод перечня ключей
    print(item, user[item]) #ключи и значения ключей
    print(item, user[item]['count'])  # ключи и значения ключей и колтичество
    print(item, user[item]['count']*user[item]['price'])
    total += user[item]['count']*user[item]['price']
print(total)
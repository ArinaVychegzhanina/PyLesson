#Задание 1
import random
s1 = random.randint(1, 10)
s2 = int(input('Введите целое число: '))
while s1 != s2:
    if s1 > s2:
      print('Ваше число меньше загаданного')
      s2 = int(input('Введите целое число: '))
    elif s1 < s2:
      print('Ваше число больше загаданного')
      s2 = int(input('Введите целое число: '))
if s1 == s2:
    print('Вы угадали!')

#Задание 2
def password():
    pas = []
    for i in range(random.randint(7, 10)):
        j = random.randint(33, 126)
        c = chr(j)
        pas.append(c)
    return pas

#Задание 3
def reliable(pw):
    a = 0; b = 0; d = 0
    for i in range(len(pw)):
        if pw[i].isalpha():
            if pw[i].islower():
                a += 1
            elif pw[i].isupper():
                b += 1
        elif pw[i].isdigit():
            d += 1
    if (len(pw) >= 8) and (a >= 1) and (b >= 1) and (d >= 1):
        return True
    else:
        return False
if reliable(input('Введите пароль')) == True:
    print('Это надежный пароль')
else:
    print('Это ненадежный пароль')

#Задание 4
m = 1
while reliable(password()) != True:
    m += 1
print('Надежный пароль', "".join(password()), 'удалось вывести с попытки', m)
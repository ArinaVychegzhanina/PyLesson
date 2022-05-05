def catch_all(*args, **kwargs):
    print("args =", args)
    print("kwargs = ", kwargs)
catch_all(3,4,3,2,a=2,b=5, c=5,f=5,d=5) #args = (3, 4, 3, 2); kwargs =  {'a': 2, 'b': 5, 'c': 5, 'f': 5, 'd': 5}
try:
    number = int(input())
    print(5/number)
except: #попадаем сюда, если ошибка (если введем 0 или букву)
    print("Error")


try:
    number = int(input())
    print(5/number)
except ValueError: #попадаем сюда, если ошибка (если введем букву)
    print("Error number")
except ZeroDivisionError:  #попадаем сюда, если ошибка (если введем 0)
    print("Error zero")
print('hi')


def mean(num_list):
    if len(num_list)==0:
        raise Exception("dfbfs. "
                        "ffgsfgvf")
    else:
        return sum(num_list)/len(num_list)

print(mean([1,2,5]))

#if len(lst) != 0:
#    mean(lst)

try:
    print(mean([]))
except Exception as err:
    print(err)


#def kelvin_to_fahrenheit(temperature):
 #  assert temperature >= 0, "Colder than absolute zero!"
  # return round(((temperature - 273) * 1.8) + 32, 2)

#print(kelvin_to_fahrenheit(273))
#print(kelvin_to_fahrenheit(505.78))
#print(kelvin_to_fahrenheit(-5))



#def my_abs(value):
#    return 0 #pass

#assert my_abs(0) == 0, 'not null' #тестирование
#assert my_abs(1) == 1, 'not 1'
#assert my_abs(-1) == 1, 'not 1'


def my_abs(value):
    if value < 0:
        return -value
    return value

assert my_abs(0) == 0, 'not null'
assert my_abs(1) == 1, 'not 1'
assert my_abs(-1) == 1, 'not 1'

def get_int(msg):
    while True: #пока не введут строку из цифр
        try:
            x = int(input(msg))
            return x
        except ValueError:
            print("Error converting to a number")

get_int("Введите число")

#file=open("text.txt","r", encoding='cp1251') #если в нашей директории, иначе другой путь; file=open("text.txt") - r по умолчанию;
# encoding - кодировка utf8(по умолчанию) или cp1251
#print(file.read())
#file.close()

#менеджер контекста #(*mode="r"*)
with open("test", mode="r", encoding='utf8') as file:
    s=file.readlines()
    print(s)
######
print(len(s))
#print(s.split("\n"))
print(map(str.strip,s)) #5
lst=list(map(str.strip,s))
print(list(map(len,lst))) #список, который содержит длины всех элементов [1, 1, 7, 4, 5]
print(max(list(map(len,lst)))) #максимальная длина строчки 7


lst=[]
with open("test", mode="r", encoding='utf8') as file:
    for line in file:
        print(line,end="") #бежим по строкам
        print(len(line.strip())) #длины строк
        if len(line.strip())>10:
            lst.append(line.strip())
print(lst)

with open("test", mode="w", encoding='utf8') as file:
    print(file.write("Нello!Нello!Нello!")) #18

    import matplotlib.python as plt
    %matplotlib inline
    #создать списки для координат x и y каждой точки данных
    x_coords=[0,2,3,4,6]
    y=coords=[0,3,1,5,1]
    #Построить линейный график
    plt.plot(x_coords,y_coords)
    #Показать грфаик
    plt.show()

print(5**56+4**44)
status=1
print(status)
dif=20
double=2*dif
print(double)
status_result=1
F=10000
n=10
r=4.25
P=F/((1+r/100)**n)
print(P)
print(abs(-6.12))
print(pow(3,2))
help(pow)
# pow(3,4,5) == 3**4%5 == pow(base=3, exp=4, mod=5)
None #пустота
print(round(3.49999999)) #3, округление
print(round(4.124134,2)) #4.12
print(int(4.7)) #4, отбрасывание вещественной части
print(float(4)) #4.0
print(round(pow(3,2)*3)+pow(3,5)) #270
print(type(4)) #<class 'int'>
print(type(round)) #<class 'builtin_function_or_method'>
round=5
print(type(round)) #<class 'int'>
del round
print(type(round)) #<class 'builtin_function_or_method'>
print("hello")
print('hi'+'hello') #hihello
print('hi'*3) #hihihi
#print("hi"+5+"hey") ошибка
print("hi"+str(5)+"hey") #hi5hey
print("hel'lo") #hel'lo
print("hel\"lo") #hel"lo
print("asdafaed\f \t     \n    \nfed")
print("1",3,"ewwr",4.3) #1 3 ewwr 4.3

a = 'Petr'
b = 'Alex'
c = 'Max'
print(a, b, c, sep= ';') #Petr;Alex;Max
print("C:\hello\note")
print("C:\hello\\note")
print(r"C:\hello\note\too") #print(r"C:\hello\note\too") #
#name=input("Введите имя: ") #тип строка
#print(name)

#age=int(input("Введите возраст: ") )
#print("В следующем году тебе будет ", age+1)

print(f"Ваш возраст в следующем году {int(input())+1}")

m = int(input("Введите массу тела "))
h = int(input("Введите рост "))
print(f"Индекс массы тела - {m / (h ** 2)}")








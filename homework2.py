rain = input("Is it raining? ").lower()
print(rain)
if rain == "yes":
    wind = input("Is it windy? ").lower()
    if wind == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")

name = input("Enter your name in lowercase ").title()
lastname = input("Enter your last name in lowercase ").title()
print(name, "", lastname)

poem = input("Enter the first line of a poem ")
print(len(poem))
a, b = int(input(f"Enter the start and end position before {len(poem)} ")), int(input())
print(poem[a:b])

name = input("Enter your name ")
if len(name) < 5:
    lastname = input("Enter your last name ")
    print((name.title() + lastname))
else:
    print(name.lower())

from math import sqrt
number = int(input("Enter an integer greater than 500 "))
print("{0:.2f}".format(sqrt(number)))

import math
figure = input("Введите тип фигуры: ").lower()
if figure == "круг":
    r = int(input("Введите радиус круга: "))
    print("Площадь круга равна", "{0:.2f}".format(math.pi*r*r))
if figure == "треугольник":
    a, b, c = int(input("Введите стороны треуголька: ")), int(input()), int(input())
    print("Площадь треугольника равна", math.sqrt(((a+b+c)/2)*((-a+b+c)/2)*((a-b+c)/2)*((a+b-c)/2)))
if figure == "прямоугольник":
    ab, cd = int(input("Введите стороны прямоугольника: ")), int(input())
    print("Площадь прямоугольника равна", ab*cd)
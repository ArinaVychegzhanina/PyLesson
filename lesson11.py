a = input().split()
s1 = []
print(a)

def calc(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a // b
    else:
        return "Error"

for i in range(len(a)):
    if a[i].isdecimal():
        s1.append(int(a[i]))
    elif len(s1) >= 2:
        m = s1.pop()
        n = s1.pop()
        if (m == 0) & (a[i] == "/"):
            print('Error')
            exit()
        s2 = calc(a[i], n, m)
        s1.append(s2)
    else:
        print('Error')
        exit()
    print(s1)
print(s1[0])


s2 = list(input())
s = []
s1 = []
m = 0; n = 0; a = 0; b = 0; c = 0; d = 0
print(s2, s2[-1])
for i in range(len(s2)):
    if s2[i] == '(':
        m += 1
    if (s2[i] == ')')&(m>n):
        n += 1
    if s2[i] == '{':
        a += 1
    if (s2[i] == '}')&(a>b):
        b += 1
    if s2[i] == '[':
        c += 1
    if (s2[i] == ']') & (c > d):
        d += 1
if (m == n) & (a == b)& (c == d):
    print('скобки расставлены правильно')
else:
    print('скобки расставлены неправильно')

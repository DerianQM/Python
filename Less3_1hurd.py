# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
import math

str1 = input("Введите выражение , которое я буду резать, вида a +- b, где a и б простые дроби вида a/b ")
N = 0
M = 0
D1 = [0]
D2 = [0]
cort = str1.split(' ')
for f in cort:
    if (f =='-') or (f=='+'):
        part = cort.index(f)
        znk = f


for i in range(part): # нарезка просится в цикл , но сам принцип разный и создавать кортеж из возврата 2х значений и потом еще с ним возиться нет времени
    try:
        N=int(cort[i])

    except:
        D1 = cort[i].split('/')


cort_part=cort[part+1:]
for f in cort_part:
    try:
        M=int(f)

    except:
        D2 = f.split('/')


if D1[0]==0 and D2[0]==0:
    if znk =='-':
        res = N - M
    else:
        res = N + M
    print(f"Результат {res}")
elif D1[0]!=0 and D2[0]!=0:
    if N < 0:
        p1 = (abs(N)+ int(D1[0])/int(D1[1]))*-1
    else:
        p1 = N + int(D1[0]) / int(D1[1])
    if M < 0:
        p2 = (abs(M) + int(D2[0]) / int(D2[1]))*-1
    else:
        p2 = M + int(D2[0]) / int(D2[1])

    if znk =='-':
        res = p1 - p2
    else:
        res = p1 + p2
    massotv = math.modf(res)

    if int(massotv[1]) == 0:
        print(f"  { round((massotv[0]) * int(D1[1])*int(D2[1]))} / {int(D1[1])*int(D2[1])} ")
    elif int(massotv[1]) > 0:
        print(f" {int(massotv[1])} { round((massotv[0]) * int(D1[1])*int(D2[1]))} / {int(D1[1])*int(D2[1])} ")
    else:
        print(f" {int(massotv[1])} { round(abs(massotv[0]) * int(D1[1])*int(D2[1]))} / {int(D1[1])*int(D2[1])} ")

elif D1[0]!=0 and D2[0]==0:

    if N < 0:
        p1 = (abs(N) + int(D1[0]) / int(D1[1]))*-1
    elif N > 0:
        p1 = N + int(D1[0]) / int(D1[1])
        print("P1 = ",p1)
    if znk =='-':
        res = p1 - M
        
    else:
        res = p1 + M
    massotv = math.modf(res)

    if int(massotv[1]) == 0:
        print(f"  { round((massotv[0]) * int(D1[1]))} / {int(D1[1])} ")
    elif int(massotv[1]) > 0:
        print(f" {int(massotv[1])} { round((massotv[0]) * int(D1[1]))} / {int(D1[1])} ")
    else:
        print(f" {int(massotv[1])} { round(abs(massotv[0]) * int(D1[1]))} / {int(D1[1])} ")
elif D1[0]==0 and D2[0]!=0:
    print(D2)
    if M < 0:
        p1 = (abs(M) + int(D2[0]) / int(D2[1]))*-1
    else:
        p1 = M + int(D2[0]) / int(D2[1])
    if znk =='-':
        res = N - p1
    else:
        res = N + p1
    massotv = math.modf(res)

    if int(massotv[1]) == 0:
        print(f"  { round((massotv[0]) * int(D2[1]))} / {int(D2[1])} ")
    elif int(massotv[1]) > 0:
        print(f" {int(massotv[1])} { round((massotv[0]) * int(D2[1]))} / {int(D2[1])} ")
    else:
        print(f" {int(massotv[1])} { round(abs(massotv[0]) * int(D2[1]))} / {int(D2[1])} ")




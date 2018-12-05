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
'''def find_space(temp_str):
    k = temp_str.find(' ')
    k1 = temp_str.rfind(' ')  # предположим, что пользователь вводит по шаблону, разделяя  + и - пробелами иначе это будет не работать
    d2 = temp_str[:k]
    znk = temp_str[k + 1:k1]
    d3 = temp_str[k1 + 1:]
    return (d2,znk,d3)

def delresult(znk,N,M,D1,D2):
    if znk == '-':
        if D1[0] =='0':




        arg1 = int(d1) * int(d4) - int(A[0]) * int(A[2])
    else:
        arg1 = int(d1) * int(d4) + int(A[0]) * int(A[2])
    arg2 = int(A[0]) * int(d4)
    print(f" {arg1 // arg2}  {round(arg1 % arg2)}/{arg2} ")
'''
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
        p1 = (N + int(D1[0])) / int(D1[1])
    if M < 0:
        p2 = (abs(M) + int(D2[0]) / int(D2[1]))*-1
    else:
        p2 = (M + int(D2[0])) / int(D2[1])

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
    else:
        p1 = (N + int(D1[0])) / int(D1[1])
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
        p1 = (M + int(D2[0])) / int(D2[1])
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

  #  print(f" {int(res)} {abs()*int(D1[1])))} / {D1[1]} ")
#print(f" {massotv[1]} { round(abs(massotv[0]) * int(D1[1]))} / {D1[1]} ")
#for part in range(len(cort)):
#    try:
#        M=int(cort[i])
#        print(N)
#    except:
#        D2 = cort[i].split('/')
#        print(D1)

'''a = str.find('/')
b = str.rfind('/')

part1 = str[:a]
c = part1.find('')
d = part1.rfind('')
if c ==-1:
    d1=str[:a]
elif c == d:
    d1 = str[c+1:a]
    N = part1[:c]


d1= str[:a]

if a == b:  # может выглядит и не очень, но еще более оптимизировать нет времени
    d4 = 1
    temp_str = str[a+1:]
    A = find_space(temp_str)
    delresult(A, d1, d4)
else:
    d4 = str[b + 1:]
    temp_str = str[a + 1:b]
    A = find_space(temp_str)
    delresult(A, d1, d4)



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
'''
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
import math
import turtle


def paint(mass): # мы это проходили в предподготовке, никакого жульничества, зато интересно
    turtle.penup()
    turtle.goto(float(mass[0][0]), float(mass[0][1]))
    turtle.pendown()
    turtle.fillcolor("Gray")
    turtle.begin_fill()
    turtle.goto(float(mass[1][0]), float(mass[1][1]))
    turtle.goto(float(mass[2][0]), float(mass[2][1]))
    turtle.goto(float(mass[3][0]), float(mass[3][1]))
    turtle.goto(float(mass[0][0]), float(mass[0][1]))
    turtle.end_fill()
    turtle.hideturtle()
    turtle.mainloop()

def fibonacci(n, m):
    sp1 = [1, 1]
    for i in range(m):
        sp1.append(sp1[i] + sp1[i + 1])
    return sp1[n:m]


def sort_to_max(org_list):
    n = 1
    while n < len(org_list):
        for i in range(len(org_list) - n):
            if org_list[i] > org_list[i + 1]:
                org_list[i], org_list[i + 1] = org_list[i + 1], org_list[i]
        n += 1
    return (org_list)


def filt(func, itt):
    mass = list()
    for i in itt:
        if func(i):  # если результат выполнения функции True делаем добавление элемента в массив
            mass.append(i)
    return mass


def createPoint():  # функция для создания списка координат, который введет пользователь
    listNew = []
    for f in range(8):
        print("Введите ", f + 1, "ю координату ")
        s = input()
        listNew.append(s)
    pointmass=prnt(listNew)
    return (pointmass)


def prnt(list):  # Вывод для понятливости того, что ты ввел и преобразование в массив из списков
    k = 0
    pointmass=[]
    for f in range(4):
        print(f"точка {spk[f]}  [{list[k]}].[{list[k + 1]}]")
        pointmass.append([list[k],list[k + 1]])
        k += 2
    return pointmass

def pointcheck (x1, y1, x2, y2):
    if float(x1) - float(x2) == 0:
        leng = float(inf)
    else:
        leng = (float(y1) - float(y2)) / (float(x1) - float(x2))
    return leng

n = int(input("Введите с какого элемента вывести ряд Фибоначчи n =")) - 1
m = int(input("Введите по какой элемента вывести ряд Фибоначчи m ="))

print(f"Ряд Фибонначи с {n + 1} элемента по {m} элемент равен {fibonacci(n, m)}")
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


sp = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print("Отсортированный список", sort_to_max(sp))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

sp1 = filt(lambda x: x % 2 == 1, sp)  # лямбда тоже функция, поэтому норм
print("Фильтрованный список",sp1)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print("Математика не нужна говорили на вводных курсах, это поэтому большинство заданий с ней связано")
spk = ['A', 'B', 'C', 'D']
mass = createPoint()

ab = pointcheck(mass[0][0], mass[0][1], mass[1][0], mass[1][1])
ac = pointcheck(mass[0][0], mass[0][1], mass[2][0], mass[2][1])
ad = pointcheck(mass[0][0], mass[0][1], mass[3][0], mass[3][1])
bc = pointcheck(mass[1][0], mass[1][1], mass[2][0], mass[2][1])
bd = pointcheck(mass[1][0], mass[1][1], mass[3][0], mass[3][1])
cd = pointcheck(mass[2][0], mass[2][1], mass[3][0], mass[3][1])



if (ab == cd) or (ac == bd) or (ad == bc):
    print("Отлично -не забудь посмотреть открывшееся окно - там нарисовано")
else:
    print("НЕТ! --не забудь посмотреть открывшееся окно - там нарисовано")
# не всегда будет именно прямоугольник, там смотря с какой стороны считать , но принцип будет понятен
paint(mass)
# смотря в каком порядке вести линии и задавать точки тут нужен перебор всех сторон
# так лучше из всего, что я просмотрел по вычислению по 4м точкам. больше проблем доставил именно способ вычисления, чем написание самой программы,давайте засунем бооооольше матиматики, почему нет 

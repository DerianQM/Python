
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
import math

def fibonacci(n, m):
    sp1 =[1,1]
    for i in range(m):
        sp1.append(sp1[i]+sp1[i+1])
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
       if func(i): #если результат выполнения функции True делаем добавление элемента в массив
            mass.append(i)
    return mass

def createPoint():  # функция для создания списка координат, который введет пользователь
        listNew = []
        for f in range(8):
            print("Введите ", f+1, "ю координату ")
            s = input()
            listNew.append(s)
        prnt(listNew)
        return (listNew)

def prnt(list): # Вывод для понятливости того, что ты ввел
    k = 0
    for f in range(4):
        print(f"точка {spk[f]}  [{list[k]}].[{list[k+1]}]")
        k+=2


n = int(input("Введите с какого элемента вывести ряд Фибоначчи n ="))-1
m = int(input("Введите по какой элемента вывести ряд Фибоначчи m ="))

print(f"Ряд Фибонначи с {n+1} элемента по {m} элемент равен {fibonacci(n,m)}")
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()




sp = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print("Отсортированный список",sort_to_max(sp))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

sp1 = filt(lambda x: x%2 == 1, sp) # лямбда тоже функция, поэтому норм
print(sp1)



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print("Математика не нужна говорили на вводных курсах, это поэтому большинство заданий с ней связано")
spk = ['A','B','C','D']
mass= createPoint()

AB= abs((float(mass[3])-float(mass[1]))**2+(float(mass[2])-float(mass[0]))**2)
print(AB)
CD= abs((float(mass[7])-float(mass[5]))**2+(float(mass[6])-float(mass[4]))**2)
print(CD)
AC= abs((float(mass[5])-float(mass[1]))**2+(float(mass[4])-float(mass[0]))**2)
print(AC)
BD= abs((float(mass[7])-float(mass[3]))**2+(float(mass[6])-float(mass[2]))**2)
print(BD)
if (AB==CD)and(AC==BD):
    print("Чудесно")
else:
    print("НЕТ!")

# решение пробное, еще поработаю над ним
__author__ = 'Гущин Дмитрий Валерьевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

import random
import math

print("Задание 1 normal\n")
a = str(random.randrange(0,1000000))
check = 0
for f in a:
    if check <= int(f):
        check = int(f)

print("Число было - ",a,"\n максимальная цифра в числе -", check)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("Задание 2 normal\n")

one = int(input("Введите перое числовое значение -\n"))
two = int(input("Введите второе числовое значение -\n"))

mass = [one,two] # заношу в список

mass.reverse() # меняю местами элементы списка, если список был бы больше, пришлось бы указывать конкретные элементы

print("Первое значение -", mass[0], "Второе значение", mass[1])

print("Задание 2 normal - с переменными")

two = one + two
one = two - one
two = two - one


print("Первое значение -", one, "Второе значение",two)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("Задание 3 normal - квадратные корни уравнения ax² + bx + c = 0.")

a = int(input("Введите коэффициент a -\n"))
b = int(input("Введите коэффициент b -\n"))
c = int(input("Введите коэффициент c -\n"))

discr = b**2 - 4*a*c

if discr < 0:
    print("Дискриминант =", discr, " < 0, корней нет")
elif discr == 0:
    x1 = (-b + math.sqrt(discr))/2*a
    print("Дискриминант =", discr, ", единственный корень - ",x1)
else:
    x1 = (-b + math.sqrt(discr)) / 2 * a
    x2 = (-b - math.sqrt(discr)) / 2 * a
    print("Дискриминант =", discr, " > 0, корень 1 = ", round(x1, 3), "корень 2 =", round(x2,3))
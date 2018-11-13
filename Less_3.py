# coding : utf-8
import os
import psutil
import sys

# Комментарии

print("Урок №2")
print("Привет, программист")
name = input("Введите ваше имя: ")
print(name, ", Добро пожаловать в мир Python!")
answer = input("Давайте поработаем? (y/n)")

if answer == 'y':
	variant = input("Это хорошо. Выбери из списка действие и введите его номер:\n 1 Действие \n 2 Информация о системе \n 3 Действие \n")
	if variant == '1':
		print ("Прекрасно")
	elif variant == '2':
		print (" Имя текущей директории ", os.getcwd()) 
		print("\n Платформа (ОС) ", sys.platform )
		print("\n Кодировка файловой системы ", sys.getfilesystemencoding()),
		print("\n имя пользователя ", psutil.users())
		print("\n Количество CPU ", psutil.cpu_count())
	elif variant == '3':
		print ("превосходно")
	else:
		print ("Нет номера такой функции") 

elif answer == 'n':
	print("Goodbay!")
else:
	print("Неизвестный параметр")
input()
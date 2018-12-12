# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")



def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f'директория {dir_name} создана')
    except FileExistsError:
        print(f'директория {dir_name} уже существует')


def ping():
    print("pong")


def copyFile():
    if not dir_name:
        print("Необходимо указать имя копируемого файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        shutil.copyfile(dir_path, f"{dir_path}.copy")
        print(f"Файл {dir_path} успешно скопирован")
    except FileNotFoundError:
        print(f'Файл {dir_path} не найден')


def delFile():
    if not dir_name:
        print("Необходимо указать имя удаляемого файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isfile(dir_path):    
        try:
            os.remove(dir_path)
            print(f"Файл {dir_path} успешно удален")
        except FileNotFoundError:
            print(f'Файл {dir_path} не найден')
    else:
        print("Это директория")

def changeDir():
    try:
        os.chdir(os.path.join(os.getcwd(), dir_name))
        print(f"Рабочая директория успешно изменена на {dir_name}")
    except OSError:
        print(f" Директория {dir_name} не найдена! ")
    print(os.getcwd())


def fullDir():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copyFile,
    "rm": delFile,
    "cd": changeDir,
    "ls": fullDir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

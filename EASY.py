import os

def changedir(folder):
  
    try:
        os.chdir(folder)
        print("Рабочая директория успешно изменена на ", folder)
    except:
        print(" Директория не найдена! ")

def removedir(namedir):

    try:
        os.removedirs(namedir)
        print(f"Директория {namedir} успешно удалена")
    except:
        print(" Директория не найдена или не пуста! ")

def createdir(namedir):
    try:
        os.mkdir(namedir)
        print(f"Директория {namedir} успешно создана")
    except:
        print(" Что-то пошло не так ") 

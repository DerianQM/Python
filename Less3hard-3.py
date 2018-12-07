

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
import os
def create_file(fname,temp_sp):
    path_w = os.path.join( fname + '.txt')
    my_file = open(path_w, 'w')
    for i in  temp_sp:
        my_file.write(i)
    my_file.close()


path = os.path.join('fruits.txt')
with open(path, 'r') as line:
    mainfile = line.readlines()
    print("Строк в текущем файле", mainfile)

masssp = list(map(chr, range(ord('А'), ord('Я')+1)))


for i in masssp:
    temp_sp = []
    for k in mainfile:
        if k.startswith(i):
            temp_sp.append(k)
    if len(temp_sp):
        fname = i + '_fruits'
        create_file(fname, temp_sp)
        
print("Посмотри, сколько гадости я создал")

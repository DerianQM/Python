
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

def createdict(path):
    file = open(path,'r', encoding='UTF-8')
    strn = file.read().split("\n")[:-1]
    tempdict = dict() # создаем словарик и записываем ключ и значение , нарезая строку
    for item in strn:
        key = item.split(" ")[0]
        value = item.split(" ")[1:]
        tempdict[key] = value
        file.close()
    return(tempdict)

path = 'workers.txt'
dict1= createdict(path)
path = 'hours_of.txt'
dict2= createdict(path)

norm_hours = 30
result = dict()
print (dict1)
print (dict2)


for key in dict1:
    oklad = str(dict1[key])[2:-2]
    hours = str(dict2[key])[2:-2]
    if int(hours) < norm_hours:
        zp = round(int(oklad)*int(hours)/norm_hours)
    elif int(hours) > norm_hours:
        zp = round(int(oklad)/int(hours)*(int(hours)-norm_hours)*2+ int(oklad))
    else:
        zp = int(oklad)
    result[key] = zp    


with open('ZP.txt','w') as out:
    for key,val in result.items():
        out.write('{}:{}\n'.format(key,val))


print(result)


# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла




class Perents: #костыль
    def __init__(self, *args): # может принимать сколь угодно аргументов, недокоструктор
        self.sname = args[0]
        self.whours = int(args[1])
    def get_name(self):
        return f"{self.sname}"
class Worker(Perents):
    def __init__(self, dataline): # принимаю строку из файла
        _data = dataline.split()
        super().__init__(_data[0],_data[1])
        self.oklad = int(_data[2]) # это аля наш статик по часам, я его в файл занес, но можно было и просто число прописать
class WorkHours(Perents): #костыль
    def __init__(self, dataline):
        _data = dataline.split()
        super().__init__(_data[0],_data[1])

data_workers = []
hours_of = []
mass = dict()

with open("workers.txt", "r", encoding="UTF-8") as workers_file: # файл при такой записи сам закроется
     workers_file.readline()
     for line in workers_file:
         data_workers.append(Worker(line)) # читаю построчно и добавляю в список аргументы из строки
with open("hours_of.txt", "r", encoding="UTF-8") as hours_of_file:
     hours_of_file.readline()
     for line in hours_of_file:
         hours_of.append(WorkHours(line)) # читаю построчно и добавляю в список аргументы из строки

def ZP(oklad, norm_hours, fakt_hours): # это можно/нужно засунуть в класс , но времени уже нет
    if norm_hours >= fakt_hours:
        return oklad / norm_hours * fakt_hours
    else:
        return oklad + oklad/norm_hours * 2 * (fakt_hours - norm_hours)
for person in data_workers:
    for hours in hours_of:
        if person.get_name() == hours.get_name(): # сравниваю 2 значения фамилий
            zp = int(ZP(person.oklad, person.whours, hours.whours))
            mass.update({person.get_name():zp})
print(mass) # просто посмотреть
with open('ZP.txt','w') as out:
    for key,val in mass.items():
        out.write('{}:{}\n'.format(key,val))      
# буду рад любой критике, прога похожа на индусский код, но , через классы? - да, я художник, я так вижу, очень прошу скорректировать, может я лучше разберусь , потому как по мне я тут бред написал)
# тк золотым правилом является - класс не должен состоять из 1 функции и самого тела

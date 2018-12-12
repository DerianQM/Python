# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt

class triangle:
    def __init__(self,x1,x2,y1,y2,z1,z2):
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            self.z1 = z1
            self.z2 = z2
    def S (self):
        return abs((((self.x1- self.z1)*(self.y2-self.z2)-(self.y1-self.z1)*(self.x2-self.z2)))*0.5)
    def H (self):
        return round(abs((self.y2-self.z2)*self.x1 + (self.z1-self.y1)*self.x2 + (self.y1*self.z2 - self.z1*self.y2))/sqrt((self.y2 - self.z2)**2 + (self.z1- self.y1)**2),2)
    def P (self):
        return round( (sqrt (abs((self.y1-self.x1)**2-(self.y2-self.x2)**2)) + sqrt(abs((self.z1-self.y1)**2-(self.z2-self.y2)**2)) + sqrt(abs((self.z1-self.x1)**2-(self.z2-self.x2)**2))),2)

def createPoint():  # функция для создания списка координат, который введет пользователь
    listNew = []
    for f in range(6):
        print("Введите ", f + 1, "ю координату ")
        s = int(input())
        listNew.append(s)
    return (listNew)


mass = createPoint()

tr = triangle(mass[0],mass[1],mass[2],mass[3],mass[4],mass[5])

print("Площадь треугольника равна ",tr.S())
print("Высота треугольника равна ",tr.H())
print("Периметр треугольника равен ",tr.P())
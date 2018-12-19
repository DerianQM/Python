
import random
class Card:
     def __init__(self):
        self.card = [[], [], []]
        
     def __repr__(self):
        result = ''
        for row in self.card:
             for column in row:
                result += str(f'{column:>2} ') # гениальное создание сырой строки с 3мя \n  внутри, чтобы принт их разнес (взаимствованно)
             result += '\n'
        return result
     def prepare_card(self):
        numbers = random.sample(range(1, 91), 15)
        start = 0
        end = 5
        for row in self.card:
            sp = numbers[start:end] + list('-')*5 # по мне так лучше не придумать, разумнее, чем у богов(моя личная идея с подсказки Марии)
            random.shuffle(sp)
            for column in range(0, 10):
                row.append(sp[column])
            start += 5
            end += 5
     
     def cross_out(self, number):
        for row in self.card:
            if number in row:
                    row[row.index(number)] = 'x' # тоже лучше, чем у богов (да, я тоже на что то гожусь)
                    return True
        return False    

     def play(self, barrel, answer=None): # моя задумка, может и громоздко , но понятно и для любой карты
          
         if answer:
              check = self.cross_out(barrel)
              if   check == True and answer == 'y':
                   print("Верно")
              elif check == True and answer == 'n':
                   print("Вы проиграли, такая фишка у Вас была")
                   exit()
              elif check == False and answer == 'n':
                   pass
              else :
                   print("Вы проиграли, такой фишки у Вас не было")
                   exit()
         else:
               check = self.cross_out(barrel) # закоментить от if до еlse чтобы проверить победу, разве что потыкать на любую клавишу придется
               if   check == True:
                    print(f"Компьютер зачеркнул {barrel}")
         
          
     def victory(self):
           if len([column for row in self.card for column in row if type(column) == int]) > 0:
                return True
           else:
                return False


def checkVictory(player_card,ai_card):
         if player_card.victory()== False and ai_card.victory() == False: # проверяю на победу и не сую в класс, да, вот такой я
            print("У вас ничья!")
            exit()
         elif  player_card.victory()==False:
            print("Вы выиграли!")
            exit()
         elif ai_card.victory()==False:
            print("Победил компьютер!")
            exit()            
               
def showcard(card,name): # обрамляю карточку, да, хотел декоратор, оно даже очень похоже, хоть сендвичи лепи, но и так норм
     print(f"------ карточка {name} --------")
     print(card)
     print("-----------------------------")
   

player_card = Card() # создаю обьект класса 
player_card.prepare_card() # конструирую его
ai_card = Card()
ai_card.prepare_card()


barrels = random.sample(range(1, 91), 90) # список уникальных значений , позволяет sample создать
print("Добро пожаловать в сессию игры 'Лотто'")

for i, barrel in enumerate(barrels):
       print(f"Новый бочонок: {barrel}. Осталось бочонков: {len(barrels) - i - 1}")
       showcard(player_card,name = 'Ваша')
       showcard(ai_card,name = 'Kомпьютера')     
       player_card.play(barrel, input('Зачеркнуть цифру? (y/n):'))# обработка ответа и действие над обьектом класса, да , тут явно надо запихать в класс, тк это поведение
       ai_card.play(barrel)
       checkVictory(player_card,ai_card)# функция проверки на победу

#ненавижу классы, хоть с ними и проще
       
       






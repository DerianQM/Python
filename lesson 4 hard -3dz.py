mass = [[3, 1], [6, 2], [4,3], [2, 4], [8, 5], [5, 6], [7, 7], [1, 8]]# верный ряд, поменять любую цифру, чтоюы получить нет
# разблокировать, чтобы не вводить
#print(mass)

def horizontal(mass, row):
    tempmass = mass.copy()
    tempmass.remove(row)
    for ch  in tempmass:
        if row[0] == ch[0]:
            print("NO")
            exit()
        if row[1] == ch[1]:
            print("NO")
            exit()
def diagonal(mass,row):
    tempmass = mass.copy()
    tempmass.remove(row)
    for ch in tempmass:
        i=0
        j=0       
        while (ch[0]+i)<= 8 or (ch[1]+j)<= 8:
            if row == [ch[0]+i,ch[1]+j]:  
                print("NO")
                exit()            
            i+=1
            j+=1
           

    for ch in tempmass:
        i = 0
        j = 0
        while (ch[0]-i)>= 0 or (ch[1]-j)>= 0:
            if row == [ch[0]-i,ch[1]-j]:
                print("NO")
                exit() 
            i+=1
            j+=1
    
    for ch in tempmass:
        i = 0
        j = 0
        while (ch[0]+i)<= 8 or (ch[1]-j)>= 0:
            if row == [ch[0]+i,ch[1]-j]:
                print("NO")
                exit() 
            i+=1
            j+=1
    

    for ch in tempmass:
        i = 0
        j = 0
        while (ch[0]-i)>=0 or (ch[1]+j)<=8:
            if row == [ch[0]-i,ch[1]+j]:
                print("NO")
                exit() 
            i+=1
            j+=1





for row in mass:
     horizontal(mass, row) # проверка горизонталей и вертикалей
     diagonal(mass, row) #проверка диагоналей
print("YES")

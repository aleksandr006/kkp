a = [0]*4 
from random import *
from keyboard import *
for i in range (4):
    ver = 0
    while (ver==0):
        player = int(input("1 - kivi, 2 - käärid, 3 - paaber. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1
    a[i] = player     
    if player == 1:
        print("Olete valinud kivi.")
    if player == 2:
        print("Sa valisid käärid.")
    if player == 3:
        print("Valisite paberi.")
    comp=randint(1,3)
    if comp == 1:
        print("Arvuti valis kivi.")
    if comp == 2:
        print("Arvuti valis käärid.")
    if comp == 3:
        print("Arvuti valitud paber.")
    if player == comp:
        win = 0
    if player == 1 and comp == 2:
        win = 1 
    if player == 1 and comp == 3:
        win = 2
    if player == 2 and comp == 1:
        win = 2
    if player == 2 and comp == 3:
        win = 1
    if player == 3 and comp == 1:
        win = 1
    if player == 3 and comp == 2:
        win = 2
    if win == 0:
        print("viik!")
    if win == 1:
        print("Võitis mängija!")
    if win == 2:
        print("Võitnud arvuti!")
print (a)
k = 0
n = 0
b = 0
for i in range (4):
    if a[i] == 1:
        k = k+1
    if a[i] == 2:
        n = n+1
    if a[i] == 3:
        b = b+1
ver = 0
comp = 1
if k>2:
    comp=3
if n>2:
    comp = 1
if b>2:
    comp = 2
    
while (ver==0):
    player = int(input("1 - kivi, 2 - käärid, 3 - paaber. "))
    if (player == 1 or player == 2 or player == 3):
        ver = 1
if player == 1:
        print("Olete valinud kivi.")
if player == 2:
        print("Olete valinud käärid.")
if player == 3:
        print("Oled valinud oma paber")
if comp == 1:
        print("Arvuti valis kivi.")
if comp == 2:
        print("Arvuti valis käärid.")
if comp == 3:
        print("Arvuti valis paber.")
if player == comp:
        win = 0
if player == 1 and comp == 2:
        win = 1 
if player == 1 and comp == 3:
        win = 2
if player == 2 and comp == 1:
        win = 2
if player == 2 and comp == 3:
        win = 1
if player == 3 and comp == 1:
        win = 1
if player == 3 and comp == 2:
        win = 2
if win == 0:
        print("viik!")
if win == 1:
        print("Võitis mängija!")
if win == 2:
        print("Võitnud arvuti!")
v1=["kivi","käärid","paber"]
v2=["kivi","käärid","paber"]
b=0
c=0
p=''
from random import*
while p not in [1,2]:
    try:
        p=int(input('Выберите с кем хотите играть:\n1=игра с компом\n2=игра ботов'))
    except:
        TypeError
if p==1:
    while True:
        a=''
        while a not in [1,2,3,4]:
            try:
                a=int(input('Выберите камень=1, бумага=2, ножницы=3, закончить игру=4  ='))
            except:
                TypeError
        if a==4: break
        z=randint(1,3)
        if z==1:
            print('Компьютер выбрал камень')
        elif z==2:
            print('Компьютер выбрал бумага')
        else:
            print('Компьютер выбрал ножницы')
        if a==1 and z==3:
            print('Ты выйграл')
            b+=1
        elif a==z:
            print('Ничья')
        elif a==2 and z==3:
            print('Ты проиграл')
            c+=1
        elif a==3 and z==2:
            print('Ты выйграл')
            b+=1
        elif a==3 and z==1:
            print('Ты проиграл')
            c+=1
        elif a==2 and z==1:
            print('Ты выйграл')
            b+=1
        elif a==1 and z==2:
            print('Ты проиграл')
            c+=1
elif p==2:
    v1=['Камень','Ножницы','Бумага']
    v2=['Камень','Ножницы','Бумага']
    while True:
        print('Играем? esc= выходим, enter= играем')
        if read_key()=='esc':
            break
        elif read_key()=='enter':
            p1=choice(v1)
            print('Первый Бот: ',p1)
            p2=choice(v2)
            print('Второй Бот: ',p2)
            if p1==p2:
                print('Ничья')
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print('Выйграл 1')
            else:
                print('Выйграл 2')

import os
import random
draw, cwin, uwin = (0,0,0)   # For counting wins and draw
t,r = (0,10)                 # For end of loop
new = []
middle = ['SNAKE','GUN','WATER']
game =True
input('''Description of the game:\nThis is "snake, gun, water". This game will played 10 rounds between computer and user. 
Both computer and user can select anyone option between given three options(Snake, Water, Gun) and winner will be decided by rule as below :\n1.Between "Snake" and "Water" = Snake(Because snake can drink water)\n2.Between "Snake" and "Gun" = Gun(Because snake can killed by gun)\n3.Between "Gun" and "Water" = Water(gun will damage inside water)\npress enter for continue ''')
os.system('cls')
while game and t<10:
    print(f'You have {r} round only')
    user = input('''choose anyone\npress 1 for SNAKE\npress 2 for Gun\nPress 3 for WATER \n=>''')
    os.system('cls')

    while user != '1' and user !='2' and user!= '3':
        os.system('cls')
        print('Please select specified value')
        user = input('''choose anyone\npress 1 for SNAKE\npress 2 for GUN\npress 3 for WATER \n=>''')

    if (user=='1' or user=='2' or user=='3'):
        if user=='1':
            ser = 'SNAKE'
        elif user=='2':
            ser = 'GUN'
        elif user=='3':
            ser = 'WATER'
        random.shuffle(middle)
        new = new + [middle[0]]
        if (new[0]=='SNAKE' and user == '1') or (new[0]=='GUN' and user == '2') or (new[0]=='WATER' and user == '3'):
            draw+=1
            print(f'Game draw\nComputer : {new[0]}\nUser : {ser}')
        elif new[0]=='GUN' and user == '1':
            cwin +=1
            print('Computer win this round\nComputer : GUN\nUser : SNAKE')
        elif new[0]=='WATER' and user == '1':
            uwin +=1
            print('User win this round\nComputer : WATER\nUser : SNAKE')

        elif new[0]=='SNAKE' and user == '2':
            uwin +=1
            print('User win this round\nComputer : SNAKE\nUser : GUN')
        elif new[0]=='WATER' and user == '2':
            cwin +=1
            print('Computer win this round\nComputer : WATER\nUser : GUN')        

        elif new[0]=='SNAKE' and user == '3':
            cwin +=1
            print('Computer win this round\nComputer : SNAKE\nUser : WATER')
        elif new[0]=='GUN' and user == '3':
            uwin +=1
            print('User win this round\nComputer : GUN\nUser : WATER')


        # input('press enter for next round')
        t+=1
        r-=1
        new.pop()
        if t==10 and r==0:
            print(f"Total rounds =10\nComputer win {cwin} rounds\nUser win {uwin} rounds\nDraw {draw}")
            game = False
            break
        elif t<10 and r>0:
            input('press enter for next round')
        os.system('cls')
           

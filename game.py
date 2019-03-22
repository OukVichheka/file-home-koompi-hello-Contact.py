from enum import Enum
import random

class mmenu(Enum):
    Lnum = '1'
    Rock = '2'
    Exit = '0'
class rmenu(Enum):
    PwB = '1'
    PwP = '2'
    Exit = '0'                                                                                                                                                          
        
class choice(Enum):
    Rock = 1
    Paper = 2
    Scissor = 3


def PB():
    while True:
        Bchoice = random.randint(1,4)   #Banswer = Bot Choice
        pn = input('Enter your name or press 0 and enter to go back:') #pn = PlayerName
        if pn == '0':
            print('Thank you for playing')
            break
        print(f'Player Name:{pn}')
        print('1.Rock')
        print('2.Paper')
        print('3.Scissor')
        Pchoice = input('Enter your choice:') #Pchoice = Player Choice
        Pchoice = int(Pchoice)
        if Bchoice == choice.Rock.value:
            if Pchoice == choice.Paper.value:
                print(f'Bot answer is {Bchoice}')
                print(f'{pn} win the game')
            elif Pchoice == choice.Scissor.value:
                print(f'Bot answer is {Bchoice}')
                print('Bot win the game')
        elif Bchoice == choice.Paper.value:
            if Pchoice == choice.Rock.value:
                print(f'Bot answer is{Bchoice}')
                print(f'{pn} win the game')
            elif Pchoice == choice.Scissor.value:
                print(f'Bot answer is {Bchoice}')
                print('Bot win the game')
        elif Bchoice == choice.Scissor.value:
            if Pchoice == choice.Paper.value:
                print(f'Bot answer is {Bchoice}')
                print('Bot win the game')
            elif Pchoice == choice.Rock.value:
                print(f'Bot answer is {Bchoice}')
                print(f'{pn} win the game')
    return  

    
def PP():
    while True:
        print('If you want to go back just press 0 and enter ^_^')
        Np1 = input('Enter your name Player1:') #Np1 = Name Player 1
        Np2 = input('Enter your name Playe2:')  #Np2 = Name Player 2
        if Np1 or Np2 == 0:
            break
        print('1.Rock')
        print('2.Paper')
        print('3.Scissor')
        print('Please enter your choice:')
        P1choice = input(f'{Np1}:') #P1choice = Player 1 Choice
        P2choice = input(f'{Np2}:') #P2choice = Player 2 Choice
        if P1choice ==  choice.Rock.value:
            if P2choice == choice.Paper.value:
                print(f'{Np2} win the game')
            elif P2choice == choice.scissor.value: 
                print(f'{Np1} win the game')
        elif P1choice == choice.Paper.value:
            if P2choice == choice.Rock.value:
                print(f'{Np2} win the game ')
            elif P2choice == choice.Scissor.value:
                print(f'{Np1} win the game ')
        elif P1choice  == choice.scissor.value:
            if P2choice == choice.Paper.value:
                print(f'{Np2} win the game')
            elif P2choice == choice.Scissor.value:
                print(f'{Np1} win the game')
    return 


def LuckyGame1():
    while True:
        Num = input('Enter number from 1-100 or Press 0 and Enter to exit:')
        Num = int(Num)
        RanNum = random.randint(1,101)
        if Num == 0:
            break
        elif Num == RanNum:
            print('----------')
            print(f'You win')
            print('----------')
        else :
            print('-'*47)
            print('You lose')
            print(f'The Number is {RanNum} But your number is {Num}')
            print('-'*47)
    return


def RockGame2():
    print('Welcome to rock paper and scissors game')
    while True:
        print('1.Play with Bot')
        print('2.Play with your Partner')
        print('0.Exit')
        Rmenu = input('>>>')
        if Rmenu == rmenu.PwB.value:    #PwBw = Play With Bot
            PB()
        elif Rmenu == rmenu.PwP.value:    #PwP = Play with Player
            PP()
        elif Rmenu == rmenu.Exit.value:
            break
    return


def MainMenu():
    print('Welcome to the jungle Game')
    while True:
        print('Choose the game you want to play')
        print('1.Lucky Number')
        print('2.Rock Paper Scissor')
        print('0.Exit')
        Mmenu = input('>>>')
        if Mmenu == mmenu.Lnum.value:
            LuckyGame1()
        elif Mmenu == mmenu.Rock.value:
            RockGame2()
        elif Mmenu == mmenu.Exit.value:
            break
    return


MainMenu()
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:38:43 2021

@author: GodwinEke
"""
import time
import random
random_number=random.randint(1,100)

#Definition of functions
#---------------------------------------------
def delay():
    """
    input:none
    Function made to add delay in code execution
    Return None
    """
    time.sleep(2)
     
def Game():
    """
    Input: None.
    It loops the number of attempts (7 times) made to guess the number.
    If not gotten after 7 trials, it breaks.
    returns None.
    
    """
    
    trials=7
    attempts=0
    while attempts <= trials:
        guess=int(input(f'Guess the number({trials-attempts} trial/s remaining): '))
        if guess< random_number:
            print('Guess higher')
        elif guess> random_number:
            print('Guess lower')
        else:
            print('Wow... you really got me')
            print('Congratulations. You really are smart.')
            delay()
            print("No. I hate losing. Let's play again.")
            break
        if attempts+1 ==trials:
            print(f'Sorry mate. I won this time. Answer was {random_number}.')
            break
        attempts+=1


#Start the game
#---------------------------------------------
print("Welcome to Erikwonda's Game!!")
delay()
print('You are going to guess the number I picked randomly from 1-100')
delay()
print ('You have seven trials.\n')
delay()


status_answer=input ('Are you ready? type Y/N: ')
if status_answer=='Y' or status_answer=='y' or status_answer=='Yes' or status_answer=='yes':
    print('Yeah!!! On your marks...')
    delay()
    print('Set..')
    delay()
    print ('Go!!!!!')
    
#---------------------------------------------
#Game code execution    
    Game()

#If user wants to play again, this causes the loop
#---------------------------------------------
    while True:
        end_answer=input('\n Do you feel like playing? Type Y/N: ')
        if end_answer=='Y' or end_answer=='y':
            print ("Let's go!!!")
            random_number=random.randint(1,100)
            Game()
        elif end_answer=='N' or end_answer=='n'or end_answer=='no' or end_answer=='NO':
            print("Yh me too. I think that's cool for today. If you wanna play, you know where to find me.")
            print("PEACE!!!!!!!!!!!!")
            break
else:
    print("Ugh...Just play please '---'")
    status_answer2=input('Do you want to play? just say Yes..Pleaseeeeee: ')
    if status_answer2=='Y' or status_answer2=='y' or status_answer2=='Yes' or status_answer=='YES':
        print('Yeeeeeeeeeeeeeeeh!! On your marks...')
        print('Set..')
        print ('Go!!!!!')
    else:
        print('Well. Sorry to see you go. Anytimw you want to play, you know where to find me!')
        print('Have a great day!!')  
       


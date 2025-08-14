'''
   author:Gideon Wang
   version:1
'''
#-------------libraries--------
import random
#-------------functions---------

#------------main routine----------
hp=100#our hitpoints
dff=13#our defence
en_hp=100#enemy hitpoints
en_dff=13#enemy defence
while hp>0 and en_hp>0:#checking if both alive
    while(True):
        try:#tests the code if it will fail
            attack=input('''
                enter your attack:
                [s]word
                [a]xe
                [h]eal
                ''')#enter our attack
            if attack[0].lower()=='s' or attack[0].lower()=='a' or attack[0].lower()=='h':
                break
            else:
                print("invalid selection")
        except:
            print("your input was not correct input")
    #checking what the user entered
    if attack=='s':#when the user enters s for sword attack
        pass
    elif attack=='a':
        pass
    elif attack=='h':
        pass
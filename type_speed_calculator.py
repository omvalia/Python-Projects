#Typing Speed Calculator Python Project
#This is a console based project

from time import *
import random as r

#Function for calculating the mistakes
def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error=error+1
        except:
             error=error+1
    return error

#Function to calculate speed of typing per minute
def speed_time(time_start,time_end,userinput):
    time_delay=(time_end-time_start)
    time_round=round(time_delay,2)
    speed=(len(userinput)/time_round)*6
    return round(speed)

if __name__=='__main__':
    while True:
        ck=input("Ready for the test yes/no: ")
        if ck=="yes":
        #Random Paragraphs 
            test = ['''She counted. One. She could hear the steps coming closer. Two. Puffs of breath could be seen coming.''',

                    '''He couldn't move. His head throbbed and spun. He couldn't decide if it was the flu or the drinking.''',

                    '''MaryLou wore the tiara with pride. There was something that made doing anything she didn't really.'''
                    ]

            test1=r.choice(test)

            print("    ****Typing Speed Calculator****    ")
            print()
            print(test1)
            print()
            time_1=time()
            testinput=input("Enter: ")
            time_2=time()

            print("Speed: ",speed_time(time_1,time_2,testinput),"word/per minute")
            print("Error: ",mistake(test1,testinput))
        
        elif ck=="no":
            print("Thank you for visiting")
            break
        else:
            print("Type yes or no....")

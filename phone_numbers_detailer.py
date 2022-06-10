#Phone Number details Python Project
#In this project we can fetch the information of any registered phone number
#For this we need to add phonenumber library using (pip install phonenumbers)

import phonenumbers                                     #Importing phonenumbers package to get phone number details
from phonenumbers import timezone,geocoder,carrier   

number = input("Enter Your No. with +__: ")             
phone=phonenumbers.parse(number)                        #This will print the phone number
time=timezone.time_zones_for_number(phone)              #This will print the time zone ('Asia/Calcutta')
carr=carrier.name_for_number(phone,"en")                #This will print the carrier provider (Airtel/Jio)
reg=geocoder.description_for_number(phone,"en")         #This will print tthe location of the phone number (India)

#Printing the details
print(phone)
print(time)
print(carr)
print(reg)

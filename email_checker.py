#Email Checker Python Project
#This is console based project 
#Email is taken in form of a string and then it is checked through various level of conditions

#1 - Check the length of email (should not be less than 6 characters)
#2 - Check if the first letter of email is an alphabet or not
#3 - Check whether the email consist of "@" symbol and also check its position
#4 - Check whether the email consist of "." symbo; and also check its position
#5 - Check whether the email consist of any spaces/uppercase/invalid characrer


print("Check your Email!!!")
email=input("Enter your email: ")
k=0
j=0
d=0
if len(email)>=6:                                                                                              #1
    if email[0].isalpha():                                                                                     #2
        if ("@" in email) and (email.count("@")==1):                                                           #3
            if(email[-4]==".") ^ (email[-3]=="."):                                                             #4
                for i in email:
                    if i==i.isspace():                                                                         #5
                        k=1
                    elif i.isalpha():
                        if i==i.upper():                                                                       
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("There is space or uppercase or invalid character in your email!!")                 #5
                else:
                    print("You have a correct email id!!!")
            else:
                print(". should be before 3/4 characters of your email!!")                                    #4
        else:
            print("@ character error!!")                                                                      #3
    else:
        print("First character of email should be an alphabet!!")                                             #2
else:
    print("Email has less than 6 characters!!")                                                                #1            




class Committees: 
    def askUser(self):
        x = input("\nPress 1 to Go back or Enter any other input to exit: ")
        if(x == "1"):
            return x
        else:
            print("\nThank you for visting!\n")
            quit()

    def upg_committee(self,comm):
        if(comm == 1):
            print("\nStudent's Council :")
            print("For more details click on: https://www.upgcm.ac.in/Students%20Council/M__27\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
            
        elif(comm == 2):
            print("\nCultural Committee :")
            print("For more details click on: https://www.upgcm.ac.in/Cultural%20Committee/M__28\n")
            print("Follow: https://www.instagram.com/upgculturalcommittee/\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
          
        elif(comm == 3):
            print("\nSports Committee :")
            print("For more details click on: https://www.upgcm.ac.in/Sports/M__36\n")
            print("Follow: https://www.instagram.com/upgsportscommittee/\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
  
        elif(comm == 4):
            print("\nMONTAGE :")
            print("For more details click on: https://www.upgcm.ac.in/MONTAGE/M__145\n")
            print("Follow: https://www.instagram.com/upgmontage/\n")
 
            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
         
        elif(comm == 5):
            print("\nNational Service Scheme :")
            print("For more details click on: https://www.upgcm.ac.in/National%20Service%20Scheme/M__31\n")
            print("Follow: https://www.instagram.com/upg.nss/\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
  
        elif(comm == 6):
            print("\nWomen Development Cell :")
            print("For more details click on: https://www.upgcm.ac.in/Women%20Development%20Cell/M__107\n")
            print("Follow: https://www.instagram.com/upg_wdc/\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
          
        elif(comm == 7):
            print("\nSocial Outreach Unit :")
            print("For more details click on: https://www.upgcm.ac.in/Social%20Outreach%20Unit/M__110\n")
            print("Follow: https://www.instagram.com/sou.yearbook//\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
          
        elif(comm == 8):
            print("\nEntrepreneurship Cell :")
            print("For more details click on: https://www.upgcm.ac.in/Entrepreneurship%20Cell/M__55\n")
            print("Follow: https://www.instagram.com/ecellupg/\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
          
        elif(comm == 9):
            print("\nThe Buddy Project :")
            print("For more details click on: https://www.upgcm.ac.in/The%20Buddy%20Project/M__101\n")
            print("Follow: https://www.instagram.com/upg.tbp/\n")
 
            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
         
        elif(comm == 10):
            print("\nRotaract Club :")
            print("For more details click on: https://www.upgcm.ac.in/Rotaract/M__34\n")
            print("Follow: https://www.instagram.com/rc.upg/\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
          
        elif(comm == 11):
            print("\nEloquence :")
            print("For more details click on: https://www.upgcm.ac.in/Eloquence/M__123\n")
            print("Follow: https://www.instagram.com/upgdlle/\n")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
          
        elif(comm == 12):
            print("\nUPG Pulse :")
            print("For more details click on: https://www.upgcm.ac.in/UPG%20Pulse/M__111n")
 
            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
         
        elif(comm == 13):
            print("\nSoft Skills :")
            print("For more details click on: https://www.upgcm.ac.in/Soft%20Skills/M__47")

            if(s.askUser() == "1"):        #calling to line 5
                s.comList()        #calling to line 574
          
        elif(comm == 14):
            s.giveOptions()        #calling to line 662

class Events(Committees):
    def printLine(self):
        print("---------------------------------------------------------")

    def eventIT(self,option):
        if(option == 1):
            print("\nInternational Conference 2022: ")
            print("Topic : Emerging Trends in Digital Technologies")
            print("https://upgcm.ac.in/International%20Conference%202022/M__176")

            if(s.askUser() == "1"):        #calling to line 5
                s.event(10)        #calling to line 182
 
        elif(option == 2):
            print("\nInternational Conference 2021: ")
            print("Topic : Emerging Trends in Digital Technologies")
            print("https://upgcm.ac.in/http//upgcm.ac.in/InternationalConference2021/M%20%20164/M__164")
            print("Registration form : https://upgcm.ac.in/International%20Conference%20Registration%20Form/M__165")

            if(s.askUser() == "1"):        #calling to line 5
                s.event(10)        #calling to line 182
                      
        elif(option == 3):
            print("\nUPG's Techvanza: ")
            print("https://upgcm.ac.in/UPGs%20Techvanza/M__160")
            print("Gallery : https://upgcm.ac.in/PhotoGallery_SlideShow.aspx?MKey=161&cKey=6")

            if(s.askUser() == "1"):        #calling to line 5
                s.event(10)        #calling to line 182
               
        elif(option == 4):
            print("\nNational Conference: ")
            print("Topic : Emerging Trends in Digital Technologies - 2020")
            print("https://upgcm.ac.in/http//upgcm.ac.in/NationalConferenceRegistrationForm/M%20%20154/M__150")
            print("Registration form : https://upgcm.ac.in/National%20Conference%20Registration%20Form/M__154")

            if(s.askUser() == "1"):        #calling to line 5
                s.event(10)        #calling to line 182
               
        elif(option == 5):
            print("\nIOT Workshop: ")
            print('''
            Usha Pravin Gandhi College of Arts, Science and  Commerce in association with Ad-Hoc Board of
            Studies in Information technology , University of Mumbai conducted a one-day workshop for
            the Revised Syllabus  of T.Y.B.Sc.I.T Semester V in the subject of " Internet of Things"  on
            17th  July,2018. The workshop was attended by the 130 faculty members of various affiliated
            colleges of University of Mumbai. Resource persons Prof Hiren Dand and Prof. Mandar Bhave
            conducted the hands-on sessions to  provide the insights of the practical's based on the Raspberry
            Pi module.
            ''')

            if(s.askUser() == "1"):        #calling to line 5
                s.event(10)        #calling to line 182
 
        elif(option == 6):
            print("\nTechnovation: ")
            print("https://upgcm.ac.in/Technovation/M__141")

            if(s.askUser() == "1"):        #calling to line 5
                s.event(10)          #calling to line 182
 
        elif(option == 7):
            s.eventList()          #calling to line 604

    def event(self,option):
        if(option == 1):
            print("\nWorkshop on Research Methodology: ")
            print("https://upgcm.ac.in/Workshop%20on%20Research%20Methodology/M__157")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
 
        elif(option == 2):
            print("\nUPG's LitFest: ")
            print("https://upgcm.ac.in/UPGs%20LitFest/M__136")    
            print("Gallery : https://upgcm.ac.in/PhotoGallery_SlideShow.aspx?MKey=137&cKey=5")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
 
        elif(option == 3):
            print("\nUPGCM and Salaam Baalak: ")
            print("https://upgcm.ac.in/UPGCM%20and%20Salaam%20Baalak/M__127")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
                
        elif(option == 4):
            print("\nGanesh Chaturthi 2018: ")
            print("Day 1 : https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/398_Download_Day1.pdf")
            print("Day 2 : https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/399_Download_Day2.pdf")
            print("Day 3 : https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/400_Download_DAy%203.pdf")
            print("Day 4 : https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/401_Download_Day%204.pdf")
            print("Day 5 : https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/402_Download_Day%205.pdf")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
  
        elif(option == 5):
            print("\nTree Ganesha: ")
            print("https://upgcm.ac.in/Tree%20Ganesha/M__102")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
   
        elif(option == 6):
            print("\nE Waste")
            print("E-waste Project Report: ")
            print("http://www.upgcm.ac.in/Common/Uploads/HomeTemplate/CDoc_EWASTE-3.pdf")
            print("\nSVKM UPG College - Sony Music OASIS E Waste Video Link :")
            print("https://www.youtube.com/watch?v=og3hJhpTlE4")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
                
        elif(option == 7):
            print("\nRUR Seminar: ")
            print("https://upgcm.ac.in/RUR%20Seminar/M__129")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
               
        elif(option == 8):
            print("\nIQAC seminar on Sports and Entertainment: ")
            print("https://upgcm.ac.in/IQAC%20seminar%20on%20Sports%20and%20Entertainment/M__135")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
                
        elif(option == 9):
            print("\nEvents of B.M.S :")
            print("International Conference 2021")
            print("Topic : Unlocking the potential of Post-Covid Digital transformations in Management")
            print("https://upgcm.ac.in/International%20Conference%202021/M__206")

            if(s.askUser() == "1"):        #calling to line 5
                s.eventList()        #calling to line 604
 
        elif(option == 10):
            print("\nEvents of B.Sc.(I.T): ")
            print('''            1. International Conference 2022
            2. International Conference 2021
            3. UPG's Techvanza
            4. National Conference
            5. IOT Workshop
            6. Technovation
            7. Go back
            ''')

            action1 = int(input("Please select one of the option: "))
            try:
                if(action1 > 7 or action1 < 1):
                    raise Exception
            except Exception:
                print("\nPlease Enter Valid Number within 1 and 7 only")
                s.printLine()        #calling to line 475
                s.eventList(10)        #calling to line 604
            else:
                s.eventIT(action1)        #calling to line 119
        
        elif(option == 11):
            s.giveOptions()        #calling to line 662

class courseInformation(Events):
    def optionSelction(self):
        print('''        1. Syllabus.
        2. Faculty.
        3. Go Back
        ''')

        selectedOption = int(input("Please Enter number: "))
        try:
            if(selectedOption > 3 or selectedOption < 1):
                raise Exception
        except Exception:
            print("\nPlease Enter Valid Number within 1 and 3 only")
            return
        else:
            return selectedOption

    def firstBscIt(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("Bachelor of Science (Information Technlogy).")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("First Year Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/446_Download_FYBScIT-Syllabus-2016-17.pdf")
            print("\nSecond Year Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/447_Download_S.Y.B.Sc_.-Information-Technology1.pdf")
            print("\nThird Year Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/448_Download_Final-TYBSc-IT-Syllabus-2.pdf")
            
            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490

        elif(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            print("https://upgcm.ac.in/BSc%20IT/M__16")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490

        elif(act == 3):
            s.secondCourse()        #calling to line 490

        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.firstBscIt()        #calling to line 298

            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()        #calling to line 282
        
    def secondBMS(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("Bachelor of Mangement Studies.")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("First Year Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/326_Download_sem12.pdf")
            print("\nSecond Year Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/327_Download_sem34.pdf")
            print("\nThird Year Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/325_Download_sem56.pdf")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()         #calling to line 490 

        elif(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            print("https://upgcm.ac.in/BMS/M__14")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()         #calling to line 490 
                 
        elif(act == 3):
            s.secondCourse()        #calling to line 490
 
        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.secondBMS()        #calling to line 332
            
            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()        #calling to line 282  

    def thirdBMM(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("BMM also known as BA (Multimedia and Mass Communication).")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("Full Course Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/445_Download_CDoc_BA%20FTNMP%20Revised%20Syllabus.pdf")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490
                             
        elif(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            print("https://upgcm.ac.in/BMM/M__15")
            
            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490
                 
        elif(act == 3):
            s.secondCourse()        #calling to line 490

        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.thirdBMM()        #calling to line 366
            
            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()         #calling to line 282 
                 
    def fourthMscIt(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("Master of Science (Information Technlogy).")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("First Year Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/450_Download_M.Sc_.-IT-Part-1-Syllabus-2019-20-onse-side-converted.pdf")
            print("\nSecond Year Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/449_Download_M.Sc.I.T.%20Part%202%20Final%20Syllabus%202020-2021.pdf")
 
            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()         #calling to line 490
                            
        elif(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            print("https://upgcm.ac.in/MSc%20IT/M__17")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()         #calling to line 490
                 
        elif(act == 3):
            s.secondCourse()        #calling to line 490

        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.fourthMscIt()        #calling to line 396

            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()        #calling to line 282  
                 
    def fifthMA(self):
        act = s.optionSelction()        #calling to line 282
        s.printLine()        #calling to line 475
        print("Masters of Arts (Entertainment media and Advertising)")
        s.printLine()        #calling to line 475

        if(act == 1):
            print("Full Course Syllabus: ")
            print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/710_Download_MAEMA%20Revised%20Syllabus.pdf")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490
                 
        if(act == 2):
            print("Please Open below Link to see faculty member, you will be directed to collge official website!")
            print("https://upgcm.ac.in/M.A%20[EMA]/M__144")

            if(s.askUser() == "1"):        #calling to line 5
                s.secondCourse()        #calling to line 490
                 
        elif(act == 3):
            s.secondCourse()        #calling to line 490
                          
        else:
            print("Please Enter Valid Number between 1 and 3 only")
            s.fifthMA()        #calling to line 428
        
            if(s.askUser() == "1"):        #calling to line 5
                s.optionSelction()         #calling to line 282 
                 
    def selectedOptionAction2(self, option):
        s.printLine()        #calling to line 475

        if(option == 1):
            s.firstBscIt()        #calling to line 298
        elif(option == 2):
            s.secondBMS()        #calling to line 332
        elif(option == 3):
            s.thirdBMM()        #calling to line 366
        elif(option == 4):
            s.fourthMscIt()        #calling to line 396
        elif(option == 5):
            s.fifthMA()        #calling to line 428
        else:
            s.giveOptions()        #calling to line 662
            
class chatbotFunction(courseInformation):
    def printLine(self):
        print("---------------------------------------------------------")

    def firstAboutUpg(self):
        s.printLine()        #calling to line 475
        print("About College")
        s.printLine()        #calling to line 475

        print("\nUsha Pravin Gandhi College of Management (NAAC A Grade), also known as UPG College, is a college in Vile Parle, Mumbai, India. \nUPG College is affiliated with the University of Mumbai, Mumbai (NAAC A++ Grade). \nUPG College is a branch of the SVKM Group Shri Vile Parle Kelavani Mandal.")
        print("\nThe College was established by Shri Vile Parle Kelavani Mandal in 2003.\nSince its inception in 2003, Usha Pravin Gandhi College has introduced many courses. \nThe college has introduced un-aided courses like, \n\n1) Bachelors in Management Studies (BMS), \n2) Bachelors in Mass Media (BMM), \n3) Bachelors in Information Technology (BSc.IT) and \n4) Masters in Information Technology (MSc.IT).")
        print("\nFor more Details Please Visit: http://upgcm.ac.in/Index.aspx")
        
        if(s.askUser() == "1"):        #calling to line 5
            s.giveOptions()        #calling to line 662
            
    def secondCourse(self):
        s.printLine()        #calling to line 475
        print("With which course I can help you?")
        print('''        1. Bachelor of Science (Information Technlogy).
        2. Bachelor of Mangement Studies.
        3. BMM also known as BA (Multimedia and Mass Communication).
        4. Master of Science (Information Technlogy).
        5. Masters of Arts (Entertainment media and Advertising).
        6. Go Back
        ''')

        action2 = int(input("Please select one of the option: "))
        try:
            if(action2 > 6 or action2 < 1):
                raise Exception
        except Exception:
            print("\nPlease Enter Valid Number within 1 and 6 only")
            s.secondCourse()        #Recalling Itself (line 487)
        else:
            s.selectedOptionAction2(action2)        #calling to line 455

    def thirdAdmission(self):
        s.printLine()        #calling to line 475
        print("New Admission Details")
        s.printLine()        #calling to line 475
        print("\nPlease Open below Link, you will be directed to collge official website!\nYou will find all the necessary details about admission eligibilty, process and fee structure.")
        print("https://upgcm.ac.in/Common/Uploads/TabbedContentTemplate/1_Down_First%20Year%20Admission%20notice%202019-20.pdf")
        print("\n\nPlease Open Below link for 2017-21 Cut off list")
        print("https://upgcm.ac.in/Common/Uploads/HomeTemplate/CDoc_CUT-OFF%20LIST%20%202017-21.pdf")

        if(s.askUser() == "1"):        #calling to line 5
            s.giveOptions()        #calling to line 662

    def fourthNoticeBoard(self):
        s.printLine()        #calling to line 475
        print("Notice Board")
        s.printLine()        #calling to line 475
        print("\nPlease Open below Link, you will be directed to collge official website!")
        print("https://upgcm.ac.in/Result-(B.M.M.%20,B.M.S.%20,%20B.Sc.(I.T.),%20B.A.%20,%20M.A.)/M__62")
        print("\nYou will find all the necessary details from this notice board.")

        if(s.askUser() == "1"):        #calling to line 5
            s.giveOptions()        #calling to line 662

    def fifthContactUs(self):
        s.printLine()        #calling to line 475
        print("Contact Us")
        s.printLine()        #calling to line 475

        e = int(input("Press 1 to fill Enquiry Form or \nPress 2 for College Contact Details: "))
        if(e == 1):
            s.printLine()        #calling to line 475
            print("Conatct Us Form")
            s.printLine()        #calling to line 475
            name=input("Enter your name: ")
            phoneNumber=input("Enter your phone number: ")
            emailId=input("Enter your Email Id: ")
            q=input("What is your query?\n")

            fp = open("ContactUsForm.txt", "a")
            fp.write("\n\nName: "+ name)
            fp.write("\nPhone number: "+ phoneNumber)
            fp.write("\nEmail Id: "+ emailId)
            fp.write("\nQuery: "+ q)
            fp.close()

            print("\nThank you for your interest!\nCollege will contact you as soon as possible!")

            if(s.askUser() == "1"):        #calling to line 5
                s.giveOptions()        #calling to line 662

        elif(e == 2):
            print("\nShri Vile Parle Kelavani Mandal's\nUsha Pravin Gandhi College of Arts, Science and Commerce,\nBhakti Vedanta Swami Marg,\nJuhu Scheme, Vile Parle (West),\nMumbai 400 056.\nMaharashtra, India")
            print("\nContact No: 42332041- 44")
            print("\nEmail Id: Info@upgcm.ac.in")
            print("\nFax. : 91-22-2613 6468")
            
            if(s.askUser() == "1"):        #calling to line 5
                s.giveOptions()        #calling to line 662
        
        else:
            print("Please Enter Valid Input")
            s.fifthContactUs();        #calling to line 534

    def comList(self):
        s.printLine()
        print("Committees")
        s.printLine()
        print('''        1. Student's Council
        2. Cultural Committee
        3. Sports Committee
        4. MONTAGE 
        5. National Service Scheme
        6. Women Development Cell
        7. Social Outreach Unit
        8. Entrepreneurship Cell
        9. The Buddy Project
        10. Rotaract Club
        11. Eloquence
        12. UPG Pulse
        13. Soft Skills
        14. Go back
        ''') 
    
        enter1 = int(input("Please select one of the option: "))
        try:
            if(enter1>14 or enter1<1):        #calling to line 5
                raise Exception
        except Exception:
            print("Enter a valid number between 1 to 14 only")
            s.comList()         #Recalling itself (line 571)
        else:
            s.upg_committee(enter1)         #calling to line 13

    def eventList(self):
        s.printLine()
        print("Events")
        s.printLine()
        print('''        1. Workshop on Research Methodology
        2. UPG's LitFest
        3. UPGCM and Salaam Baalak
        4. Ganesh Chaturthi 2018
        5. Tree Ganesha
        6. E Waste
        7. RUR Seminar
        8. IQAC seminar on Sports and Entertainment
        9. Events of B.M.S
        10. Events of B.Sc.(I.T)
        11. Go Back
        ''') 

        action = int(input("Please select one of the option: "))
        try:
            if(action > 11 or action < 1):
                raise Exception
        except Exception:
            print("\nPlease Enter Valid Number within 1 and 11 only")
            s.eventList()        #Recalling itself (line 601)
        else:
            s.event(action)        #calling to line 179   
        
    def fullExit(self):
        print("\nThank you for visting!")
        quit()

    def selectedOptionAction1(self, option):
        if(option == 1):
            s.firstAboutUpg()        #calling to line 478
        elif(option == 2):
            s.secondCourse()         #calling to line 490
        elif(option == 3):
            s.thirdAdmission()       #calling to line 511
        elif(option == 4):
            s.fourthNoticeBoard()    #calling to line 523
        elif(option == 5):
            s.fifthContactUs()       #calling to line 534
        elif(option == 6):
            s.comList()              #calling to line 574
        elif(option == 7):
            s.eventList()            #calling to line 604
        elif(option == 8):
            s.fullExit()             #calling to line 631

#Chatbot will start from here
class startChatbot(chatbotFunction):
    def startBot(self):
        print("\n")
        s.printLine()                 #calling to line 475
        print("Welcome to SVKM's Usha Pravin Gandhi College of Mangement\n\nI am Skyra, your assistant.")
        s.printLine()                 #calling to line 475
        s.giveOptions()               #calling to line 662

    def giveOptions(self):
        print("\nHow can I help you?:")
        print('''        1. About College
        2. Courses
        3. New Admission Details / Cut-Off List 2017-20
        4. Notice Board
        5. Contact us
        6. Committee
        7. Events
        8. Exit
        ''')
        
        action1 = int(input("Please select one of the option: "))
        try:
            if(action1 > 8 or action1 < 1):
                raise Exception
        except Exception:
            print("\nPlease Enter Valid Number within 1 and 8 only")
            s.giveOptions()                 #Recalling itself for valid  (line 662)
        else:
            s.selectedOptionAction1(action1)        #calling to line 635

s = startChatbot()         #Creating object of class startChatbot()
s.startBot()           #Triggering the event
 

'''
 ------Group Members------

   53003200001 - Dharmik
   53003205036 - Arpita 
   53003205022 - Srunjay
   53003205013 - Om
   53003205020 - Zeal

'''

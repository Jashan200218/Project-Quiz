'''
1)User input
: emp id , name , dept_name , Dept_number
2)game start

hint -> like 1 = monday etc.
        means work load
        : includes hr , sales , marketing department
        
        if(dept == hr):
        work load : hr ( hiring , meetings)
        proper schedule
        
        assign : email id 
        
        if(dept == sales):
        report (product details : 3 products)
        
        if(dept == marketing):
        work load
        
        else:
        ( bad luck : double work load)
'''







print("|**************************************************************************|")
print("|                   WELCOME TO GUESS THE FORTUNE DAY GAME                  |")
print("|**************************************************************************|")

print()
Emp_id=int(input("Please Enter your Employee ID : "))
Emp_Name=input("Enter your Name : ")
dept_name=input("Enter your Department Name : ")
print("|**************************************************************************|")
print("|                             GUESS GAME START                             |")
print("|**************************************************************************|")


fortune_number=int(input("Enter a number for the Fortune day(1-7) : "))

if fortune_number==1:
    fortune_day="Monday"
elif fortune_number==2:
    fortune_day="Tuesday"
elif fortune_number==3:
    fortune_day="Wednesday"
elif fortune_number==4:
    fortune_day="Thursday"
elif fortune_number==5:
    fortune_day="Friday"
elif fortune_number==6:
    fortune_day="Saturday"
elif fortune_number==7:
    fortune_day="Sunday"
else:
    print("Sorry Wrong Number ! Please Enter the number between 1 to 7 ")
print()    
                                 

department = input("Enter the Department(HR,Sales,Marketing) : ")


if(department=='HR'):
    print("|============WELCOME TO THE HR DEPARTMENT===============|")
    print()
    fort_num=int(input("Please Enter a number to check your fortune : "))
    print()
    if fort_num==fortune_number:
        print("|---------------------------------------------------|")
        print("| Time       | Task Description                     |")
        print("|---------------------------------------------------|")
        print("| 09:00 AM   | Team Meeting                         |")
        print("| 10:00 AM   | Recruitment                          |")
        print("| 11:00 AM   | Employee Onboarding                  |")
        print("| 12:00 PM   | Meeting with Sales Department        |")
        print("| 01:00 PM   | LUNCH BREAK                          |")
        print("| 02:00 PM   | Vendor Project Handling Meeting      |")                     
        print("| 03:00 PM   | Training and Development             |")
        print("| 04:00 PM   | Performance Review                   |")
        print("| 05:00 PM   | End of Day Wrap-up                   |")
        print("|---------------------------------------------------|")
        print("Report on the Assigned Email : Cognizant777@gmail.com")
    else:
        print("BAD LUCK :< .... HAVE TO WORK OVERTIME ")
        print()
# else:
#     print("Sorry ....No activities scheduled...")
              
    




elif(department=='Sales'):
    print("|============WELCOME TO THE SALES DEPARTMENT===============|")#fort_num=int(input("Please Enter a number to check your fortune : "))
    fort_num=int(input("Please Enter a number to check your fortune : "))
    if(fort_num<3):
        print("|---------------------------------------------------|")
        print("| Time       | Task Description                     |")
        print("|---------------------------------------------------|")
        print("| 09:00 AM   | Morning Briefing & Goal Setting      |")
        print("| 10:00 AM   | Review Sales Report                  |")
        print("| 11:00 AM   | Coffee Break                         |")
        print("| 12:00 PM   | Product Demos & Presentations        |")
        print("| 01:00 PM   | LUNCH BREAK                          |")
        print("| 02:00 PM   | Client Follow-ups                    |")                     
        print("| 03:00 PM   | Meeting with Marketing department    |")
        print("| 04:00 PM   | Staff Meeting                        |")
        print("| 05:00 PM   | End of Day Wrap-up                   |")
        print("|---------------------------------------------------|")
        print("Report on the assigned Email : Cognizant777@gmail.com")
        
   
       
    elif(fort_num<3):
        fort_num-=1
        print("|---------------------------------------------------|")
        print("| Time       | Task Description                     |")
        print("|---------------------------------------------------|")
        print("| 09:00 AM   | Morning Briefing & Goal Setting      |")
        print("| 10:00 AM   | Review Sales Report                  |")
        print("| 11:00 AM   | Coffee Break                         |")
        print("| 12:00 PM   | Product Demos & Presentations        |")
        print("| 01:00 PM   | LUNCH BREAK                          |")
        print("| 02:00 PM   | Half-Day                             |")                     
        print("| 03:00 PM   | Half-Day                             |")
        print("| 04:00 PM   | Half-Day                             |")
        print("| 05:00 PM   | Half-Day                             |")
        print("|---------------------------------------------------|")
        print("Report on the assigned Email : Cognizant777@gmail.com")
    
       
    elif(fort_num<3):
        fort_num-=1
        print("|---------------------------------------------------|")
        print("| Time       | Task Description                     |")
        print("|---------------------------------------------------|")
        print("| 09:00 AM   | Morning Briefing & Goal Setting      |")
        print("| 10:00 AM   | Product Demos & Presentations        |")
        print("| 11:00 AM   | Coffee Break                         |")
        print("| 12:00 PM   | Client Follow-ups                    |")
        print("| 01:00 PM   | LUNCH BREAK                          |")
        print("| 02:00 PM   | Review Sales Report                  |")                     
        print("| 03:00 PM   | End of Day Wrap-up                   |")
        print("| 04:00 PM   | End of Day Wrap-up                   |")
        print("| 05:00 PM   | End of Day Wrap-up                   |")
        print("|---------------------------------------------------|")
        print("Reports on the assigned Email : Cognizant777@gmail.com") 
    else:
        print("Bad Luck...... BUSY DAY ")
        
# else:
#     print("Sorry ....No activities scheduled...")        
    
    
    
elif(department=='Marketing'):
    print("|===========WELCOME TO THE MARKETING DEPARTMENT==============|")
    print()
    Fort_Num=int(input("Please Enter a number to check your fortune : "))
    print()
    if Fort_Num==fortune_number:
        print("|---------------------------------------------------|")
        print("| Time       | Task Description                     |")
        print("|---------------------------------------------------|")
        print("| 09:00 AM   | Morning Briefing & Strategy Meeting  |")
        print("| 10:00 AM   | Market Research and Analysis         |")
        print("| 11:00 AM   | AD Designing                         |")
        print("| 12:00 PM   | Meeting with HR Department           |")
        print("| 01:00 PM   | LUNCH BREAK                          |")
        print("| 02:00 PM   | Meeting with Client for Presentation |")                     
        print("| 03:00 PM   | Meeting with Marketing department    |")
        print("| 04:00 PM   | Social Medai Analyzing               |")
        print("| 05:00 PM   | End of Day Wrap-up                   |")
        print("|---------------------------------------------------|")
        print("Report on the Assigned Email : Cognizant777@gmail.com")
    else:
        print("BAD LUCK :< .... CHALLENGING SITUATION AT WORK ")
        print()
    
    
else:
    print("BAD LUCK :< ! BETTER LUCK NEXT TIME :) ")       
    
    








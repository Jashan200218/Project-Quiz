'''
Quiz Project
max - ques => 7 

1) user details :
2) age > =18 :
    proceed further 
    terms conditions (7)
    if( accept ):
      proceed futher 
            ==============================================================
                        QUIZ START MK89
            =============================================================
                1) fisrt question :
                 if ( guess == 3):
                 (score +=1)
                  next question dispplay 
                else :
                loop -> 3 chance  
                        
    else :
    exit 
    
else :
exit 

'''

game_name=input("Enter your game name : ")
name=input("Name : ")              
email=input("Email : ")
age=int(input("Age : "))


print(f"============================================================================================================================================")
print()
print(f"                                             :)  WELCOME TO THE QUIZ GAME  :)                                                          ")
print()
print(f"============================================================================================================================================")

print()
print()
print(f"==================================================== Hi! GAMER {game_name} ==========================================================================")
print()

if(age>=18):
    print("Please proceed further")
    print()
    print(f"++++++++++++++++++++++++++++++++++++++++++++++ Terms and Conditions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("Following are the Terms and Conditions :")
    print()
    print("1) You cannot leave the game in the middle.")
    print("2) You can only choose one option : option a) option b) option c) and option d). ")
    print("3) If you cannnot guess the correct answer at once then the score will not be calculated or remained same. ")
    print("4) If you cannot guess the correct answer at once then three chances will be given. ")
    print("5) If you cannot guess the correct answer in the given three chances then the game will be over.")
    # print("6) ")
    # print("7)")
    print()
    guess=input("Accept: " )
    if(guess=="yes" or guess=="Yes"):
        print("Proceed")
        print()
        print(f"=======================================================================================================================")
        print()
        print(f"                                               QUIZ START {game_name}                                      ") 
        print()
        print(f"=======================================================================================================================")
        print()
        #---------------------------------------1st question---------------------------------
        print("Que1.Who invented Computer ? ")
        print("  a) Charles Babbage              b) Issac Newton  ")
        print("  c) Thomas Edison                d) Aryabhata  ")
        print()
        
        correct_ans=input("Answer : ")
        score=0
        
        if(correct_ans == 'a'):
            score+=10
            print("Correct Answer! You've Scored a Point")
        else:
            print("Try Again")
            print()
            chance=3
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                
                if(correct_ans == 'a'):
                    print("Next question ")
                    break
                else:
                    print("Try Againn wrong !!")
                    chance-=1
        print()
        print()            
       
       
       #----------------------------------2nd question----------------------------------------             
        print("Que2.Which planet is known as the Red Planet? ")
        print("  a) Earth                 b) Mars ")
        print("  c) Jupiter               d) Saturn ")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'b'):
            score+=10
            print("Correct Answer! You've Scored a Point")
        else:
            print("Try again")
            chance=3
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'b'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn wrong !!")
                    chance-=1    
        print()
        print()
                    
        
        #---------------------------------------------3rd question--------------------------
        print("Que3. What is the largest ocean on Earth?")
        print("  a) Indian Ocean            b) Atlantic Ocean ")
        print("  c) Pacific Ocean           d) Southern Ocean ")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'c'):
            score+=10
            print("Correct Answer! You've Scored a Point")
        else:
            print("Try again")
            chance=3
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'c'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn wrong !!")
                    chance-=1
        print()
        print()            
                    
                    
        #----------------------------------4th question-------------------------------------
        print("Que4.Python is which level language ?")
        print("  a) Meduin-level           b) Low-level")
        print("  c) High-level             d) None of them ")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'c'):
            score+=10
            print("Correct Answer! You've Scored a Point")
        else:
            print("Try again")
            chance=3
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'c'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn wrong !!")
                    chance-=1
        print()
        print()            
                    
                    
                    
        #--------------------------------------5th question----------------------------------
        print("Que5.What is the national flower of Japan?")
        print("  a) Iris                       b) Lotus")
        print("  c) Cherry Blossom             d) None of them ")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'c'):
            score+=10
            print("Correct Answer! You've Scored a Point")
        else:
            print("Try again")
            chance=3
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'c'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn wrong !!")
                    chance-=1
        print()
        print()            
                    
                    
        #--------------------------------------6th question----------------------------------
        print("Que6.What is the largest animal on Earth?")
        print("  a) Elephant                   b) Lion")
        print("  c) Giraffe                    d) Blue Whale ")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'd'):
            score+=10
            print("Correct Answer! You've Scored a Point")
        else:
            print("Try again")
            chance=3
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'd'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn wrong !!")
                    chance-=1
        print()
        print()
        
        
        #------------------------------------------7th question-----------------------------------
        print("Ques7.Which company is known for creating the Macintosh line of computers?")
        print("  a) Samsung            b) HP ")
        print("  c) Dell               d) Apple ")
        print()
        correct_ans=input("Answer : ")
        
        if(correct_ans == 'd'):
            score+=10
            print("Correct Answer! You've Scored a Point")
        else:
            print("Try again")
            chance=3
            while(chance > 0):
                correct_ans=input("Answer : ")
                print()
                if(correct_ans == 'd'):
                    print("Next Question")
                    break
                else:
                    print("Try Againn wrong !!")
                    chance-=1
        print()               
        # print("Your total Score is :" , score)            
        print()
        print()
    
   
    
    else:
        print("Please Exit")
            
           
else:
    print("Sorry! Not Eligible.")

print()

print(f"-------------------------------------------------------------------------------------------------------------------------------------")
print(f"-------------------------------------------------------------------------------------------------------------------------------------")
print()      
print(f"                                                       CERTIFICATE                                                                   ")
print() 
print(f"                                                           of                                                                        ")
print()   
print(f"                                                      PARTICIPATION                                                                  ")  
# print(f"-------------------------------------------------------------------------------------------------------------------------------------")
# print(f"-------------------------------------------------------------------------------------------------------------------------------------")
print() 
print()   
print(f"                              {name} has successfully completed the QUIZ GAME, scoring {score}  points                                      ")
print()
print(f"                                            HOPE YOU HAD FUN PLAYING  !!!!                                                           ")
print()
print(f"                                                 jOIN US SOON !!!                                                                     ")
print()                                                 
print(f"                                                THANKYOU {name} :)                                                                   ")
print()
print(f"-------------------------------------------------------------------------------------------------------------------------------------")
print(f"-------------------------------------------------------------------------------------------------------------------------------------")










# print()
# print("Name        ===>     {name} ")
# print("Email       ===>     {email} ")
# print("Age         ===>     {age} ")
# print()
# print()
# print("SCORE       ===>        {score}")





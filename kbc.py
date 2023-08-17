# # kaun banega corepati
import time   #importing  time
# # taking user name from the input
# time.sleep(1)
name=input("Enter your name: ")
time.sleep(1)
print("Wlecome to the kaun banega corepati",name)

# # Topics
# print("which topic do u want to choose: ")
# time.sleep(1)                               #timedelay 1sec
Topic= ["Games", "Sports", "Technology"]
print(Topic)
time.sleep(1)
user = input("Enter the topic: ")                           #idar tak sahi bana

#take input from the user 

if(user == "Games"):
    print("We are about to start the game")
    time.sleep(1)
    print("All the best")
    time.sleep(1)
    print("1 Questions ")
    Questions = "when was temple run introduced in android"
    print(Questions)
    time.sleep(1)
    Options = ["4 Agust 2011", "october2", "may4", "july"]
    print(Options)
    time.sleep(1)
    user=input("enter the  answer: ")
    print("the answer is: ",user)
    if(user == "4 Agust 2011"):
        print("Right answer ")
    else:
        print("Wrong answer you lose the game")             #end of first questions
        time.sleep(1)
    print("Next quetions ")
    time.sleep(1)
    #2nd questions
    Questions2 = "When was free fire released "                           
    print(Questions2)
    Options1 = ["Agust 21 2017", "october4 2018","23Agust 2017", "november2022"]
    print(Options1)
    user2=input("Enter the answer: ")
    print("the answer is: ",user2)
    if(user == "23Agust 2017"):
        print("right answer ")
    else:
        print("wrong answer you lose the game")                   #end of 2nd questons
    time.sleep(1)
    # print("next questions begin here")
    time.sleep(1)
    print("next question")
    time.sleep(1)
    print("3rd question")
    q3 = "which game was launcded in india first"
    print(q3)
    o3 = ["chess", "carrom", "cards", "poker"]
    print(o3)
    user3=input("enter the  answer: ")
    print("the answer is: ",user3)
    if(user3 == "chess"):
        print("Rigt answer ")
    else:
        print("wrong answer you lose the game")                      #ed of 3d question
    time.sleep(1)
    #next questions begin here
    print("last questions")
    time.sleep(1)
    print("next question")
    q4 = "chess is also known as"
    print(q4)
    o4 = ["royal game", "branded game", "traditional game", "modern game"]
    print(o4)
    user4 = input("Enter the anser: ")
    print(user4)
    if(user4 == "royal game"):                                     #end of 4th question
        print("Right answer")
    else:
        print("wrong answer")
    q = "who is the father of the national game"
    print(q)
    an = ["Dhyan chand","denver","elliot", "tokyo"]
    print(an)
    user = input("Enter your anser: ")
    if("Dhyan chand" in an):
        print("right anser")
    else:
        print("wrong answer")                      #end of 5th question
        print("congralutions for completing the quiz") 

         # end of the questions 
elif user == "Technology":
    print("The game begin now" )
    time.sleep(1)
    print("All the best")
    time.sleep(1)
    print("first question ")
    tr = "Which one is the first  search engine in internet"
    print(tr)
    tr1 = ["Google", "archie", "altavista", "WAIS"]
    print(tr1)
    ans5 = input("enter the answer: ")
    time.sleep(1)
    if("Google" in tr1):
        print("right answer")
    else:
        print("wrong answer you lose he game")                         #1question end of programme
    print("next question")
    time.sleep(1)
    
    tr = "What is part of a database that holds only one type of information?"
    print(tr)
    tr8 = ["report", "Field", "record", "file"]
    print(tr8)
    ans = input("Enter the answer: ")
    if("Field" in tr8):
        print("right answer")
    else:
        print("Wrong answer")                      #end of 2nd programme
        time.sleep(1)
        print("next question")
        time.sleep(1)
    tr15 = "OS' computer abbreviation usually means ?"
    print(tr15)
    tr16 = ["Order of Significance", "Open Software", "operating systems", "optical sensor"]
    print(tr16)
    ans = input("Enter the answer: ")
    if("operating systems" in tr16):
        print("right answer ")
    else:
        print("wrong answer you lose he game")                        #end of 3rd programme
    tr12 = "which of the following programming language is used to create programms like appllets"
    print(tr12)
    q13 = ["COBOL","C language", "java", "BASIC"]
    print(q13)
    ans = input("Enter the answer: ")
    if("java" in q13):
        print("right answer")
    else:
        print("wrong answer")         #end of 4th question
        time.sleep(1)
        print("next question")
    tr14 = "first computer virus is known as"
    print(tr14)
    q14 = ["rabbit", "creeper virus", "elk cloner", "SCA virus"]
    print(q14)
    ans = input("Enter the answer: ")
    if("creeper virus" in q14):
        print("right answer")
    else:
        print("wrong answer")                #end of 5th question
        time.sleep(1)
        print("Congralutions you won the game")
        print("congralutions for completing the quiz") 
        

elif user == "Sports":
    print("we are about to start the sport game")
    time.sleep(1)
    print("All the best")
    time.sleep(1)
    print("1 Questions ")
    Questions1 = "Since which of the following year winter olpmpics are held ?"
    print(Questions1)
    time.sleep(1)
    Options = [1896, 1900, 1889, 1924]
    print(Options)
    time.sleep(1)
    user=input("enter your answer: ")
    if(user == "1924"):
        print("right answer ")
    else:
        print("Wrong the answer")             #end of 1st question
    time.sleep(1)
    print("next question")
# questions 
    Questions2 = " Which country won the FIFA World Cup in 2018?"
    print(Questions2)
    time.sleep(1)
    Options = [ "Brazil", "GermanyFrance" , "Spain"]
    print(Options)
    time.sleep(1)
    user=input("enter your answer: ")
    if(user == "France"):
        print("right answer ")
    else:
        print("Wrong answer")          #end of 2nd question
    Questions3 = "  Who won the Wimbledon Women’s Singles title in 2021?"
    print(Questions3)
    time.sleep(1)
    Options = [ "Serena William","Simona Halep",  "Ashleigh BartyNaomi",  "namoiOsaka"]
    print(Options)
    time.sleep(1)
    user=input("enter your answer: ")
    if(user == "Ashleigh BartyNaomi"):
        print("right answer ")
    else:
        print("Wrong the answer")                  #end of 3rd question

# next questons
    time.sleep(1)
    print("next question")
    Questions4 = " Who holds the record for the most Grand Slam titles in mens tennis?"
    print(Questions4)
    time.sleep(1)
    Options = ["Roger Federer", "Rafael Nadal", "Novak Djokovic" , "Pete Sampras"]
    print(Options)
    time.sleep(1)
    user=input("enter your answer: ")
    if(user == "Roger Federer"):
        print("right answer ")
    else:
        print("Wrong the answer")          #end of 4th question
    Questions5 = " Which country has won the most Olympic gold medals?"
    print(Questions5)
    time.sleep(1)
    Options = ["United States","China","Russia","Germany"]
    print(Options)
    time.sleep(1)
    user=input("enter your answer: ")
    if(user == "United States"):
        print("right answer and you won $1000")
    else:
        print("you lose the game")       #end of 5th question
        print("congralutions for completing the quiz") 


    # elif user == "Basic python":          #working on it it will be available soon.......

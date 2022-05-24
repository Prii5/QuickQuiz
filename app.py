print ("""Welcome to the quiz users!  
Pull up your sleeves and hold back. \n\n""")

a = str(input("Would you like to be the part of the game:(yes/no):"))

if a.lower() != "yes":
    quit()
else:
    print ("Okay! Lets get going")
    
score = 0
    
first_que = input("what does the CPU stand for? ").lower()
if first_que == "central processing unit":
    print ("You got your answer correct")
    score += 1
else:
    print("incorrect")
    
print('\n')
    
second_que = input("what does the GPU stand for? ")
if second_que.lower() == "graphics processing unit":
    print ("You got your answer correct")
    score += 1
else:
    print("incorrect")

print('\n')
    
third_que = input("what does the RAM stand for? ")
if third_que.lower() == "random accesing unit":
    print ("You got your answer correct")
    score +=1
else:
    print("incorrect")
    
    
fourth_que = input("what does the PSU stand for? ")
if fourth_que.lower() == "power supply unit":
    print ("You got your answer correct")
    score +=1
else:
    print("incorrect")
    
print("The total score is: " + str(score))
print("The percentage is: " + str((score/4)*100) + "%")
    
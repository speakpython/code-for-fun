day = 0 # birth day to be determined 

# Prompt the user to answer the first question
question1 = \
"""
Is your birthday in Set1

  1  3  5  7
  9 11 13 15
 17 19 21 23
 25 27 29 31

 Enter 0 for No and 1 for Yes: 
""" 
answer = eval(input(question1 + ' >> '))

if answer == 1:
    day += 1
    
# Prompt the user to answer the second question
question2 = \
"""
Is your birthday in Set2

  2  3  6  7
 10 11 14 15
 18 19 22 23
 26 27 30 31

 Enter 0 for No and 1 for Yes:
""" 
answer2 = eval(input(question2 + ' >> '))

if answer2 == 1:
    day += 2

#Prompt the user to answer the third question
question3 = \
"""
 Is your birthday in Set3
 
 4  5  6  7
 12 13 14 15
 20 21 22 23
 28 29 30 31

 Enter 0 for No and 1 for Yes: 
"""
answer3 = eval(input(question3 + ' >> '))

if answer3 == 1:
    day += 4
    
#Prompt the user to answer the fourth question
question4 = \
"""
 Is your birthday in Set4
 
 8  9  10 11
 12 13 14 15
 24 25 26 27
 28 29 30 31
 
 Enter 0 for No and 1 for Yes: 
"""
answer4 = eval(input(question4 + ' >> '))

if answer4 == 1:
    day += 8
    
#Prompt the user to answer the last question
question5 = \
"""
Is your birthday in Set5

 16 17 18 19
 20 21 22 23
 24 25 26 27
 28 29 30 31
 
 Enter 0 for No and 1 for Yes: 
"""
answer5 = eval(input(question5 + ' >> '))

if answer5 == 1:
    day += 16
print("*"*24)
print("Your birthday is on " + str(day) + "!") #displayng result!
print("*"*24)
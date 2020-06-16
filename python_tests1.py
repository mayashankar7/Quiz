print(" \t  Welcome to Quiz World")
print("Before you start this wonderful game , we recomonds yous to please create your username")
username = input("Enter your username here")
password = input("Enter your password here")
print("Thanks for joining us. \n\t Lets play !")
question_1 =  "Question 1 .- Number of alphabets english have \n Choices:- \n (1) 25 \n (2) 23 \n (3) 24 \n (4) 26"
print(question_1)
true_answer1 = 25
answer1 = int(input("Your Answer of 1"))
question_2 = "Question 2.- Programming Language taught in first semester \n Choices:- \n (1) C \n (2) R \n (3) Python \n (4) Java"
if answer1 == true_answer1:
    print("That's Right! \n ",question_2)
else:
    print("Try again please \n", question_1 , "\n")
    print(input("Enter your answer of 1"))
true_answer2 = "C"
answer2 = input("Your answer of 2")
question_3 = "Question 3.- Who discovered India ? \n Choices:- \n (1) Vasco De Gama \n (2) Columbus \n (3) Williams Amazon \n (4) Mahatma Gandhi"
if answer2 == true_answer2:
    print("That's Right! \n",question_3)
else:
    print("Try again please\n",question_2)
true_answer3 = "Vasco De Gama"
answer3 = input("Your answer of 3")
if answer3 == true_answer3:
    print("You Played Well")
else:
    print("Try again please",question_3)
print("Happy Happy!")




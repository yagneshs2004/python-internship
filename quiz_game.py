import time
import random


print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
qn = 4
i=0
ques_ans = {'What is the capital of India?': 'new delhi', " Which planet is known as the Red Planet?": "mars",
        " What is the largest mammal in the world?": 'whale', "How many continents are there in the world?":'7'}
ques_choice = {'What is the capital of India?': 0, " Which planet is known as the Red Planet?": 1,
        " What is the largest mammal in the world?": 2, "How many continents are there in the world?":3}

choices=[['new delhi','tamil nadu','karnataka','andhra pradesh'],['earth','mars','venus','saturn'],['lion','whale','bat','human'],[2,5,6,7]]
feedback={'What is the capital of India?': 'Located in Center of India, New Delhi', " Which planet is known as the Red Planet?": "4th Planet In Our Solar System, Mars",
        " What is the largest mammal in the world?": 'A Huge Fish In The Sea, Blue Whale', "How many continents are there in the world?": '4th Prime Number, 7'}
dup=ques_ans
playing = input('Do you want to play ? ').lower()
if playing == 'yes' or playing == 'sure':
    while i<qn:
        print()
        if i ==0:
            print("Get Ready For Your First Question")
            time.sleep(1)
        elif i<qn-1:
            print("Get Ready For Your Next Question...")
            time.sleep(1)
        else:
            print("The Final Question Of This Quiz is...")
            time.sleep(1)
        print(f"Question {i+1}:\n")
        a=random.choice(list(dup.keys()))
        print(a,'\n')
        b=ques_choice[a]
        for k in choices[b]:
            print(k,end='\n')
        ans=input("Enter your Answer: ")
        if ans == ques_ans[a]:
            score+=1
            print("**CONGRATULATIONS**")
            print("Correct answer, u earned 1 mark. current score = ",score)
        else:
            print("Its not right, The Right Answer is,:- ",feedback[a])
            print()
            print("Current Score = ",score)
        time.sleep(0.8)

        time.sleep(1.5)


        dup.pop(a)
        i+=1
print("Thank You For Participating In The Quiz, Your Score is : ",score)


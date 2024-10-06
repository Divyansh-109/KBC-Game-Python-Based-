import random 

def get_name(): 
    # Get the user's Name
    name= input("Enter your name: ")
    return name

def rules():
    #Some Basic Rules
    print('''\nRead the following Instructions carefully:
    1. There will be 10 Questions.
    2. Each Correct Answer will lead you win a amount.
    3. If you give a Wrong Answer then the game will end and the prize will be according to the milestone reached by you. 
    4. There are Two lifelines (Audience Poll and 50-50) that can be used only once. 
    5. You have to answer in format of (1,2,3,4) or type "AP" for Audience Poll, "FF" for 50-50, or "quit" to exit. ''')
    
def user_agree():
    #User Agree to the rules
    while True:
        try:
            agree= input("Do you agree with the rules? (yes/no): ")
            if agree.lower() == "yes":
                return("\nLet's start the game"),True
            elif agree.lower() == "no":
                return("You didn't agree with the rules, so you can't play the game"),False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        except ValueError:
            print("An error occurred:", ValueError)

def get_question(question):
    #Display the question
    print("\nQuestion: ", question["question"])
    for i in range(len(question["options"])):
        value=question["options"]
        print(value[i])

def get_answer():
    #Get the user's answer
    while True:
        answer = input("Enter your answer (1,2,3,4), 'AP' for Audience Poll, 'FF' for 50-50, or 'quit' to quit: ")
        if answer.lower() == "quit": #To Quit the game
            return "quit"
        if answer.upper() in ["AP", "FF"]: #For Lifelines
            return answer.upper()
        try:
            answer = int(answer)
            if answer in [1,2,3,4]:
                return answer
            else:
                print("Invalid input. Please enter a number between 1 and 4, or type 'AP', 'FF', or 'quit'.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4, or type 'AP', 'FF', or 'quit'.")

def check_answer(question, answer):
    #Check the user's answer
        if answer == question["answer"]:
            return True
        else:
            return False
    
def display_prize(final_amount):
    #Display the prize
    print("\nYou won: Rs.", final_amount)

def audience_poll(question):
    #Audience Poll Lifeline
    answers=[0, 0, 0, 0]
    for _ in range(100):
        answers[random.randint(0,3)]+=1
    answers[question["answer"]-1] +=20 #To Increase the chances of correct answer
    return answers

def fifty_fifty(question):
    #Fifty Fifty Lifeline
    answers = [i for i in range(1, 5) if i!= question["answer"]]
    return random.sample(answers, 2)

def game():
    # Game Logic
    name = get_name()
    print(f"Welcome {name}, to Kaun  Banega Crorepati.!")
    rules()
    if not user_agree():
        print("You didn't agree to the rules. Game Over!")
        return

    #Initializing the amount
    final_amount=0

    #Use of Nested List for  storing questions, options and answers
    questions = [
    {"question": "Who developed Python Programming Language?", "options":["1. Wick Van Rossum", "2. Rasmus Lerdof", "3. Guido Van Rossum", "4. Niene Stom"], "answer":3},
    
    {"question": "Which type of programming does Python support?", "options":["1. Object-oriented", "2. Structured", "3. Functional", "4. All of the above"], "answer":4},
    
    {"question":"What will be the value of the following Python expression (4 + 3 % 5)?", "options":["1. 7", "2. 4", "3. 2", "4. 1"], "answer":1},
    
    {"question":"Which of the following is used to define a block of code in Python?", "options":["1. Key", "2. Indentation", "3. Brackets", "4. All of these"], "answer":2},
    
    {"question":"Which keyword is used for functions in Python?", "options":["1. Function", "2. def", "3. func", "4. Define"], "answer":2},
    
    {"question":"What will be the output of this python code:\n i=1\n while True:\n    if i%3==0:\n    break;\n    print(i)\n    i+=1", "options":["1. 1 2 3", "2. error", "3. 1 2", "4. none of the above"], "answer":3},
    
    {"question":"which of the following functions can help us to find the version of python we are currently working on?", "options":["1. sys.version(1)", "2. sys.version(0)", "3. sys.version()", "4. sys.version"], "answer":4},
    
    {"question":"Python supports the creation of anonymous function at runtime,using a construct called,______", "options":["1. pi", "2. anonymous" ,"3. lambda", "4.none of the above"], "answer":3},
    
    {"question":"What will be the output of the following python function?\n min(max(False, -3, -4), 2, 7)", "options":["1. -4", "2. -3", "3. 2", "4. False"], "answer":4},
    
    {"question":"How to call constructor in Python Classes?", "options":["1. __main__", "2. __init__", "3. def", "4. constructor"], "answer":2}
    ]

    prize=[10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 10000000]
    lifelines= ["Audience Poll", "50-50"]

    used_audience_poll= False
    used_fifty_fifty=False

    #Use of Loops to iterate over the questions
    for i, question in  enumerate(questions):
        get_question(question)
        while True:
            answer = get_answer()
            if answer == "quit":
                print(f"You quit the game. Your final winning amount is: Rs. {final_amount}")
                return
            
            elif answer is None: 
                print(f"You quit the game. Your final winning amount is: Rs. {final_amount}")
                return

            # Lifelines handling
            if answer == "AP":
                if not used_audience_poll:
                    answers = audience_poll(question)
                    print(f"Audience Poll Results: {answers}")
                    used_audience_poll = True
                    continue  # Go back to the question after using the lifeline
            
            elif answer == "FF":
                if not used_fifty_fifty:
                    answers = fifty_fifty(question)
                    print("Two wrong Options are: ", answers)
                    used_fifty_fifty = True
                    continue  # Go back to the question after using the lifeline
            
            #Check The answer
            if check_answer(question,answer):
                final_amount= prize[i]
                print(f"Correct answer! You won Rs. {final_amount}")
                if i==3:
                    print("Congratulations!! You have reached the first milestone of 80,000.")
                elif i==7:
                    print("Congratulations!! You have reached the second milestone of 12,50,000.")
                break
            else:
                # If the lifeline was used, inform the user
                if used_audience_poll or used_fifty_fifty:
                    print("Incorrect answer. You have used a lifeline. Please try again.")
                    continue  # Allow the user to try again without ending the game
                else:
                    # Show milestone prize for incorrect answer
                    if i < 3:
                        print("Incorrect answer. You won Rs. 0. Game Over!")
                        final_amount = 0
                    elif i < 7:
                        print("Incorrect answer. You won Rs. 80,000. Game Over!")
                        final_amount = 80000
                    else:
                        print("Incorrect answer. You won Rs. 12,50,000. Game Over!")
                        final_amount = 1250000
                
                    display_prize(final_amount)
                    return
    print(f"Congratulations! You won the game with a prize of: Rs. {final_amount}")

game()

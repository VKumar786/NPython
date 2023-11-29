'''
    TODO: Exercise 3: Kaun Banega Crorepati (KBC) | Python Tutorial - Day #27 
'''

data = [
    {
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Seoul", "Beijing", "Bangkok"],
        "answer": "Tokyo"
    },
    {
        "question": "Which programming language is known for its simplicity and readability?",
        "options": ["Java", "Python", "C++", "JavaScript"],
        "answer": "Python"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "In which year did the World War II end?",
        "options": ["1943", "1945", "1950", "1939"],
        "answer": "1945"
    }
]

money = 0

for i, obj in enumerate(data):
    print("Question >> ", obj["question"])
    print("Options are :-")
    for idx, option in enumerate(obj["options"]):
        print(f"{idx+1} {option}".center(35))

    ans = int(input("Please select an answer by entering a number from 1 to 4 :: "))

    idx = obj["options"].index(obj["answer"]) + 1

    if (idx == ans):
        print(
            f"Congratulations! That's the correct answer!\nYou've won ${10**i}!")
        money += 10**i
    else:
        print("Sorry, that's not the correct answer. Better luck next time.")

print(f"Total Amount won :: $", money)

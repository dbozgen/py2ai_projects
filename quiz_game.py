score = 0
questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 7 + 8?", "answer": "15"},
    {"question": "What color do you get when you mix blue and yellow?", "answer": "green"},
    {"question": "How many days are in a week?", "answer": "7"},
    {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
    {"question": "What is 5 x 6?", "answer": "30"},
    {"question": "What animal says 'meow'?", "answer": "cat"},
    {"question": "How many legs does a spider have?", "answer": "8"},
    {"question": "What is the capital of Japan?", "answer": "tokyo"},
    {"question": "What is 12 - 4?", "answer": "8"}
]

for q in questions:
    user_answer = input(q["question"] + " ").strip().lower()
    if user_answer == q["answer"]:
        print ("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")
print(f"Your final score is {score} out of {len(questions)}.")




# Dictionary Practice: RPG Game Charactersx

hero_1 = {
    "name": "Aragorn",
    "class": "Ranger",
    "level": 20,
    "abilities": ["Tracking", "Swordsmanship", "Leadership"],
    "health": 150,
}

hero_2 = {
    "name": "Gandalf",
    "class": "Wizard",
    "level": 30,
    "abilities": ["Magic", "Wisdom", "Fireworks"],
    "health": 100,
}

hero_3 = {
    "name": "Legolas",
    "class": "Archer",
    "level": 18,
    "abilities": ["Archery", "Agility", "Keen Sight"],
    "health": 120,
}

hero_4 = {
    "name": "Gimli",
    "class": "Warrior",
    "level": 17,
    "abilities": ["Axe Mastery", "Endurance", "Smithing"],
    "health": 160,
}

print (hero_1["abilities"][1])  # Output: Swordsmanship
print (hero_2["level"])          # Output: 30
print (hero_3["name"])           # Output: Legolas


heroes = [hero_1, hero_2, hero_3, hero_4]

hero_1["health"] -= 20  # Aragorn takes damage
hero_1["potion"] = 2   # Aragorn acquires potions

print (f"{hero_1['name']}'s health: {hero_1['health']}")  # Output: 130


#

quiz = {
    "Q1": {
        "question": "What is 3 + 5?",
        "answer": "8",
    },
    "Q2": {
        "question": "What is the capital of France?",
        "answer": "Paris",
    },
    "Q3": {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter",
    },
}

user_answer = input (quiz["Q2"]["question"] + " ")

if user_answer.strip().lower() == quiz["Q2"]["answer"].lower():
    print ("Correct!")
else:
    print ("Incorrect. The correct answer is " + quiz["Q2"]["answer"] + ".")
    

for quiz_id, quiz_data in quiz.items():
    print(f"Q: {quiz_data['question']}")
    print(f"A: {quiz_data['answer']}")
    print()  # blank line for readabilityB
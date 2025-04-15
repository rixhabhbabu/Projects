
# Simple Python Quiz App

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q['question'])
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}")
    print(f"\n🎯 Your final score: {score}/{len(questions)}")

# Questions List
quiz_questions = [
    {
        "question": "1. What is the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
        "answer": "B"
    },
    {
        "question": "2. What does 'len()' function do in Python?",
        "options": ["A. Adds numbers", "B. Prints output", "C. Returns length", "D. Converts string to int"],
        "answer": "C"
    },
    {
        "question": "3. Which keyword is used to define a function in Python?",
        "options": ["A. def", "B. func", "C. define", "D. function"],
        "answer": "A"
    },
    {
        "question": "4. Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "5. What is the correct file extension for Python files?",
        "options": ["A. .pt", "B. .pyt", "C. .py", "D. .p"],
        "answer": "C"
    }
]

# Run the Quiz
run_quiz(quiz_questions)

# python.py

questions = [
    {
        "question": "1. Python kis type ki language hai?",
        "options": [
            "A) Programming Language",
            "B) Database",
            "C) Operating System",
            "D) Browser"
        ],
        "answer": "A"
    },
    {
        "question": "2. Django kis language ka framework hai?",
        "options": [
            "A) Java",
            "B) Python",
            "C) C++",
            "D) PHP"
        ],
        "answer": "B"
    },
    {
        "question": "3. SQL ka use kis liye hota hai?",
        "options": [
            "A) Database management",
            "B) Image editing",
            "C) Gaming",
            "D) Networking"
        ],
        "answer": "A"
    }
]


score = 0
submissions = []


print("===== Python Quiz System =====\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Apna answer submit karein (A/B/C/D): ").upper()

    submissions.append(user_answer)

    if user_answer == q["answer"]:
        print("✅ Correct Answer\n")
        score += 1
    else:
        print("❌ Wrong Answer")
        print("Correct Answer:", q["answer"], "\n")


print("============================")
print("Quiz Completed")
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Your Score:", score, "/", len(questions))


print("\nSubmitted Answers:")
for i, ans in enumerate(submissions):
    print(f"Question {i+1}: {ans}")

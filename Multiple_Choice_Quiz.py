from Question import Question

question_prompts = [
    "What data structure should be used when number of elements is fixed?\n(a) Array\n(b) Array List\n(c) Vector\n(d) Set\n\nYour answer:",
    "What causes the program to exit abruptly and hence its usage should be minimalistic?\n(a) Try\n(b) Finally\n(c) Exit\n(d) Catch\n\nYour answer:",
    "Which of the following is a best practice to measure time taken by a process for execution?\n(a) System.currentTimeMillis()\n(b) System.nanoTime()\n(c) System.getCurrentTime()\n(d) System.getProcessingTime()\n\nYour answer:",   
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got ", str(score), "out of", str(len(questions)))

run_quiz(questions)
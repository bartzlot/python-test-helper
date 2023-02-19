#! /usr/bin/env python
"""Dummy docstring."""
from test_modules import checking_answers, picking_random_elements, saving_into_file, adding_new_questions

questions = ["Ile to 2+2: ", "Jaka jest wartość liczby Pi: ", "Czy słoń to ssak: "]
answers = [
    ["3", "4", "1", "5"],
    ["3.14", "2", "4.5", "1.73"],
    ["nie", "tak", "nie wiem", "moze"],
]
correctAnswers = ["4", "3.14", "tak"]
PROGRAM_RUNNING = True
saving_into_file(questions, answers, correctAnswers)
adding_new_questions(questions, answers, correctAnswers)


# todo - while PROGRAM_RUNNING is True:
while True:
    try:
        questionsAmount = int(input("Ile pytań ma zawierać quiz: "))
        if questionsAmount > len(questions) or questionsAmount <= 0:
            print("Podaj liczbę z zakresu 1-{}".format(len(questions)))
            continue
        else:
            break
    except ValueError:
        print("Proszę podać liczbę!")
        continue
randomQuestions = picking_random_elements(questions, questionsAmount)
randomAnswers = []
for i in randomQuestions:
    randomAnswers.append(picking_random_elements(answers[i], len(answers[i])))
print(randomAnswers)
print(randomQuestions)
POINTS = 0
ITR = 0
for i in randomQuestions:
    print("\n")
    print(questions[i])
    ABCD = 65
    ANSWER = ""
    for j in randomAnswers[ITR]:
        letter = chr(ABCD)
        if correctAnswers[randomQuestions[ITR]] == answers[i][j]:
            CORRECT_ANSWER = letter
        ABCD += 1
        print("{}: {}".format(letter, answers[i][j]), end=" | ")
    print("\n")
    ITR += 1
    ANSWER = str(input("Podaj odpowiedź: "))
    if checking_answers(ANSWER, CORRECT_ANSWER) is True:
        POINTS += 1
print(
    "Twój wynik: {}/{} - {}%".format(
        POINTS, questionsAmount, round((POINTS / questionsAmount) * 100, 2)
    )
)

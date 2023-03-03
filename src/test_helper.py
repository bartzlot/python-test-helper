#! /usr/bin/env python
"""Dummy docstring."""
from test_modules import (
    adding_new_questions,
    checking_answers,
    curses,
    main_menu,
    picking_random_elements,
    reading_from_file,
    reading_points_from_file,
    saving_into_file,
    saving_points_to_file,
)

QUESTIONS = []
ANSWERS = []
CORRECT_ANSWERS = []
points = []
# stdscr = curses.initscr()
# curses.wrapper(main_menu)
reading_from_file(QUESTIONS, ANSWERS, CORRECT_ANSWERS)
# adding_new_questions(QUESTIONS, ANSWERS, CORRECT_ANSWERS)
# saving_into_file(QUESTIONS, ANSWERS, CORRECT_ANSWERS)

# todo - while PROGRAM_RUNNING is True:
while True:
    try:
        questions_amount = int(input("Ile pytań ma zawierać quiz: "))
        if questions_amount > len(QUESTIONS) or questions_amount <= 0:
            print("Podaj liczbę z zakresu 1-{}".format(len(QUESTIONS)))
            continue
        else:
            break
    except ValueError:
        print("Proszę podać liczbę!")
        continue
randomQuestions = picking_random_elements(QUESTIONS, questions_amount)
randomAnswers = []
for i in randomQuestions:
    randomAnswers.append(picking_random_elements(ANSWERS[i], len(ANSWERS[i])))
POINTS = 0
ITR = 0
for i in randomQuestions:
    print("\n")
    print(QUESTIONS[i])
    ABCD = 65
    ANSWER = ""
    for j in randomAnswers[ITR]:
        letter = chr(ABCD)
        if CORRECT_ANSWERS[randomQuestions[ITR]] == ANSWERS[i][j]:
            CORRECT_ANSWER = letter
        ABCD += 1
        print("{}: {}".format(letter, ANSWERS[i][j]), end=" | ")
    print("\n")
    ITR += 1
    ANSWER = str(input("Podaj odpowiedź: "))
    if checking_answers(ANSWER, CORRECT_ANSWER) is True:
        POINTS += 1
points.append("{}/{}".format(POINTS, questions_amount))
print(
    "Twój wynik: {}/{} - {}%".format(
        POINTS, questions_amount, round((POINTS / questions_amount) * 100, 2)
    )
)
saving_points_to_file(points, 10)

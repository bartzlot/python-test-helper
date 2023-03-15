from .test_modules import (
    picking_random_elements,
    checking_answers,
    saving_into_file,
    reading_from_file,
    adding_new_questions,
    saving_points_to_file,
    reading_points_from_file,
)

def quiz_game(questions_amount: int):
    QUESTIONS = []
    ANSWERS = []
    CORRECT_ANSWERS = []
    points = []
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

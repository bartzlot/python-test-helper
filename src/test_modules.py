"""Dummy docstring."""
import random


def picking_random_elements(elements: list, list_amount: int):
    """Picks random values from list without repetitions
    Args:
    list: list of elements
    list_amount: amount of random picked elements
    """
    random_numbers = range(0, len(elements))
    random_elements = random.sample(random_numbers, list_amount)
    return random_elements


def checking_answers(answer: str, correct_answer: str):
    """Checks if given answer is correct with const (works for upper and lower
    letters)
        Args:
        answer: given answer
        correct_answer: correct uppercase answer
    """
    if answer.upper() == correct_answer:
        print("POPRAWNA ODPOWIEDŹ")
        return True
    else:
        print("NIEPOPRAWNA ODPOWIEDŹ")
        return False


def saving_into_file(questions: list, answers: list, correct_answers: list):
    """Save elements from 3 given lists into file with ';' suffix after values
    Args:
    questions: list of questions
    answers: list of answers
    correct_answers: list of correct answers associated with questions
    """
    with open("questions.txt", "w") as f:
        for i in range(len(questions)):
            f.write(
                "{};{};{}\n".format(
                    questions[i], ";".join(answers[i]), correct_answers[i]
                )
            )


def adding_new_questions(questions: list, answers: list, correct_answers: list):
    """Function adding new questions from user while whole program is running

    Args:
        questions (list): list of questions
        answers (list): list of answers
        correct_answers (list): list of correct answers
    """
    while True:
        pick = str(input("Jezeli nie chcesz wprowadzać nowego pytania wpisz [N]: "))
        if pick == "N" or pick.upper() == "N":
            break
        else:
            question = str(input("Podaj pytanie jakie chcesz dodać: "))
        if question == "" or question.isnumeric() is True:
            print("Musisz podać pytanie...\n")
            continue
        else:
            break
    temp_answers = []
    itr = 1
    while itr <= 4:
        single_answer = str(input("Podaj {} odpowiedź: ".format(itr)))
        if single_answer == "":
            print("Musisz wymyślić jakąś odpowiedź...")
            continue
        else:
            itr += 1
            temp_answers.append(single_answer)
    options = ["A", "B", "C", "D"]
    while True:
        print("Wskaz poprawną odpowiedź spośród - ", end="")
        print(
            "A: {}|B: {}|C: {}|D: {}: ".format(
                temp_answers[0], temp_answers[1], temp_answers[2], temp_answers[3]
            ),
            end="",
        )
        temp_correct_answer = str(input())
        if temp_correct_answer.upper() not in options:
            print("Musisz wskazać, którąś z podanych...")
            continue
        else:
            temp_correct_answer = temp_answers[
                options.index(temp_correct_answer.upper())
            ]
            print(temp_correct_answer)
            break
    questions.append(question)
    answers.append(temp_answers)
    correct_answers.append(temp_correct_answer)

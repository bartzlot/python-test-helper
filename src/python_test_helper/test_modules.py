"""Dummy docstring."""
import curses
import json
import os
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


def checking_answers(answers: list, correct_answers: list):
    """Checks if given answer is correct with const (works for upper and lower
    letters)
        Args:
        answer: given answer
        correct_answer: correct uppercase answer
    """
    temp_check = []
    for index, i in enumerate(correct_answers):
        if i["state"]:
            temp_check.append(index)
    return set(answers) == set(temp_check)


def saving_into_file(test: dict, path: str):
    """Save elements from 3 given lists into file with ';' suffix after values
    Args:
    questions: list of questions
    answers: list of answers
    correct_answers: list of correct answers associated with questions
    """
    with open(path, "w", encoding="utf-8") as file:
        json.dump(test, file)


def reading_from_file(path: str):
    """FIX ME."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def define_correctness():
    """dummy doc"""
    while True:
        is_correct_input = str(input("Czy odpowiedź jest poprawna[T/N]: "))

        if is_correct_input.upper() == "T":
            return True

        if is_correct_input.upper() == "N":
            return False

        print("Musisz wskazać poprawność odpowiedzi...")
        continue


def adding_new_questions():
    """Function adding new questions from user while whole program is running"""
    questions = []

    while True:
        question = str(input("Podaj pytanie jakie chcesz dodać lub wpisz [N], aby zakończyć wprowadzanie: "))

        if question.upper() == "N":
            break

        if question == "" or question.isnumeric() is True:
            print("Musisz podać pytanie...\n")
            continue

        temp_answers = []
        itr = 1

        while True:
            single_answer = str(input(f"Podaj {itr} odpowiedź lub wpisz [N], aby zakończyć dodawanie: "))

            if single_answer == "":
                print("Musisz wymyślić jakąś odpowiedź...")
                continue

            if single_answer.upper() == "N":
                break

            packed_answer = {
                "answer": single_answer,
                "is_correct": define_correctness(),
            }
            temp_answers.append(packed_answer)
            itr += 1

        questions.append({"question": question, "answers": temp_answers})

    return questions


def saving_points_to_file(points: list, records_amount: int):
    """FIX ME."""
    with open("points.txt", "w", encoding="utf-8") as file:
        for itr, i in enumerate(points):
            file.write(i + "\n")
            if itr > records_amount:
                break


def reading_points_from_file(points: list):
    """FIX ME."""
    try:
        with open("points.txt", "r", encoding="utf-8") as file:
            for line in file:
                points.append(line.strip())
    except IOError:
        print("Nie mozna otworzyć pliku, sprawdź czy znajduje się w odpowiedniej ściezce...")
    except EOFError:
        print("Plik jest pusty, nie mozna odczytać punktów...")
    except IndexError:
        print("Plik z pytaniami zawiera dane w złym formacie...")
        print("Poprawny format:")
        print("[punkty]/[ilość pytań]")


menu_options = ["Rozpocznij quiz", "Ostatnie wyniki", "Zamknij program"]


def main_menu(stdscr):
    """FIX ME."""
    attributes = {}
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes["normal"] = curses.color_pair(1)
    attributes["highlighted"] = curses.color_pair(2)
    key = 0
    option = 0
    while key != 10:
        stdscr.erase()
        stdscr.addstr("MENU GŁOWNE\n", curses.A_UNDERLINE)
        for i, _ in enumerate(menu_options):
            if i == option:
                attr = attributes["highlighted"]
            else:
                attr = attributes["normal"]
            stdscr.addstr(f'{i + 1}')
            stdscr.addstr(menu_options[i] + "\n", attr)
        key = stdscr.getch()
        if key == curses.KEY_UP and option > 0:
            option -= 1
        elif key == curses.KEY_DOWN and option < len(menu_options) - 1:
            option += 1
    stdscr.addstr(f"Wybrałeś {menu_options[option]}")
    stdscr.getch()


def quiz_game(questions_amount: int):
    """FIX ME."""
    questions: list[str] = []
    answers: list[list[str]] = []
    correct_answers: list[list[str]] = []
    points = []
    random_questions = picking_random_elements(questions, questions_amount)
    random_answers = []
    for i in random_questions:
        random_answers.append(picking_random_elements(answers[i], len(answers[i])))
    points_counter = 0
    itr = 0
    for i in random_questions:
        print("\n")
        print(questions[i])
        abcd = 65
        answer = ""
        for j in random_answers[itr]:
            letter = chr(abcd)
            if correct_answers[random_questions[itr]] == answers[i][j]:
                correct_answer = letter
            abcd += 1
            print(f'{letter}: {answers[i][j]}', end=" | ")
        print("\n")
        itr += 1
        answer = str(input("Podaj odpowiedź: "))
        if checking_answers([answer], [correct_answer]) is True:
            points_counter += 1
    points.append(f'{points_counter}/{questions_amount}')
    print(f'Twój wynik: {points_counter}/{questions_amount} - {round((points_counter / questions_amount) * 100, 2)}%')
    saving_points_to_file(points, 10)


def create_new_test(path: str):
    """FIX"""
    if os.path.exists(path):
        test = reading_from_file(path)
    else:
        test = get_test_info()

    test["questions"] += adding_new_questions()
    saving_into_file(test, path)


def get_test_info():
    """Get basic test information

    Returns:
        _type_: _description_
    """
    return {"title": "FIX ME", "description": "FIX ME", "questions": []}

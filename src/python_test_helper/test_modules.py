"""Dummy docstring."""
import curses
import random
import json
import os


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
        if i['state']:
            temp_check.append(index)
    if set(answers) == set(temp_check):
        return True
    else:
        return False


def saving_into_file(questions: list, answers: list):
    """Save elements from 3 given lists into file with ';' suffix after values
    Args:
    questions: list of questions
    answers: list of answers
    correct_answers: list of correct answers associated with questions
    """
    dump_list = []
    with open("questions.json", "w") as f:
        for itr, i in enumerate(questions):
            dump_dict = {
                'question': i,
                'answers': answers[itr],
            }
            dump_list.append(dump_dict)
        json.dump(dump_list, f, indent=2)


def reading_from_file(questions: list, answers: list):
    """Reading elements from file 'questions.txt'

    Args:
        questions (list): questions list
        answers (list): answers list
        correct_answers (list): correct answers list
    """
    try:
        with open("questions.json", "r") as f:
            questions_data = json.load(f)

    except IOError:
        print(
            "Nie mozna otworzyć pliku, sprawdź czy znajduje się w odpowiedniej ściezce..."
        )
    try:
        for i in questions_data:
            questions.append(i['question'])
            answers.append(i['answers'])
    except EOFError:
        print("Plik jest pusty, nie mozna odczytać pytań...")
    except IndexError:
        print("Plik z pytaniami zawiera dane w złym formacie...")
        print("Poprawny format:")
        print("[pytanie] ;[odp1] ;[odp2];[odp3] ;[odp-N] ;[poprawna odp]")


def define_correctness(is_correct: bool):
    """dummy doc"""
    while True:
            c = str(input("Czy odpowiedź jest poprawna[T/N]: "))
            if c.upper() == 'T':
                return True
            elif c.upper() == 'N':
                return False
            else:
                print('Musisz wskazać poprawność odpowiedzi...')
                continue


def adding_new_questions(questions: list, answers: list):
    """Function adding new questions from user while whole program is running

    Args:
        questions (list): list of questions
        answers (list): list of answers with correctness state
    """
    while True:
        question = str(input("Podaj pytanie jakie chcesz dodać lub wpisz [N], aby zakończyć wprowadzanie: "))
        if question.upper() == "N":
            break
        elif question == "" or question.isnumeric() is True:
            print("Musisz podać pytanie...\n")
            continue
        else:
            break
    temp_answers = []
    itr = 1
    # options = []
    while True:
        single_answer = str(
            input(
                "Podaj {} odpowiedź lub wpisz [N], aby zakończyć dodawanie: ".format(
                    itr
                )
            )
        )
        if single_answer == "":
            print("Musisz wymyślić jakąś odpowiedź...")
            continue
        elif single_answer.upper() == "N":
            break
        else:
            itr += 1
            packed_answer = {}
            is_correct = None
            is_correct = define_correctness(is_correct)
            packed_answer = dict(answer=single_answer, state=is_correct)
            temp_answers.append(packed_answer)
    questions.append(question)
    answers.append(temp_answers)
    print(answers)

def saving_points_to_file(points: list, records_amount: int):
    with open("points.txt", "w") as f:
        for itr, i in enumerate(points):
            f.write(i + "\n")
            if itr > records_amount:
                break


def reading_points_from_file(points: list, records_amount: int):
    try:
        f = open("points.txt", "r")
    except IOError:
        print(
            "Nie mozna otworzyć pliku, sprawdź czy znajduje się w odpowiedniej ściezce..."
        )
    try:
        for line in f:
            points.append(line.strip())
    except EOFError:
        print("Plik jest pusty, nie mozna odczytać punktów...")
    except IndexError:
        print("Plik z pytaniami zawiera dane w złym formacie...")
        print("Poprawny format:")
        print("[punkty]/[ilość pytań]")


menu_options = ["Rozpocznij quiz", "Ostatnie wyniki", "Zamknij program"]


def main_menu(stdscr):

    attributes = {}
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes["normal"] = curses.color_pair(1)
    attributes["highlighted"] = curses.color_pair(2)
    c = 0
    option = 0
    while c != 10:
        stdscr.erase()
        stdscr.addstr("MENU GŁOWNE\n", curses.A_UNDERLINE)
        for i in range(len(menu_options)):
            if i == option:
                attr = attributes["highlighted"]
            else:
                attr = attributes["normal"]
            stdscr.addstr("{}".format(i + 1))
            stdscr.addstr(menu_options[i] + "\n", attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(menu_options) - 1:
            option += 1
    stdscr.addstr("Wybrałeś {}".format(menu_options[option]))
    stdscr.getch()


def quiz_game(questions_amount: int, QUESTIONS: list, ANSWERS: list):
    points = []
    randomQuestions = picking_random_elements(QUESTIONS, questions_amount)
    randomAnswers = []
    picked_answers = []
    for i in randomQuestions:
        randomAnswers.append(picking_random_elements(ANSWERS[i], len(ANSWERS[i])))
    POINTS = 0
    ITR = 0
    for i in randomQuestions:
        temp_picked_answers = []
        for j in randomAnswers[ITR]:
            temp_picked_answers.append(ANSWERS[i][j])
        ITR += 1
        picked_answers.append(temp_picked_answers)
    print("\n")
    ITR = 0
    ABCD = 65
    ANSWER = ""
    for j in picked_answers:
        print(QUESTIONS[randomQuestions[ITR]])
        for k in j:
            print("{}: {}".format(chr(ABCD), k['answer']), end=" | ")
            ABCD += 1
        print("\n")
        ITR += 1
        ALREADY_ANSWERED = []
        while True:
            ANSWER = str(input("Podaj odpowiedź, jezeli wszystkie odpowiedzi zostaly wprowadzone lub chcesz przerwać quiz wpisz [N]: "))
            if ANSWER == '' or len(ANSWER) > 1 or (ANSWER.upper() in ALREADY_ANSWERED):
                print("Musisz podać odpowiedź w poprawnym formacie i nie powtarzać odpowiedzi...")
            elif ANSWER.upper() == 'N':
                if checking_answers(ALREADY_ANSWERED, picked_answers[ITR-1]) is True:
                    POINTS += 1
                    break
                else:
                    break
            elif len(ALREADY_ANSWERED) == ABCD-65:
                print("Podałeś juz wszystkie odpowiedzi...")
                break
            elif ord(ANSWER.upper()) > (ABCD-1):
                print("Podaj odpowiedź z zakresu A - {}".format(chr(ABCD-1)))
            else:
                ALREADY_ANSWERED.append(ord(ANSWER.upper())-65)
        points.append("{}/{}".format(POINTS, questions_amount))
        ABCD = 65
    print(
        "Twój wynik: {}/{} - {}%".format(
            POINTS, questions_amount, round((POINTS / questions_amount) * 100, 2)
        )
        )
    saving_points_to_file(points, 10)


def create_new_test(path: str):
    if os.path.exists(path) == True:
        print('istnieje')
    else:
        print('nie istnieje')

#! /usr/bin/env python
"""Dummy docstring."""
# from .game_modules import quiz_game
import json
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
    quiz_game,
    create_new_test,
)
QUESTIONS = []
ANSWERS = []
CORRECT_ANSWERS = []
reading_from_file(QUESTIONS, ANSWERS)
# adding_new_questions(QUESTIONS, ANSWERS)
# saving_into_file(QUESTIONS, ANSWERS)
quiz_game(2, QUESTIONS, ANSWERS)
# create_new_test("questionss.json")

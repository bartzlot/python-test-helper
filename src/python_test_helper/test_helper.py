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
)
QUESTIONS = []
ANSWERS = []
CORRECT_ANSWERS = []
reading_from_file(QUESTIONS, ANSWERS, CORRECT_ANSWERS)
# adding_new_questions(QUESTIONS, ANSWERS, CORRECT_ANSWERS)
# saving_into_file(QUESTIONS, ANSWERS, CORRECT_ANSWERS)
quiz_game(1, QUESTIONS, ANSWERS, CORRECT_ANSWERS)

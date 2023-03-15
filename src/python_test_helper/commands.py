import click
import pkg_resources
from .test_modules import (
    adding_new_questions,
    checking_answers,
    curses,
    main_menu,
    picking_random_elements,
    reading_from_file,
    reading_points_from_file,
    saving_into_file,
    saving_points_to_file,
    quiz_game,)

@click.group()
def cli():
    pass


@cli.command()
@click.argument('questions_amount', type=int)
def start(questions_amount):
    quiz_game(questions_amount)


if __name__ == "__main__":
    cli()

"""Dummy docstring."""
import click
from .test_modules import (
    quiz_game,
    create_new_test
    )


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """Fix dummy doc."""


@cli.command()
@click.argument('path', type=click.Path(dir_okay=False, writable=True, readable=True))
def create_test(path):
    """Fix dummy doc."""
    create_new_test(path)


@cli.command()
@click.argument('questions_amount', type=int)
@click.argument('file_name',
                type=click.Path(exists=True,
                                dir_okay=True,
                                readable=True,
                                writable=False,
                                executable=False))
def start(file_name, questions_amount):
    """dummy doc"""
    quiz_game(questions_amount)


# @cli.command()
# @click.argument('file_name', type=str)
# def create_test(file_name):
#     print("test")

if __name__ == "__main__":
    cli()

"""Dummy docstring"""
import click
from .test_modules import quiz_game


@click.group()
def cli():
    """dummy doc"""


@cli.command()
@click.option('--path', default='path')
def create_test(path):
    """dummy doc"""
    print(path)


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


if __name__ == "__main__":
    cli()

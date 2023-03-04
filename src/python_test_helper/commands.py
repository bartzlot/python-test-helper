import click
import pkg_resources


@click.group()
def cli():
    pass


@cli.command()
def start():
    print("hello world")


if __name__ == "__main__":
    cli()

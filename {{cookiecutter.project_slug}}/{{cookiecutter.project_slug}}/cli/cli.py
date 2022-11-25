"""Console script for {{cookiecutter.project_slug}}."""

import sys

import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("{{cookiecutter.project_slug}}.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

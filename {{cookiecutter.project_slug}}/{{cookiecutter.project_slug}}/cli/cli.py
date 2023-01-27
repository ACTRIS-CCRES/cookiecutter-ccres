"""Console script for {{cookiecutter.project_slug}}."""

import logging
import sys

import click

from {{cookiecutter.project_slug}}.logger import get_log_level_from_count, init_logger

lgr = logging.getLogger(__name__)


@click.command()
@click.option(
    "-v",
    "--verbose",
    count=True,
    default=0,
    type=int,
    help=(
        "Set the level of verbosity. By default ERROR.\n"
        "-v set the level to INFO.\n"
        "-vv set the level to DEBUG."
    ),
)
def main(verbose: int) -> int:
    """Command line interface for {{cookiecutter.project_slug}}."""
    log_level = get_log_level_from_count(verbose)
    init_logger(log_level)
    click.echo("{{cookiecutter.project_slug}}.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

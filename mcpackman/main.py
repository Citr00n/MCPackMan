import os
import json
import click
import logging
import appdirs
from prompt_toolkit import prompt

VERSION = 'dev'
LEVELS = [logging.WARNING, logging.INFO, logging.DEBUG]
WORKDIR = appdirs.user_data_dir('mcpackman', 'citr0n')


@click.group()
@click.option('-v', '--verbose', count=True)
@click.help_option('-h', '--help')
def cli(verbose):
    level = LEVELS[min(verbose, (len(LEVELS) - 1))]
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.getLogger('json').setLevel(level)
    logging.debug(f'VERBOSITY: {verbose}')
    logging.debug(f'WORKDIR: {WORKDIR}')


@cli.command()
def test():
    click.echo(click.style('test', fg='green'))


if __name__ == '__main__':
    cli()

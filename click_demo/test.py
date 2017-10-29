# -*- coding:utf-8 -*-
import click
import os
import sys


@click.group()
def cli1():
    click.echo("begin execute cmd of cli1")


@cli1.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def cmd1(count, name=None):
    """Command on cli1"""
    for i in range(count):
        print "{},exec CMD!".format(name)


@click.group()
def cli2():
    pass


@cli2.command()
@click.option('--name', nargs=2, type=click.Tuple([unicode, int]))
def cmd2(name):
    """Command on cli2"""
    print "exec CMD2!, {}".format(name)

cli = click.CommandCollection(sources=[cli1, cli2])


if __name__ == '__main__':
    cli()


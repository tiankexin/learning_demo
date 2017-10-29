import sys
import click


@click.group(invoke_without_command=True)
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    ctx.obj['debug'] = debug


@cli.command()
@click.option('--shout/--abc', default=False)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)


@cli.command()
@click.option('/debug;/no-debug')
def log(debug):
    click.echo('debug=%s' % debug)


@cli.command()
@click.option('--upper', 'transformation', flag_value='upper',
              default=True)
@click.option('--lower', 'transformation', flag_value='lower')
def trans(transformation):
    click.echo(transformation)


@cli.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
def digest(hash_type):
    click.echo(hash_type)


@cli.command()
@click.option('--name', prompt=True)
def hello(name):
    """
    In some cases, you want parameters that can be provided from the command line,
    but if not provided, ask for user input instead.
    This can be implemented with Click by defining a prompt string.
    """
    click.echo('Hello %s!' % name)


@cli.command()
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def encrypt(password):
    click.echo('Encrypting password to %s' % password.encode('rot13'))


@cli.command()
@click.password_option()
def encrypt2(password):
    click.echo('Encrypting password to %s' % password.encode('rot13'))


def print_version(ctx, param, value):
    print "aaaaaaa", value, ctx, ctx.resilient_parsing
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@cli.command()
@click.version_option(version=0.1)
@click.pass_context
def hello2(ctx):
    if ctx.obj['debug']:
        click.echo("UNDER DEBUG:")
    click.echo('Hello World!')


if __name__ == '__main__':
    cli(obj={})

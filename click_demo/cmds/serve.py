from click_demo.cmds import *


@click.command()
def serve():
    print "execute func ##serve"


@click.command()
def serve2():
    print "execute func ##serve"

cmds = [serve, serve2]

if __name__ == '__main__':
    # pylint: disable=E1120
    serve()

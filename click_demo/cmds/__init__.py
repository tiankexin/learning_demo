# -*- coding: utf-8 -*-
import click
import os
import importlib
import sys
sys.path.append('/Users/tkx/testspace/learning_demo')
plugin_folder = os.path.dirname(__file__)

print "aaaaaa", plugin_folder, __file__, __name__
plugin_folder = '/Users/tkx/testspace/learning_demo/click_demo/cmds'
module = importlib.import_module('.' + 'serve', 'click_demo.cmds')
print "bbbbbbb", module


class MyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        return sorted(self.cmds.keys())

    def get_command(self, ctx, name):
        try:
            return self.cmds[name]
        except KeyError:
            raise click.UsageError(
                "There's no such command: %s\n"
                "Available ones are: %s" % (name, ", ".join(self.cmds))
            )

    @property
    def cmds(self):
        if not hasattr(self, '_cmds'):
            filenames = [fn[:-3] for fn in os.listdir(plugin_folder)
                         if fn.endswith('.py') and fn != '__init__.py']
            self._cmds = {}
            print "ccccc", filenames
            for fn in filenames:
                module = importlib.import_module('.' + fn, 'click_demo.cmds')
                print "bbbbbbb", module
                for cmd in getattr(module, 'cmds', []):
                    self._cmds[cmd.name] = cmd
        return self._cmds


@click.command(cls=MyCLI)
@click.version_option()
def cli():
    print "start exec cli##"
    context = click.get_current_context()
    print context.invoked_subcommand

if __name__ == '__main__':
    print "sys args: {}".format(sys.argv)
    cli()

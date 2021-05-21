import sys

from pyforge.command import *
from pyforge.gui.widget.button import Button
from pyforge.utils import *


class PyforgeManager(CommandBase):
    formats = [ArgumentCollection(cmd=StringArgument('^(args|list|include-path|version)$'))]
    description = ['pyforge manager',
            '/pyforge args',
            '/pyforge list',
            '/pyforge include-path',
            '/pyforge version']

    def execute(self):
        if self.args['cmd'] == 'args':
            get_minecraft().dialogue.add_dialogue(' '.join(sys.argv))
        elif self.args['cmd'] == 'list':
            text = '%d mod(s) loaded:\n' % len(mods)
            for mod in mods:
                text += ' - %s\n' % mod
            get_minecraft().dialogue.add_dialogue(text)
        elif self.args['cmd'] == 'include-path':
            text = 'Values in sys.path:\n'
            for d in sys.path:
                text += ' - %s\n' % d
            get_minecraft().dialogue.add_dialogue(text)
        elif self.args['cmd'] == 'version':
            get_minecraft().dialogue.add_dialogue('pyforge %s' % PYFORGEVERSION['str'])


def add_widget():
    mod_button = Button((get_size()[0] - 200) / 2, 210, 200, 40, 'Mods')
    get_minecraft().guis['pause'].frame.add_widget(mod_button)
    get_minecraft().register_event('resize', on_resize)

def on_resize(width, height):
    mod_button.x = (width - 200) / 2
    mod_button.y = 210

register_command('pyforge', PyforgeManager)
get_minecraft().register_event('init', add_widget)

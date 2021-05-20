from pyforge.command import *
from pyforge.utils import *


class PyforgeManager(CommandBase):
    formats = [ArgumentCollection(cmd=StringArgument('^(list|version)$'))]
    description = ['pyforge manager',
            '/pyforge list'
            '/pyforge version']

    def execute(self):
        if self.args['cmd'] == 'list':
            text = '%d mod(s) loaded:\n' % len(mods)
            for mod in mods:
                text += ' - %s\n' % mod
            get_minecraft().dialogue.add_dialogue(text)
        elif self.args['cmd'] == 'version':
            get_minecraft().dialogue.add_dialogue('pyforge %s' % PYFORGEVERSION['str'])


register_command('pyforge', PyforgeManager)

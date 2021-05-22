import sys

from pyforge.command import *
from pyforge.gui.widget.button import Button
from pyforge.utils import *


class PyforgeManager(CommandBase):
    formats = [ArgumentCollection(cmd=StringArgument('^(args|list|include-path|version)$'))]
    description = [assets.get_translation('pyforge.manager.text')[0],
            '/pyforge args',
            '/pyforge list',
            '/pyforge include-path',
            '/pyforge version']

    def execute(self):
        if self.args['cmd'] == 'args':
            get_minecraft().dialogue.add_dialogue(' '.join(sys.argv))
        elif self.args['cmd'] == 'list':
            text = assets.get_translation('pyforge.manager.text')[1] % len(mods)
            for mod in mods:
                text += ' - %s\n' % mod
            get_minecraft().dialogue.add_dialogue(text)
        elif self.args['cmd'] == 'include-path':
            text = assets.get_translation('pyforge.manager.text')[2]
            for d in sys.path:
                text += ' - %s\n' % d
            get_minecraft().dialogue.add_dialogue(text)
        elif self.args['cmd'] == 'version':
            get_minecraft().dialogue.add_dialogue('pyforge %s' % PYFORGEVERSION['str'])


# 为菜单界面加入 Mod Settings 按钮
mod_settings = None

def add_widget():
    global mod_settings
    mod_settings = Button((get_size()[0] - 200) / 2, 210, 200, 40, assets.get_translation('pyforge.pause_menu.mod_settings'))
    get_minecraft().guis['pause'].frame.add_widget(mod_settings)
    get_minecraft().register_event('resize', on_resize)

def on_resize(width, height):
    global mod_settings
    mod_settings.x = (width - 200) / 2
    mod_settings.y = 210

register_command('pyforge', PyforgeManager)
get_minecraft().register_event('init', add_widget)

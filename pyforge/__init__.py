from Minecraft.utils.utils import *

from pyforge import utils

if utils.PYFORGEVERSION != VERSION:
    log_err('Minecraft version is %s, but pyforge version is %s, exit' % (VERSION['str'], utils.PYFORGEVERSION['str']))
    exit(1)
else:
    log_info('Welcome to use pyforge %s' % utils.PYFORGEVERSION['str'])

def main():
    get_game().add_info_ext('pyforge%s' % utils.PYFORGEVERSION['str'])
    get_game().register_event('key_press', lambda a, b: log_info('You press a key'))

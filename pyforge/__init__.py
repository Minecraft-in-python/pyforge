from Minecraft.utils.utils import *

from pyforge import utils

if utils.PYFORGEVERSION != VERSION:
    log_err('Minecraft version is %s, but pyforge version is %s, exit' % (VERSION['str'], utils.PYFORGEVERSION['str']))
    exit(1)
else:
    log_info('Welcome to use pyforge %s' % utils.PYFORGEVERSION['str'])

def init():
    get_game().add_info_ext('pyforge%s' % utils.PYFORGEVERSION['str'])

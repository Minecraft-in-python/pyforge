import os

from Minecraft.utils.utils import *

from pyforge import utils

def add_mod(name, obj):
    utils.mods.setdefault(name, obj())
    log_info("Mod '%s' added" % name)

def main():
    for mod in os.listdir(os.path.join(search_mcpy(), 'lib', VERSION['str'])):
        origin_path = os.path.join(search_mcpy(), 'lib', VERSION['str'], mod)
        if origin_path.endswith('.py') and os.path.isfile(origin_path):
            __import__(mod[:-3])
        elif os.path.isdir(origin_path) and (mod != 'pyforge'):
            __import__(mod)
    for mod in utils.mods.values():
        mod.on_load()
    get_game().add_info_ext('pyforge%s' % utils.PYFORGEVERSION['str'])
    __import__('pyforge.manager')

if utils.PYFORGEVERSION != VERSION:
    log_err('Minecraft version is %s, but pyforge version is %s, exit' % (VERSION['str'], utils.PYFORGEVERSION['str']))
    exit(1)
else:
    log_info('Welcome to use pyforge %s' % utils.PYFORGEVERSION['str'])

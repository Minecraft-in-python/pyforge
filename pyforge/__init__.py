import os

from pyforge.assets import add_assets, get_resource_pack
from minecraft.source import settings
from minecraft.utils.utils import *

from pyforge import utils

def add_mod(name, obj):
    '''
    Add a mod.

    :param: name => mod's name
    :param: obj  => mod itself
    '''
    utils.mods.setdefault(name, obj())
    log_info("Mod '%s' added" % name)

def main():
    '''
    pyforge main function
    '''
    # add mods
    for mod in os.listdir(os.path.join(search_mcpy(), 'lib', VERSION['str'])):
        origin_path = os.path.join(search_mcpy(), 'lib', VERSION['str'], mod)
        if origin_path.endswith('.py') and os.path.isfile(origin_path):
            __import__(mod[:-3])
        elif os.path.isdir(origin_path) and (mod != 'pyforge'):
            __import__(mod)
    # load mods
    for mod in utils.mods.values():
        mod.on_load()
    get_game().add_info_ext('pyforge%s' % utils.PYFORGEVERSION['str'])
    add_assets(os.path.join(os.path.dirname(__file__), 'assets'))
    # load language which player set
    if not get_resource_pack().set_lang(settings['lang']):
        # load failed, try to load English
        if not get_resource_pack().set_lang('en_US'):
            # fail again, exit game
            log_err('No language file can be loaded, exit')
            exit(1)
    # import `pyforge.manager` to manage mods
    __import__('pyforge.manager')

if utils.PYFORGEVERSION != VERSION:
    log_err('Minecraft version is %s, but pyforge version is %s, exit' % (VERSION['str'], utils.PYFORGEVERSION['str']))
    exit(1)
else:
    log_info('Welcome to use pyforge %s' % utils.PYFORGEVERSION['str'])

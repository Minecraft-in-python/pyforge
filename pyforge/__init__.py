import os

from pyforge.assets import Assets
from minecraft.source import settings
from minecraft.utils.utils import *

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
    utils.assets = Assets(os.path.join(os.path.dirname(__file__), 'assets'))
    # 载入玩家设置的语言
    if not utils.assets.set_lang(settings['lang']):
        # 第一次载入失败, 尝试载入英语语言文件
        if not utils.assets.set_lang('en_US'):
            # 再次载入失败, 退出游戏
            log_err('No language file can be loaded, exit')
            exit(1)
    __import__('pyforge.manager')

if utils.PYFORGEVERSION != VERSION:
    log_err('Minecraft version is %s, but pyforge version is %s, exit' % (VERSION['str'], utils.PYFORGEVERSION['str']))
    exit(1)
else:
    log_info('Welcome to use pyforge %s' % utils.PYFORGEVERSION['str'])

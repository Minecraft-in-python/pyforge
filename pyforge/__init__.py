from Minecraft.utils.utils import *

from pyforge import utils

if utils.VERSION != VERSION:
    log_err('Minecraft version is %s, but pyforge version is %s, exit' % (VERSION['str'], utils.VERSION['str']))
    exit(1)
else:
    log_info('Welcome to use pyforge %s' % utils.VERSION['str'])

def init():
    # 在 Minecraft.game.Game 类初始化之后, 世界生成之前运行
    get_game().add_info_ext('pyforge%s' % utils.VERSION['str'])

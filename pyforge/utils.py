import Minecraft.utils.utils as _utils

from pyglet.window import key as _keys

get_minecraft = _utils.get_game
get_size = _utils.get_size
log_err, log_info, log_warn = _utils.log_err, _utils.log_info, _utils.log_warn
search_mcpy = _utils.search_mcpy

def get_key(key):
    if hasattr(_keys, key.upper()):
        return getattr(_keys, key.upper())
    elif hasattr(_keys, '_' + key):
        return getattr(_keys, '_' + key)
    else:
        raise KeyError("'%s'" % key)

mods = dict()
assets = None
MCPYVERSION = _utils.VERSION
PYFORGEVERSION = {
        'major': 0,
        'minor': 3,
        'patch': 2,
        'str': '0.3.2',
        'data': 1
        }

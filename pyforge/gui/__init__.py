from minecraft.utils.utils import *

def toggle_gui(name):
    get_game().toggle_gui(name)

def register_gui(name, gui):
    get_game().guis.setdefault(str(name), gui)

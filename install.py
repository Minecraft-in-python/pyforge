#!/usr/bin/env python3

from os import environ,mkdir,  path
from re import search
from shutil import copytree, rmtree
from sys import platform


def install():
    version = get_version()
    print('This is pyforge %s installation script.' % version)
    input('Press ENTER to install pyforge: ')
    MCPYPATH = search_mcpy()
    if not path.isdir(MCPYPATH):
        mkdir(MCPYPATH)
    if not path.isdir(path.join(MCPYPATH, 'mod')):
        mkdir(path.join(MCPYPATH, 'mod'))
    if path.isdir(path.join(MCPYPATH, 'lib', version, 'pyforge')):
        rmtree(path.join(MCPYPATH, 'lib', version, 'pyforge'))
    copytree(get_file('pyforge'), path.join(MCPYPATH, 'lib', version, 'pyforge'))
    print('Done')

def get_file(f):
    # 返回文件目录下的文件名
    return path.abspath(path.join(path.dirname(__file__), f))

def get_version():
    f = open(path.join(get_file('pyforge'), 'utils.py'))
    start_find = False
    for line in f.readlines():
        if line.strip() == 'PYFORGEVERSION = {':
            start_find = True
        elif (line.strip() == '}') and start_find:
            start_find = False
        elif line.strip().startswith("'str'") and start_find:
            return search(r"\d(\.\d+){2}(\-alpha|\-beta|\-pre\d+)?", line.strip()).group()

def search_mcpy():
    # 搜索文件存储位置
    if 'MCPYPATH' in environ:
        MCPYPATH = environ['MCPYPATH']
    elif platform == 'darwin':
        MCPYPATH = path.join(path.expanduser('~'), 'Library', 'Application Support', 'mcpy')
    elif platform.startswith('win'):
        MCPYPATH = path.join(path.expanduser('~'), 'mcpy')
    else:
        MCPYPATH = path.join(path.expanduser('~'), '.mcpy')
    return MCPYPATH

if __name__ == '__main__':
    install()

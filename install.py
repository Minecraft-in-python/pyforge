#!/usr/bin/env python3

from os import environ,mkdir,  path
from shutil import copytree, rmtree
from sys import platform

VERSION = '0.3.2'

def install():
    print('This is pyforge %s installation script.' % VERSION)
    input('Press ENTER to install pyforge: ')
    MCPYPATH = search_mcpy()
    if not path.isdir(MCPYPATH):
        mkdir(MCPYPATH)
    if not path.isdir(path.join(MCPYPATH, 'mod')):
        mkdir(path.join(MCPYPATH, 'mod'))
    if path.isdir(path.join(MCPYPATH, 'lib', VERSION, 'pyforge')):
        rmtree(path.join(MCPYPATH, 'lib', VERSION, 'pyforge'))
    copytree(get_file('pyforge'), path.join(MCPYPATH, 'lib', VERSION, 'pyforge'))
    print('Done')

def get_file(f):
    # 返回文件目录下的文件名
    return path.abspath(path.join(path.dirname(__file__), f))

def search_mcpy():
    # 搜索文件存储位置
    if 'MCPYPATH' in environ:
        MCPYPATH = environ['MCPYPATH']
    elif platform.startswith('win'):
        MCPYPATH = path.join(path.expanduser('~'), 'mcpy')
    else:
        MCPYPATH = path.join(path.expanduser('~'), '.mcpy')
    return MCPYPATH

if __name__ == '__main__':
    install()

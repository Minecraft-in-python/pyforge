import json
import os

import pyglet
from pyglet.image import load as load_image

class Assets():

    def __init__(self, name):
        self.base_dir = name

    def set_lang(self, lang):
        lang_file = os.path.join(self.base_dir, 'lang', lang + '.json')
        if os.path.exists(lang_file):
            try:
                self.lang = json.load(open(lang_file, 'r+', encoding='utf-8'))
                return True
            except:
                return False
        else:
            return False

    def get_translation(self, name):
        return self.lang.get(name, name)

    def get_asset(self, path):
        '''
        Get resources from assets, the support paths are below:

        | path prefix | extension | type |
        | :---------- | :-------: | ---: |
        |    /text    |  \*.txt   | str  |
        |   others    |  \*.json  | dict |

        :param: path => Where the asset store
        :ret: See the table
        '''
        if path.find('/') != -1:
            file_type = path.split('/')[0]
            if file_type == 'text':
                return open(os.path.join(self.base_dir, path + '.txt'), 'r+').read()
            elif file_type == 'textures':
                return load_image('image.png', file=open(os.path.join(self.base_dir, path + '.png'), 'rb'))
            else:
                return json.load(open(os.path.join(self.base_dir, path + '.json'), 'r+', encoding='utf-8'))
        else:
            raise FileNotFoundError("No such asset: '%s'" % path)

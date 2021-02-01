from json import load


class Lang():

    def __init__(self, name):
        self._lang = load(open(name, 'r+', encoding='utf-8'))

    def get(self, name, *args):
        if name in self._lang:
            try:
                return self._lang[name] % args
            except:
                return name
        else:
            return name

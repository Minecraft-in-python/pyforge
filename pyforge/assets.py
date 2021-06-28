from minecraft.source import resource_pack as _resource_pack

def add_assets(path):
    _resource_pack.add(path)

def get_assets(path):
    return _resource_pack.get_resource(path)

def get_translation(name):
    return _resource_pack.get_translation(name)

def get_resource_pack():
    return _resource_pack

import Minecraft.command as _command

CommandBase = _commands.CommandBase

def register_command(s, command):
    _commands.commands.setdefault(s, command)

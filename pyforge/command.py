import Minecraft.arguments as _arguments
import Minecraft.command as _command

BaseArgument = _arguments.BaseArgument
StringArgument = _arguments.StringArgument
NumberArgument = _arguments.NumberArgument
BlockArgument = _arguments.BlockArgument
BooleanArgument = _arguments.BooleanArgument
PositionArgument = _arguments.PositionArgument
ArgumentCollection = _arguments.ArgumentCollection

CommandBase = _commands.CommandBase

def register_command(s, command):
    _commands.commands.setdefault(s, command)

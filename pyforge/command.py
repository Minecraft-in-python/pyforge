import Minecraft.command.base as _base
from Minecraft.command.commands import commands as _commands
import Minecraft.command.arguments as _arguments

BaseArgument = _arguments.BaseArgument
StringArgument = _arguments.StringArgument
NumberArgument = _arguments.NumberArgument
BlockArgument = _arguments.BlockArgument
BooleanArgument = _arguments.BooleanArgument
PositionArgument = _arguments.PositionArgument
ArgumentCollection = _arguments.ArgumentCollection

CommandBase = _base.CommandBase

def register_command(s, command):
    _commands.setdefault(s, command)

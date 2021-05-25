import minecraft.command.base as _base
from minecraft.command.commands import commands as _commands
import minecraft.command.arguments as _arguments

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

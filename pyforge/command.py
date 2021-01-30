from Minecraft.command import commands

CommandBase = commands.CommandBase

def register_command(s, command):
    commands.commands.setdefault(s, command)

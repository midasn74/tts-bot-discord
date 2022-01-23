import discord
from discord.ext import commands
from discord.ext.commands.core import command
import configparser

settings = configparser.ConfigParser(comment_prefixes='/', allow_no_value=True)
settings.read("settings.ini")
TOKEN = settings['SECRET']['TOKEN']
commandPrefix = settings['DEFAULT']['commandPrefix']

initial_extensions_commands = [
    "cogs.commands.helpCommand",
    "cogs.commands.voiceCommands",
]

initial_extensions_events = [
    "cogs.events.errorHandler",
    "cogs.events.on_ready",
]

activity = discord.Activity(type=discord.ActivityType.listening, name=f"{commandPrefix}help")
intents = discord.Intents.all()
client = commands.Bot(command_prefix=commandPrefix, 
                    description="TTS Bot",
                    help_command=None,
                    case_insensitive=True,
                    intents=intents,
                    activity=activity)

if __name__ == '__main__':
    for extension in initial_extensions_commands: # load commands
        client.load_extension(extension)  

    for extension in initial_extensions_events: # load events
        client.load_extension(extension)  

    client.run(TOKEN) # run the bot

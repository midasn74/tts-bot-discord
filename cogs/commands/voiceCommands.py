import discord
from discord.ext import commands
from gtts import gTTS
import gtts
import nacl
from discord import FFmpegPCMAudio
from mutagen.mp3 import MP3
import configparser

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.settings = configparser.ConfigParser(comment_prefixes='/', allow_no_value=True)
        self.settings.read('settings.ini')
        self.commandPrefix = self.settings['DEFAULT']['commandPrefix']
    
    @commands.guild_only()
    @commands.command(name="connect", 
                    description="Joins the voice channel you are currently in.", 
                    brief="Voice")
    async def connect(self, ctx):
        if ctx.author.voice != None:
            if ctx.voice_client == None:
                await ctx.author.voice.channel.connect()
            else:
                sameChannel = False
                for voice_client in self.client.voice_clients:
                    if voice_client.channel == ctx.author.voice.channel:
                        sameChannel = True
                        break
                if not sameChannel:
                    await ctx.voice_client.disconnect()
                    await ctx.author.voice.channel.connect()
        else:
            await ctx.send("The bot does not know which channel to join because you are not connected to a channel.")

    @commands.guild_only()
    @commands.command(name="disconnect", 
                    description="Leaves the voice channel the bot is currently in.", 
                    brief="Voice")
    async def disconnect(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.disconnect()

    @commands.guild_only()
    @commands.command(name="tts", 
                    description="Joins the voice channel you are currently in and plays the text you sent. \n required argument(s): text between 0 and 200 characters (string)", 
                    brief="Voice")
    async def tts(self, ctx, *, args=""):
        if len(args) < 200 and len(args) > 0:
            if ctx.author.voice != None:
                if ctx.voice_client == None:
                    await ctx.author.voice.channel.connect()
                else:
                    sameChannel = False
                    for voice_client in self.client.voice_clients:
                        if voice_client.channel == ctx.author.voice.channel:
                            sameChannel = True
                            break
                    if not sameChannel:
                        await ctx.voice_client.disconnect()
                        await ctx.author.voice.channel.connect()
            else:
                await ctx.send("The bot does not know which channel to join because you are not connected to a channel.")

            if not ctx.voice_client.is_playing():
                try:
                    language = self.settings['sever.languages'][str(ctx.guild.id)]
                except:
                    language = "en"
                try:
                    gTTS(text=args, lang=language, slow=False).save(f".ttsTemp{ctx.guild.id}.mp3")
                except:
                    await ctx.send("Something went wrong while trying to reach the api.")

                source = FFmpegPCMAudio(f".ttsTemp{ctx.guild.id}.mp3")
                player = ctx.voice_client.play(source)
        else:
            await ctx.send("The text has to contain less than 200 and more than 0 characters.")

    @commands.guild_only()
    @commands.command(name="setlanguagetts", 
                    description="Sets the tts language for this guild.", 
                    brief="Voice")
    async def setlanguagetts(self, ctx, *, args=""):
        languages = ""
        languageCodes = []
        for key, value in gtts.lang.tts_langs().items():
            languages = languages + f"`{key}`: {value} \n"
            languageCodes.append(key)

        if args in languageCodes:
            self.settings['sever.languages'][str(ctx.guild.id)] = args
            with open('settings.ini', 'w') as settingsfile:
                self.settings.write(settingsfile)
            await ctx.send(f"TTS language successfully set to `{args}`")

            self.settings.read('settings.ini')
        elif args == "" or args == None or args == " ":
            await ctx.send(f"Please type the language code you want to set. \nType `{self.commandPrefix}supportedlanguages` to see a list of all supported languages.")
        else:
            await ctx.send(f"Language code is not correct. \nType `{self.commandPrefix}supportedlanguages` to see a list of all supported languages.")
        
    @commands.command(name="supportedlanguages", 
                    description="Sends a list of all the supported languages.", 
                    brief="Voice")
    async def supportedlanguages(self, ctx):
        languages = ""
        for key, value in gtts.lang.tts_langs().items():
            languages = languages + f"`{key}`: {value} \n"

        await ctx.send(languages)

def setup(bot):
    bot.add_cog(Voice(bot))
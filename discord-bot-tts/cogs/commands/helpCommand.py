import discord
from discord.ext import commands
import configparser

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.settings = configparser.ConfigParser(comment_prefixes='/', allow_no_value=True)
        self.settings.read('settings.ini')
        self.commandPrefix = self.settings['DEFAULT']['commandPrefix']
        self.embedColourR = int(self.settings['DEFAULT']['embedColour.r'])
        self.embedColourG = int(self.settings['DEFAULT']['embedColour.g'])
        self.embedColourB = int(self.settings['DEFAULT']['embedColour.b'])

    @commands.command(name='help', 
                    description='Shows you this message.')
    async def help(self, ctx):
            embed=discord.Embed(colour=discord.Color.from_rgb(self.embedColourR,self.embedColourG,self.embedColourB), title="All commands")
            embed.set_thumbnail(url=self.client.user.avatar_url)

            for command in self.client.commands:
                embed.add_field(name=command, value=command.description, inline=False)

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
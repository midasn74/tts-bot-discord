import discord
from discord.ext import commands
import random
import sys
import traceback
from discord import FFmpegPCMAudio
import nacl
import configparser

class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot connected as: {self.client.user.name}#{self.client.user.discriminator}")

def setup(bot):
    bot.add_cog(OnReady(bot))

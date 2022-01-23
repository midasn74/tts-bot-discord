import discord
from discord.ext import commands
import random
import sys
import traceback

class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = ()

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'`{ctx.command}` can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            await ctx.send('The given argument(s) were not correct.')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'One or more required arguments were missing.')

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f'Command not found')

        elif isinstance(error, commands.BotMissingPermissions):
            try:
                await ctx.send(f'The bot is missing the required permissions to complete this action.')
            except:
                try:
                    await ctx.guild.owner.send(f'The bot is missing required permissions in your sever: {ctx.guild.name} (guild id: {ctx.guild.id})')
                except:
                    pass

        else:
            await ctx.send(f'unkown error occured: `{error}`')
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(bot):
    bot.add_cog(ErrorHandler(bot))

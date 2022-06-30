import discord
from discord.app import slash_command, option, ApplicationContext
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command()
    async def ping(self, ctx: commands.Context):
        await ctx.respond("pong")

def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))
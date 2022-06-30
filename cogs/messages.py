import discord
from discord.ext import commands, slash_command, option, ApplicationContext
from bot import guilds

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids = guilds)
    async def ping(self, ctx: commands.Context):
        await ctx.respond("pong")

def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))
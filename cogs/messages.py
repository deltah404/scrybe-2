import discord
from discord.ext import commands
import bot


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=bot.guilds)
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond("pong")

def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))

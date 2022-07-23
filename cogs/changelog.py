from discord.ext import commands
from bot import guilds
import discord


class Changelog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=guilds)
    async def changelog(self, ctx):
        with open("./changelog.txt", "r") as fp:
            e = discord.Embed(title="Changelog", description=fp.read())
        await ctx.send_response(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
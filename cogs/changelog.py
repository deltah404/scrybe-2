import discord
import bot
from discord.ext import commands


class Changelog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=bot.guilds)
    async def changelog(self, ctx):
        with open("./changelog.txt", "r") as fp:
            e = discord.Embed(title="Changelog", description=fp.read())
            e.set_author(
                name=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar)
            await ctx.send_response(embed=e, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Changelog(bot))

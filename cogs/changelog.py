from discord.ext import commands
import resources.get_configs
import discord

guilds = resources.get_configs.get_attr("guilds")

class Changelog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        guild_ids=guilds,
        description="Sends the changelog of the newest features added to the bot"
    )
    async def changelog(self, ctx):
        with open("./changelog.txt", "r") as fp:
            e = discord.Embed(title="Changelog", description=fp.read())
        await ctx.send_response(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))

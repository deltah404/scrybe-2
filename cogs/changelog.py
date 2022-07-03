import discord
import bot
from discord.ext import commands


class Changelog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids = bot.guilds)
    async def changelog(self, ctx):
        with open("./changelog.txt", "r") as fp:
            e = discord.Embed(title="Changelog", description=fp.read())
            e.set_author(name = f"Requested by {ctx.author}", icon_url = ctx.author.display_avatar)
            response = await ctx.respond(":o: Please wait...")
            await response.delete_original_message()
            await ctx.send(embed=e)

def setup(bot: commands.Bot):
    bot.add_cog(Changelog(bot))

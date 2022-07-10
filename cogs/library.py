from discord.ext import commands
from resources.get_library import get_library
import discord
import bot


class Library(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=bot.guilds)
    async def library(self, ctx):
        library = get_library()["library"]
        e = discord.Embed(title="Writer's Cave Library")
        e.set_footer(text="To view more information, including the links to read each book, run XXXX")

        for id in library:
            book = library[id]
            e.add_field(name=f"{id}: {book['title']}", value=f"by {book['author']}", inline=False)

        await ctx.send_response(embed=e)


def setup(bot):
    bot.add_cog(Library(bot))

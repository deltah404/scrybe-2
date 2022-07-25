from discord.ext import commands
from PyDictionary import PyDictionary
import resources.get_configs
import discord

guilds = resources.get_configs.get_attr("guilds")


class Language(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        guild_ids=guilds,
        descriptions="Shows definitions for a specified English word"
    )
    async def define(self, ctx, word: discord.Option(str)):
        words = PyDictionary()
        word = word.lower()
        response = await ctx.send_response(f":mag_right: Searching for *\"{word}\"*...")

        definition = words.meaning(word)
        e = discord.Embed(
            title=f':notebook_with_decorative_cover: Definitions for "{word}"'
        )
        if not definition:
            e.description = ":question: No definitions found."
        else:
            e.description = ""
            tick = 1
            for k in definition.keys():
                for d in (definition[k])[:7]:
                    e.add_field(
                        name=k, value=f"{tick}: {d.replace(' (', '; ').replace('(','')}", inline=False)
                    tick += 1

        await response.edit_original_message(embed=e, content="")


def setup(bot):
    bot.add_cog(Language(bot))

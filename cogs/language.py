import discord
import bot
from discord.ext import commands
from PyDictionary import PyDictionary


class Language(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=bot.guilds)
    async def define(self, ctx, word: discord.Option(str)):
        words = PyDictionary()
        word = word.lower()
        response = await ctx.send_response(f":mag_right: Searching for **` {word} `**")

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
                for d in (definition[k])[0:7]:
                    e.add_field(
                        name=k, value=f"{tick}: {d.replace(' (', '; ').replace('(','')}", inline=False)
                    tick += 1

        e.set_author(
            name=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar)

        await response.edit_original_message(embed=e, content="")


def setup(bot: commands.Bot):
    bot.add_cog(Language(bot))

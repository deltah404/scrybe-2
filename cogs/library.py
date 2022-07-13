from random import choices
from discord.ext import commands
from resources.get_library import get_library, add_review
import discord
import bot
import json

empty_star = "<:0star:996011723536465960>"
half_star = "<:05star:996011722441773176>"
full_star = "<:1star:996011724505362503>"
verified = "<:verified:996028752070987796>"

#  to-do
#  O  add "add to library" command
#  O  add "remove from library" command
#  O  set user permissions for two above commands


def human_rating(book) -> str:
    """Convert numerical rating to a string of corresponding star emojis"""
    if isinstance(book, dict):
        if book["reviews"] == {}:
            rating = 2.5
        else:
            rating = 0
            for review in book["reviews"].keys():
                rating += book["reviews"][review]["rating"]
            rating /= len(book["reviews"])
            rating = round(rating * 2) / 2

        stars = ""
        count = 0
        while rating > 0:
            if rating > 0.5:
                stars += full_star
                rating -= 1
                count += 1
            elif rating == 0.5:
                stars += half_star
                rating -= 0.5
                count += 1

        stars += empty_star*(5-count)

        return stars


with open("resources/config.json") as fp:
    config = json.load(fp)

library = get_library()["library"]


class Library(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    library_group = discord.SlashCommandGroup(
        "library", "Commands for the server library")

    @library_group.command(guild_ids=bot.guilds)
    async def list(self, ctx):
        library = get_library()["library"]
        e = discord.Embed(title="Writer's Cave Library")
        e.set_footer(
            text="To view more information, including the links to read each book, run /library info <ID>")

        for id in library:
            book = library[id]
            e.add_field(name=f"{book['title']}",
                        value=f"by {book['author']}\n{human_rating(book)} *({len(book['reviews'])} reviews)*", inline=False)

        await ctx.send_response(embed=e)

    @library_group.command(guild_ids=bot.guilds)
    async def info(self, ctx, book: discord.Option(choices=[discord.OptionChoice(name=library[book]["title"], value=book) for book in library])):
        library = get_library()["library"]
        if str(book) not in library:
            return await ctx.send_response("There is no book with this ID. Try running `/library list` to see what books are available.", ephemeral=True)

        book = library[str(book)]

        verified_link = False

        for link in config["verified_links"]:
            if book["link"].startswith(link):
                verified_link = True

        class LinkView(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
                urlbutton = discord.ui.Button(
                    label=f"Read {book['title']}", style=discord.ButtonStyle.gray, url=book["link"])
                self.add_item(urlbutton)

        e = discord.Embed(
            title=book["title"], description=config["unverified_link_message"] if not verified_link else config["verified_link_message"].format(verified))

        e.add_field(name="Author", value=book["author"])

        e.add_field(
            name="Rating", value=f'{human_rating(book)} (*{len(book["reviews"])} reviews)*')

        await ctx.send_response(embed=e, view=LinkView())

    @library_group.command(guild_ids=bot.guilds)
    async def review(self, ctx, book: discord.Option(choices=[discord.OptionChoice(name=library[book]["title"], value=book) for book in library]), rating: discord.Option(
            choices=[str(n) for n in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]]), content: discord.Option(default="")):
        await ctx.send_response("~")
        add_review(book, {
            "rating": rating,
            "content": content,
            "author": ctx.author.id
        })


def setup(bot):
    bot.add_cog(Library(bot))

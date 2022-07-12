from discord.ext import commands
from resources.get_library import get_library
import discord
import bot
import json

empty_star = "<:0star:996011723536465960>"
half_star = "<:05star:996011722441773176>"
full_star = "<:1star:996011724505362503>"
verified = "<:verified:996028752070987796>"


def human_rating(book) -> str:
    if book["reviews"] == {}:
        rating = 2.5
    else:
        for review in book["reviews"]:
            rating += review["rating"]
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
            e.add_field(name=f"{id}: {book['title']}",
                        value=f"by {book['author']}", inline=False)

        await ctx.send_response(embed=e)

    @library_group.command(guild_ids=bot.guilds)
    async def info(self, ctx, bookid: discord.Option(int, "Enter the ID of the book you wish to view")):
        library = get_library()["library"]
        if str(bookid) not in library:
            return await ctx.send_response("There is no book with this ID. Try running `/library list` to see what books are available.", ephemeral=True)

        book = library[str(bookid)]

        verified_link = False

        for link in config["verified_links"]:
            if book["link"].startswith(link):
                verified_link = True

        e = discord.Embed(
            title=book["title"], description=config["unverified_link_message"] if not verified_link else config["verified_link_message"].format(verified))

        e.add_field(name="Author", value=book["author"])

        e.add_field(name="Rating", value=human_rating(book))
        e.add_field(
            name="Link", value=f"[Click here]({book['link']})", inline=False)

        await ctx.send_response(embed=e)


def setup(bot):
    bot.add_cog(Library(bot))

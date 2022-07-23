from discord.ext import commands
import discord

class Empty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Empty(bot))
import discord
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()
slash = discord.SlashCommand(bot, sync_commands=True)
bot.run(os.environ["bot_token"])

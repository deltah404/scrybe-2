import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()
bot.run(os.environ["TOKEN"])

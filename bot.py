import discord
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()

guilds = [992020236222091355,915996676144111706]

for fn in os.listdir("./cogs"):
    bot.load_extension(f"cogs.{fn[:-3]}")

bot.run(os.environ["bot_token"])

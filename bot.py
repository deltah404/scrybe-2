from dotenv import load_dotenv
import discord
import os

guilds = [992020236222091355, 915996676144111706]

bot = discord.Bot()

load_dotenv()

# import all bot cogs
def load_cogs():
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.{fn[:-3]}")

# start up the bot
load_cogs()
bot.run(os.environ["bot_token"])

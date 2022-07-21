from dotenv import load_dotenv
import discord
import os
import json

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

with open("Scrybe-2/resources/emoji.json", "r") as fp:
    e = json.load(fp)
    verified = e["verified"]
    loading = e["loading"]

bot = discord.Bot()

# import all bot cogs
for fn in os.listdir("Scrybe-2/cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")

# start up the bot
bot.run(os.environ["bot_token"])

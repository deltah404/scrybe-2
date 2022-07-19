from dotenv import load_dotenv
import discord
import os
import json

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

with open("resources/emoji.json", "r") as fp:
    e = json.load(fp)
    verified = e["verified"]
    loading = e["loading"]

Bot = discord.Bot()

# import all bot cogs
for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        Bot.load_extension(f"cogs.{fn[:-3]}")

# start up the bot
Bot.run(os.environ["bot_token"])

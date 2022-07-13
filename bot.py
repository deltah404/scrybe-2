from dotenv import load_dotenv
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

bot = discord.Bot()

guilds = [992020236222091355]  # 915996676144111706 #

# import all bot cogs
for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")

# start up the bot
bot.run(os.environ["bot_token"])

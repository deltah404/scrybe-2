from dotenv import load_dotenv
import discord
import os

guilds = [992020236222091355, 915996676144111706]


def load_cogs():
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.{fn[:-3]}")


if __name__ == "__main__":
    bot = discord.Bot()
    load_dotenv()
    load_cogs()
    bot.run(os.environ["bot_token"])

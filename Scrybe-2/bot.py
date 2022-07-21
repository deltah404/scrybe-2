from dotenv import load_dotenv
import discord
import os
import json

guilds = [992020236222091355, 915996676144111706]
with open("Scrybe-2/resources/emoji.json", "r") as fp:
    e = json.load(fp)
    verified = e["verified"]
    loading = e["loading"]


def main():
    intents = discord.Intents.default()
    intents.message_content = True

    load_dotenv()

    bot = discord.Bot()

    # import all bot cogs
    for fn in os.listdir("Scrybe-2/cogs"):
        if fn.endswith(".py"):
            bot.load_extension(f"cogs.{fn[:-3]}")

    # start up the bot
    bot.run(os.environ["bot_token"])


if __name__ == "__main__":
    main()

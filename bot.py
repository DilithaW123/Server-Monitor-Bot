import os
import discord
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID = os.getenv('USER_ID')
AUTHOR = os.getenv('AUTHOR')

intents = discord.Intents.default()
intents.message_content = True

client  = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected.')
    user = await client.fetch_user(USER_ID)
    await user.send("Hello, I'm now up and running!")

@client.event
async def on_message(message):
    if (message.author != AUTHOR):
        return
    msg = message.content
    if (msg[0] != "\/"):
        return;
    else:
        print(f'Received command {msg}')
    msg = msg[1:]

    match msg:
        case "shutdown":
            os.system("shutdown /s /t 1")

client.run(DISCORD_TOKEN)

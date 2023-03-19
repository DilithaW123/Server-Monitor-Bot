import os
import discord
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID = os.getenv('USER_ID')

client  = discord.Client(discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected.')
    user = await client.fetch_user(USER_ID)
    await user.send("Hello, I'm now up and running!")

@client.event
async def on_message(message):
    print(message);
    

client.run(DISCORD_TOKEN)

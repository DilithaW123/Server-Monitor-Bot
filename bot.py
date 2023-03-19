import os
import discord
from dotenv import load_dotenv
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

client  = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected.')

@client.event
async def on_message(message): 
    print(message.author)

client.run(DISCORD_TOKEN);


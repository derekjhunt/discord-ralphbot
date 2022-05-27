#!/usr/bin/python3

import discord
from discord.ext import commands
from discord import Embed
import random
import aiohttp
import json
import requests
import asyncio
import logging
import praw

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

description = '''Ralphbot - your friendly local Ralph Wiggum.
'''
bot = commands.Bot(command_prefix='!', intents=intents, help_command=commands.DefaultHelpCommand(), description=description)

# Load our Cogs
cogs_list = [
    'dankmemes',
    'happyhour',
    'heinlein',
    'memes',
    'ping',
    'qotd',
    'quote',
    'ralph',
    'roll',
    'trump',
    'urban',
    'weather',
    'wedding',
    'rlm'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

colour = random.randint(0x000000, 0xffffff)

print("Starting ralphbot...")

TOKEN = open("token.txt","r").readline()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


#If there is an error, it will answer with an error
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

print("Bot is ready!")
bot.run(TOKEN)

#!/usr/bin/python3

import discord
from discord.ext import commands
import random

description = '''Ralphbot - your friendly local Ralph Wiggum.
'''
bot = commands.Bot(command_prefix='?', description=description)

print("Starting ralphbot...")

TOKEN = open("token.txt","r").readline()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#We delete default help command
bot.remove_command('help')

@bot.command()
async def test(ctx):
    await ctx.send("test")

#answers with the ms latency
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)}ms ')


#Embeded help with list and details of commands
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='?ping', value='Returns bot respond time in milliseconds', inline=False)
    embed.add_field(name='?ralph', value='Get a wonderful quote from RalphBot', inline=False)
    await ctx.send(embed=embed)


#Answers with a random quote
@bot.command()
async def ralph(ctx):
    responses = open('ralph.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#If there is an error, it will answer with an error
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')


# Currently disabled
#react to any message that contains 'drama'
#@bot.event
#async def on_message(ctx):
#    if 'drama' in ctx.content:
#        emoji = '\N{EYES}'
#        await ctx.add_reaction(emoji)

print("Bot is ready!")
bot.run(TOKEN)

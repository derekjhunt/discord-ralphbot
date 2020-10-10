#!/usr/bin/python3

import discord
from discord.ext import commands
import random
import wikiquote
import aiohttp
import json
import asyncio

description = '''Ralphbot - your friendly local Ralph Wiggum.
'''
bot = commands.Bot(command_prefix='?', description=description)

print("Starting ralphbot...")

TOKEN = open("token.txt","r").readline()

# Edit thingy
async def edit(ctx, content=None, embed=None, ttl=None):
    perms = ctx.channel.permissions_for(ctx.me).embed_links
    ttl = None if ctx.message.content.endswith(' stay') else ttl
    try:
        if ttl and perms:
            await ctx.message.edit(content=content, embed=embed)
            await asyncio.sleep(ttl)
            try:
                await ctx.message.delete()
            except:
                log.error('Failed to delete Message in {}, #{}'.format(ctx.guild.name, ctx.channel.name))
                pass
        elif ttl is None and perms:
            await ctx.message.edit(content=content, embed=embed)
        elif embed is None:
            await ctx.message.edit(content=content, embed=embed)
        elif embed and not perms:
            await ctx.message.edit(content='\N{HEAVY EXCLAMATION MARK SYMBOL} No Perms for Embeds', delete_after=5)
    except:
        if embed and not perms:
            await ctx.message.edit(content='\N{HEAVY EXCLAMATION MARK SYMBOL} No Perms for Embeds', delete_after=5)
        else:
            await ctx.send(content=content, embed=embed, delete_after=ttl, file=None)


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

@bot.command()
async def wedding(ctx):
    await ctx.send("October 10th, you stupid cunt. Check your :calendar:. Also, don't be cheap: https://paypal.me/pools/c/8joQUEB901")

#Embeded help with list and details of commands
@bot.command(pass_context=True)
async def help(ctx):
    helptext = "```"
    for command in self.bot.commands:
        helptext+=f"{command}\n"
    helptext+="```"
    #embed = discord.Embed(
    #    colour = discord.Colour.green())
    #embed.set_author(name='Help : list of commands available')
    #embed.add_field(name='?ping', value='Returns bot respond time in milliseconds', inline=False)
    #embed.add_field(name='?ralph', value='Get a wonderful quote from RalphBot', inline=False)
    #await ctx.send(embed=embed)
    await ctx.send(helptext)

#Answers with a random quote
@bot.command()
async def ralph(ctx):
    responses = open('ralph.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

#Answers with a specific quote
@bot.command()
async def ralphtest(ctx,line: int):
    responses = open('ralph.txt').read().splitlines()
    response = responses[line-1]
    await ctx.send(response)	
	

#Answers with a random Heinlein quote
@bot.command()
async def heinlein(ctx):
    response = random.choice(wikiquote.quotes('Robert A. Heinlein'))
    await ctx.send(response)

#Answers with a random Rawles quote
@bot.command()
async def rawles(ctx):
    response = random.choice(wikiquote.quotes('James Wesley Rawles'))
    await ctx.send(response)    

@bot.command()
async def quote(ctx,arg):
#    try:
    response = random.choice(wikiquote.quotes(arg))
    #except wikiquote.DisambiguationPageException as e:
    #  s = random.choice(e.options)
    #  response = wikiquote.quotes(s)
    await ctx.send(response)

#Answers with a random quote
@bot.command()
async def trump(ctx):
    response = random.choice(wikiquote.quotes('Donald Trump'))
    await ctx.send(response)

#Answers with the quote of the day
@bot.command()
async def qotd(ctx):
    response = wikiquote.quote_of_the_day()
    await ctx.send(response)


#I'm a Parade!
@bot.command()
async def parade(ctx):
    await ctx.send(file=discord.File('images/parade.jpg'))

# Zoom Happy Hour Link
@bot.command()
async def happyhour(ctx):
    booze = open('alcohol.txt').read().splitlines()
    random.seed(a=None)
    boozequote = random.choice(booze)
    response = open('zoom.txt').read()
    await ctx.send(response)
    await ctx.send(boozequote)

@bot.command()
async def bunker(ctx,args):
    codes = ['Prison shack code: 72948531',
             'Farmland code: 49285163',
             'South Junkyard: 97264138',
             'North Junkyard: 87624851',
             'Park - 60274513',
             'TV Station - 27495810']
    location = ['Bunker 1: Located near the dam. Climb the hill located near the dam and search for the bunker in the surroundings.',
                'Bunker 2: Take the western road fo the map. Keep looking on the left for a small stone building. The bunker is located inside the stone building.',
                'Bunker 3: This bunker is just next to the second bunker location. There are similar stone houses. Inspect each and find two bunkers from them.', 
                'Bunker 4: Follow the Kart Track and keep looking on the left. Just like bunker 2 and 3, you need to spot a small stone house. That will lead you to bunker 4.',
                'Bunker 5: Located in the Southern part of the map. Look for a rocky path at the end of the cliffs. The rocky path will lead you to bunker 5.', 
                'Bunker 6: Reach the “park” and move towards the border of the map. Try and look for a stone building where the bunker 6 is located',
                'Bunker 7: Start walking towards the Northeast side of the Prison. Follow the moat and look for the bunker 7 along the cliffside.',
                'Bunker 8: Reach the Northeast side of the stadium. A small "construction site" will be spotted. Inspect the stone houses there for bunker 8.',
                'Bunker 9:  Inspect the stone houses near bunker 8. Bunker 9 should be in one of the houses just like the previous one.', 
                'Bunker 10: Start moving towards the east of the quarry. You might spot a blocked-off tunnel with train tracks by the end of the map. Bunker 10 is located above it.'
                ]
    #if arg == codes:
    #response =

    #await ctx.send(response)

# Urbandictionary
@bot.command()
async def urban(self, ctx, *, search_terms: str, definition_number: int=1):
    """Get an Urban Dictionary entry."""
    search_terms = search_terms.split(" ")
    try:
        if len(search_terms) > 1:
            pos = int(search_terms[-1]) - 1
            search_terms = search_terms[:-1]
        else:
            pos = 0
        if pos not in range(0, 11):
            pos = 0
    except ValueError:
        pos = 0
    search_terms = "+".join(search_terms)
    url = "http://api.urbandictionary.com/v0/define?term=" + search_terms
    try:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                result = json.loads(await r.text())
                if result["list"]:
                    definition = result['list'][pos]['definition']
                    example = result['list'][pos]['example']
                    defs = len(result['list'])
                    embed = discord.Embed(title='Definition #{} out of {}'.format(pos + 1, defs), description=definition, colour=embedColor(self))
                    embed.set_author(name=search_terms, icon_url='https://i.imgur.com/bLf4CYz.png')
                    embed.add_field(name="Example:", value=example, inline=False)
                    await edit(ctx, embed=embed)
                else:
                    await edit(ctx, content="Your search terms gave no results.", ttl=3)
    except IndexError:
        await edit(ctx, content="There is no definition #{}".format(pos + 1), ttl=3)
    except:
        await edit(ctx, content="Error.", ttl=3)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

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

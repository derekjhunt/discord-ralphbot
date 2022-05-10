import discord
from discord.ext import commands
import random
import aiohttp
import json

class Urban(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

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

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Urban(bot)) # add the cog to the bot
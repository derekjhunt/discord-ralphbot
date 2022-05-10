import discord
from discord.ext import commands
import random
import wikiquote

class Heinlein(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def heinlein(self, ctx):
        """"""
        response = random.choice(wikiquote.quotes('Robert A. Heinlein'))
        response_a = "Robert A. Heinlein: " + response
        await ctx.send(response_a)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Heinlein(bot)) # add the cog to the bot

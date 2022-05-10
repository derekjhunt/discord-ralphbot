import discord
from discord.ext import commands
import random
import wikiquote

class Qotd(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    # Answers with the Quote of the day
    async def qotd(self, ctx):
        response = wikiquote.quote_of_the_day()
        await ctx.send(response)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Qotd(bot)) # add the cog to the bot
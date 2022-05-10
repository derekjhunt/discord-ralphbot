import discord
from discord.ext import commands
import random
import wikiquote

class Trump(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    #Answers with a random quote
    async def trump(self, ctx):
        """Pulls a random quote from an insane, treasonous wannabe dictator."""
        response = random.choice(wikiquote.quotes('Donald Trump'))
        response_a = "Donald J. Trump: " + response
        await ctx.send(response_a)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Trump(bot)) # add the cog to the bot

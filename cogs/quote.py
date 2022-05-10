import discord
from discord.ext import commands
import random
import wikiquote
import string

class Quote(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def quote(self, ctx, arg):
        """Pulls a random quote from WikiQuote. Example: !quote "George Washington" """
    #    try:
        response = random.choice(wikiquote.quotes(string.capwords(arg)))
        #except wikiquote.DisambiguationPageException as e:
        #  s = random.choice(e.options)
        #  response = wikiquote.quotes(s)
        arg = arg.replace('"', '')
        response_a = string.capwords(arg) + ": " + response
        await ctx.send(response_a)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Quote(bot)) # add the cog to the bot

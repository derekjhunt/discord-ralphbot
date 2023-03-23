import discord
from discord.ext import commands

class There(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def there(self, ctx):
        """There, They're, Their"""
        await ctx.send("there: a location. Think of (where) with the first letter changed.")
        await ctx.send("they're: a contraction of the words (they are). The apostrophe is your signal that the word can be split into two words.")
        await ctx.send("their: possessive, the thing belonging to them. Take the (t) off, and you have (heir). What does an heir inherit? Something now belonging to them!")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(There(bot)) # add the cog to the bot
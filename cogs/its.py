import discord
from discord.ext import commands

class Its(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def its(self, ctx):
        """Its, It's"""
        await ctx.send("it's: like you're and they're, this is a contraction, in this case of the words (it is). It is not a possessive apostrophe like the ones you see after nouns. This apostrophe is your signal that the word can be split into two words.")
        await ctx.send("its: possessive, the thing belonging to it. Remember it by thinking of the other form, and ask yourself, Can I break this into two words (it is) in this sentence? If the answer is no, you don't want an apostrophe. Put the apostrophe down, and walk away from the its.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Its(bot)) # add the cog to the bot
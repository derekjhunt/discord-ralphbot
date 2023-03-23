import discord
from discord.ext import commands

class Your(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def your(self, ctx):
        """Your, You're"""
        await ctx.send("your: possessive, the thing belonging to you. See how it ends in (our)? Use that as a reminder. When it belongs to us, it's our thing. When it belongs to you, it's your thing.")
        await ctx.send("you're: a contraction of the words (you are). The apostrophe is your signal that the word can be split into two words.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Your(bot)) # add the cog to the bot
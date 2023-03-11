import imp
import discord
from discord.ext import commands
import os
import random
import praw

# Image directory
#images = os.path.join(os.getcwd(), "images")

class Actually(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def actually(self, ctx):
        """Ackchyually"""
        await ctx.send(file=discord.File('images/actually.png'))


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Actually(bot)) # add the cog to the bot
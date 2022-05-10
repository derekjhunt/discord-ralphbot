import discord
from discord.ext import commands
import os
import random

class Ralph(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def ralph(self, ctx):
        directory_path = os.getcwd()
        responses = open(directory_path + '/ralph.txt').read().splitlines()
        random.seed(a=None)
        response = random.choice(responses)
        await ctx.send(response)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Ralph(bot)) # add the cog to the bot
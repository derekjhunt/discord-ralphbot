import discord
from discord.ext import commands
import random
import os

class Happyhour(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def happyhour(self, ctx):
        directory_path = os.getcwd()
        booze = open(directory_path + '/alcohol.txt').read().splitlines()
        random.seed(a=None)
        boozequote = random.choice(booze)
        response = open(directory_path + '/zoom.txt').read()
        await ctx.send(response)
        await ctx.send(boozequote)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Happyhour(bot)) # add the cog to the bot
import imp
import discord
from discord.ext import commands
import os
import random
import praw

# RLM directory
images = os.path.join(os.getcwd(), "rlm")

class Rlm(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def rlm(self, ctx):
        """Posts a random RLM reference, meme or a wild Rich Evans"""
        await ctx.send('Oh My God!', file=discord.File(select_random_image_path()))

def select_random_image_path():
    return os.path.join(images, random.choice(os.listdir(images)))

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Rlm(bot)) # add the cog to the bot
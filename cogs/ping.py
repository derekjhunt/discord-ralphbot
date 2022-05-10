import discord
from discord.ext import commands

class Ping(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    #answers with the ms latency
    async def ping(self, ctx):
        """"Shows the latency of the bot."""
        await ctx.send(f'Pong! {round (bot.latency * 1000)}ms ')

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Ping(bot)) # add the cog to the bot
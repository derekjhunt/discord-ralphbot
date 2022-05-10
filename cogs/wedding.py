import discord
from discord.ext import commands

class Wedding(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def wedding(self, ctx):
        """TaKeN's Wedding!"""
        await ctx.send("October 10th, you stupid cunt. Check your :calendar:. Also, don't be cheap: https://paypal.me/pools/c/8joQUEB901")
        await ctx.send("And they lived happily ever after.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Wedding(bot)) # add the cog to the bot
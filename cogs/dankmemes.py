import discord
from discord.ext import commands
import random
import praw

reddit = praw.Reddit("ralphbot", user_agent='script:RalphBot:v0.0.1 by u/Azathot')

class DankMemes(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def dankmemes(self, ctx):
        memes_submissions = reddit.subreddit('dankmemes').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(DankMemes(bot)) # add the cog to the bot
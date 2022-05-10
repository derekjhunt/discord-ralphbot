import discord
from discord.ext import commands
import requests
import os

directory_path = os.getcwd()

WEATHER_API = open(directory_path + "/weather_api.txt","r").readline()

class Weather(commands.Cog): 
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # create a command

    async def weather(self, ctx, arg1):
        #arg = message.content[slice(9, len(message.content))].lower()
        result = get_weather(arg1)
        await ctx.send(embed=result)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Weather(bot)) # add the cog to the bot

# Weather - for Fuzzybabyducks
def get_weather(city):
    try:
        weather_base_url = "http://api.weatherapi.com/v1/current.json?key=" + WEATHER_API
        complete_url = weather_base_url + "&q=" + city
        response =  requests.get(complete_url) 
        result = response.json()

        city = result['location']['name']
        country = result['location']['country']
        time = result['location']['localtime']
        wcond = result['current']['condition']['text']
        wind_mph = result['current']['wind_mph']
        icon = result['current']['condition']['icon']
        humidity = result['current']['humidity']
        ccoverage = result['current']['cloud']
        celcius = result['current']['temp_c']
        fahrenheit = result['current']['temp_f']
        fclike = result['current']['feelslike_c']
        fflike = result['current']['feelslike_f']

        embed=discord.Embed(title=f"{city}"' Weather', description=f"{country}", color=0x14aaeb)
        embed.add_field(name="Temprature C°", value=f"{celcius}", inline=True)
        embed.add_field(name="Temprature F°", value=f"{fahrenheit}", inline=True)
        embed.add_field(name="Wind Condition", value=f"{wcond}", inline=True)
        embed.add_field(name="Wind MPH", value=f"{wind_mph}", inline=True)
        embed.add_field(name="Humidity %", value=f"{humidity}", inline=True)
        embed.add_field(name="Cloud Coverage %", value=f"{ccoverage}", inline=True)
        embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
        embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
        embed.set_footer(text='Time: 'f"{time}")
        embed.set_thumbnail(url="https:" + icon)

        return embed
    except:
        embed=discord.Embed(title="No response", color=0x14aaeb)
        embed.add_field(name="Error", value="Oops!! Please enter a city name", inline=True)
        return embed
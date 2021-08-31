import discord
from discord.ext import commands
import requests
import json 

def get_quote() :
    res = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(res.text)
    quote = json_data[0]['q'] + "  \n-" + json_data[0]['a']
    return quote


class Quotes(commands.Cog):

    def __init__(self,client):
        self.client = client

    #command
    @commands.command()
    async def zenquote(self,ctx):
        message = get_quote()
        await ctx.send(message)


def setup(client):
    client.add_cog(Quotes(client))
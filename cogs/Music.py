import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

class Music(commands.Cog) :

    def __init__(self,client):
        self.client = client

    #command
    @commands.command(pass_context = True)
    async def join(self,ctx):
        channel = ctx.author.voice.channel
        await ctx.send(f'Joined {channel}')
        await channel.connect()



def setup(client):
    client.add_cog(Music(client))
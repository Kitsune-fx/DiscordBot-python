import discord
from discord import channel
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

    @commands.command(pass_context = True)
    async def leave(self,ctx):
        await ctx.send(f'Leaved bye!')
        await ctx.voice_client.disconnect()



def setup(client):
    client.add_cog(Music(client))
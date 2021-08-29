from os import name
import discord
from discord.ext import commands

class Info(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    
    #command
    @commands.command()
    async def serverinfo(self,ctx):
        serverName = ctx.guild.name
        serverId = ctx.guild.id
        memCount = ctx.guild.member_count
        mbed = discord.Embed(
            color = discord.Colour(0xffff),
            title = f'Server Info'
        )
        mbed.add_field(name='Server Name',value=f'{serverName}',inline=False)
        mbed.add_field(name='Server id',value=f'{serverId}',inline=False)
        mbed.add_field(name='Member Count',value=f'{memCount} ',inline=False)
        mbed.set_image(url=f'{ctx.guild.icon_url}')
        await ctx.send(embed = mbed)

    @commands.command()
    async def myinfo(self,ctx):
        mbed = discord.Embed(
            color = discord.Colour(0xffff),
            title = f"{ctx.author}" 
        )
        mbed.set_image(url=f'{ctx.author.avatar_url}')
        
        await ctx.send(embed = mbed)

    @commands.command()
    async def userinfo(self,ctx,user: discord.Member):
        mbed = discord.Embed(
            color = discord.Colour(0xffff),
            title = f"{user}" 
        )
        mbed.set_image(url=f'{user.avatar_url}')
    
        await ctx.send(embed = mbed)

def setup(client):
    client.add_cog(Info(client))

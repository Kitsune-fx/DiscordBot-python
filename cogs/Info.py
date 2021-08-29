from os import name
import discord
from discord.ext import commands

class Info(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    
    #command
    @commands.command()
    async def serverinfo(self,ctx):
        await ctx.send(f'Server name: {ctx.guild.name} \nServer id: {ctx.guild.id} \nMember count: {ctx.guild.member_count} members')

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

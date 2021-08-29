import discord
from discord.ext import commands

class CheckPrime(commands.Cog):
    def __init__(self,client):
        self.client = client

    #command
    @commands.Command
    async def checkprimenum(self,ctx,num : int):
        result = ''
        count = 2
        if num <= 1 :
            result = f'{num} is not prime number number.'
        else: 
            while count < num:
                if num%count == 0:
                    result = f'{num} is not prime number.'
                    break
                else:
                    result = f'{num} is prime number.'
                count += 1

        await ctx.send(result)

def setup(client):
    client.add_cog(CheckPrime(client))

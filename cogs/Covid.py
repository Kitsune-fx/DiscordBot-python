import discord
from discord.ext import commands
import requests
import json 

def get_covid() :
    res = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
    r_dict = res.json()
    date = r_dict[0]['update_date']
    newCase = r_dict[0]['new_case']
    totalCase = r_dict[0]['total_case']
    totalDeath = r_dict[0]['total_death']
    totalRecover = r_dict[0]['total_recovered']
    return_result = f"Date: {date} \nNew case: {newCase}   Total case: {totalCase}\nTotal death: {totalDeath} Total recover: {totalRecover} "
    return return_result
    


class CovidStatus(commands.Cog):

    def __init__(self,client):
        self.client = client

    #command
    @commands.command()
    async def Covidtoday(self,ctx):
        message = get_covid() 
        await ctx.send(message)


def setup(client):
    client.add_cog(CovidStatus(client))
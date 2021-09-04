import discord
from discord import message
from discord.ext import commands
import requests
import json 

def covid_province(name):
    res2 = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces")
    r_dict2 = res2.json()
    for i in range(77):
        if(r_dict2[i]['province'] == name):
            index = i
    province = r_dict2[index]['province']      
    p_date = r_dict2[index]['update_date']
    p_newCase = r_dict2[index]['new_case']
    p_totalCase = r_dict2[index]['total_case']
    p_totalDeath = r_dict2[index]['total_death']  
    result = f"Covid-19 case in {province}   Date: {p_date} \nNew case: {p_newCase}   Total case: {p_totalCase}\nTotal death: {p_totalDeath} "
    return result

class CovidStatusInProvince(commands.Cog):
    def __init__(self,client):
        self.client = client

    #command    
    @commands.command()
    async def Covidin(self,ctx,*,province):
        message = covid_province(province)
        await ctx.send(message)


def setup(client):
    client.add_cog(CovidStatusInProvince(client))
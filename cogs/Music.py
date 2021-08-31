import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import pafy

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

    @commands.command(pass_context = True)
    async def play(self,ctx,url):
        channel = ctx.message.author.voice.channel
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            'option' : '-vn'    
        }

        voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_client == None:
            await voice.connect()
        else : 
            await voice_client.move_to(channel)
        
        song = pafy.new(url)
        audio = song.getbestaudio()
        await ctx.send("Master I can't play a music for you." )
        # source = await FFmpegPCMAudio(audio.url,**FFMPEG_OPTIONS)
        #FFmpeg cant work idk HOW and WHY I'll try to fix it later lol  
        # voice_client.play(source) 



def setup(client):
    client.add_cog(Music(client))
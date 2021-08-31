import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

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

        YDL_OPTION ={'format':'bestaudio','noplaylist':'True'}
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            'option' : '-vn'    
        }

        with YoutubeDL(YDL_OPTION) as ydl:
            info = ydl.extract_info(url , download=False)
        
        URL = info['formats'][0]['url']
        client.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))




def setup(client):
    client.add_cog(Music(client))
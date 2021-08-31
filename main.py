import discord
import os
from discord.ext import commands


#Put your token down here.
token = 'ODcwNjIyNjY3MzgyODc4MjA4.YQPciw.xmIWWCdSz4qIjOYePnG40LU88fA'

client = commands.Bot(command_prefix = '$')

#event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Aim to the moon!"))
    print('I am ready master.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("I don't understand the order master.")


#command
@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cog.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
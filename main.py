import discord

client = discord.Client()

@client.event
async def on_ready():
    print("I am online master.")

client.run('ODcwNjIyNjY3MzgyODc4MjA4.YQPciw.VcdgQChyEEMH6hTrFPBsBV9XFac')
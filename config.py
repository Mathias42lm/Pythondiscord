import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="/")
@client.event
async def on_ready():
    print("ready")


@client.command(aliases=['aaa'])
async def nuke(ctx,nb=1):
    id = ctx.message.guild.id
    server = client.get_server(id)
    print(id)

@client.command(aliases=['clean'])
async def clear(ctx,nb=1):
    nb=nb+1
    if nb>101:
        await ctx.send("il faut en faire moin")
    else:
        await ctx.channel
        await ctx.send("Ok supr")




client.run("OTY5OTk1NjY5MzI0NTkxMTg1.GT8jIm.LvWkdnw9GGJA7XnR9hRT-LtDUwGWNqqqlH76ts")
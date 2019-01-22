#Bot Created By Xenomt
#First import discord.py and some module
import random
import asyncio
import aiohttp
import json
import discord
import time
from itertools import cycle
from discord import Game
from discord.ext import commands
from  discord.ext.commands import Bot

TOKEN = "" #Put your token here

client = commands.Bot(command_prefix = ".g") #Put your command prefix here
client.remove_command("help")


####################################################################################################
#Account Generator

#Gen Spotify, you can change
@client.command(pass_context=True)
@commands.cooldown(1, 86400, commands.BucketType.user) # Put your cooldown in second
async def spotify(ctx): #spotify = command name, ex: .gspotify if u change spotify in uplay u will get .guplay
    author = ctx.message.author
    with open("spotify.txt", "r") as acc_spo: #create a account txt file like spotify.txt or uplay.txt in the same directory
        for i in range(random.randint(0, 2000)): #select the number of line of your dumps
            text_spo = acc_spo.readline()
        await client.send_message(author, text_spo)
        #The account will send in mp message

@client.event
async def on_command_error(error,ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(ctx.message.channel, content="This command is on a "+ str(round(error.retry_after / 60 / 60, 2)) +" h cooldown" ) # Don't need to explain that if u not dumb
 raise error

@client.event
async def on_ready():
    print("Bot is ready.")
    print("I'm running on " + client.user.name)
    print("With the ID: " + client.user.id)
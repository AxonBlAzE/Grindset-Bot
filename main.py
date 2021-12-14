import discord
import os
from music import Music 
from grind import Grind
import asyncio

my_secret = os.environ['myToken']
client = discord.Client()
voice = None
music = Music(client)
mygrind = Grind(client)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello-world'):
        await message.channel.send('Hello World')

    if message.content.startswith('!creators'):
        await message.channel.send('Shreyans Mulkutkar and Pratik Thakare')

    if message.content.startswith('!grindset'):
        # grab the user who sent the command
        user=message.author
        voice_channel=user.voice.channel
        
        # only play music if user is in a voice channel
        if voice_channel != None:
            # grab user's voice channel
            await message.channel.send('User is in channel: '+ voice_channel.name)

            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('Grindset.mp3'), after=lambda e: print('done', e))
        else:
            await message.channel.send('User is not in a channel.')

client.run(my_secret)
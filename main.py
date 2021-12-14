import discord
import os
from music import Music 
from grind import Grind

my_secret = os.environ['myToken']
client = discord.Client()
voice = None
music = Music(client)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!creators'):
        await message.channel.send('Shreyans Mulkutkar and Pratik Thakare')
    
    if message.content.startswith('!grindset'):
        voice = discord.VoiceClient(client, message.author)
        await message.channel.send('Sigma rule #0: turn that mindset into grindset')
        grind.play(message)
        # music.play()
        # await message.channel.send(file=discord.File('Grindset.mp3'))

client.run(my_secret)

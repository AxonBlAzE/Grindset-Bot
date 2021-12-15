import discord
import os
from music import Music 
from replit import db
from keep_alive import keep_alive

keep_alive()
my_secret = os.environ['myToken']
client = discord.Client()
voice = None
music = Music(client)

async def get_rule(n):
    # rule = db[n]
    if n not in db.keys():
      rule = "```There is no such rule```"
    else:
      rule = "```Sigma Rule #" + str(n) + ": " + db[n] + "```"
    return rule


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
      await message.channel.send("```Shreyans Mulkutkar and Pratik Thakare```")

    if message.content.startswith('!grindset'):
      # grab the user who sent the command
      user=message.author
      voice_channel=user.voice.channel
      
      # only play music if user is in a voice channel and bot is not in the voice channel
      if voice_channel != None:
          # grab user's voice channel

        await message.channel.send('```Sigma Rule #0: Turn that Mindset into Grindset```')

        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('Grindset.mp3'), after=lambda e: print('', e))
      
      # only play music if user is and the bot is already in a voice channel
      elif voice_channel == user.voice.channel:
        vc.play(discord.FFmpegPCMAudio('Grindset.mp3'), after=lambda e: print('', e))
        
      else:
        await message.channel.send('User is not in a channel.')
    
    if message.content.startswith('!rules'):
      s = db.keys()
      l = list(s)
      l.sort()
      for keys in l:
        # print(l)
        await message.channel.send("```Sigma Rule #" + str(keys) + ": " + db[keys] + "```")

    if message.content.startswith('!rule#'):
      n = message.content.split('#')[1]
      rule = await get_rule(n)
      await message.channel.send(rule)


    
client.run(my_secret)
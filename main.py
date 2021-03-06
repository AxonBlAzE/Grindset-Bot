import discord
import os
import random
from replit import db
from keep_alive import keep_alive
from meme_generator import MemeGenerator


keep_alive()
my_secret = os.environ['myToken']
bot = discord.Client()
voice = None
audio = discord.FFmpegPCMAudio('Grindset.mp3')


async def get_rule(n):
    # rule = db[n]
    if n not in db.keys():
        rule = "```There is no such rule```"
    else:
        rule = "```Sigma Rule #" + str(n) + ": " + db[n] + "```"
    return rule

async def generateMeme(ctx, meme_name, top_text, bottom_text=" "):
    meme_generator = MemeGenerator()
    meme_generator.generate_meme(meme_name, top_text, bottom_text)
    await ctx.channel.send(file=discord.File(meme_generator.memes_folder_path + 'meme_edited.jpg'))

async def disconnect(message):
    voice = message.guild.voice_client
    if voice:
        await voice.disconnect()
        await message.channel.send('Sigma Bot Disconnected')
    else:
        await message.channel.send('Bot needs to be connected to voice first')
        
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello-world'):
        await message.channel.send('Hello World')

    if message.content.startswith('!creators'):
        await message.channel.send(
            "```Shreyans Mulkutkar and Pratik Thakare```")

    #doest work
    # if message.content.startswith('!grindset'):
    #     user_voice = message.author.voice
    #     if not user_voice:
    #         await message.channel.send("You need to be connected in a voice channel to use this command!")
    #         return

    #     # This allows for more functionality with voice channels
    #     voice = discord.utils.get(bot.voice_clients, guild=message.guild)
        
    #     # None being the default value if the bot isnt in a channel (which is why the is_connected() is returning errors)
    #     if voice == None:
    #         voice = await user_voice.channel.connect()
        
    #     voice.play(
    #         audio,
    #         after=lambda e: disconnect(message)
    #     )

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
            await message.channel.send("```Sigma Rule #" + str(keys) + ": " +
                                       db[keys] + "```")

    if message.content.startswith('!rule#'):
        n = message.content.split('#')[1]
        rule = await get_rule(n)
        await message.channel.send(rule)


    if message.content in ('!disconnect', '-dc'):
        await disconnect(message)
        
    if message.content.startswith('!meme:'):
      n = random.randint(1,4)
      meme_name = 'chad'+str(n)
      top_text = 'Sigma Rule #' + str(random.randint(1, 1000))
      bottom_text = message.content.split(':')[1]
      await generateMeme(message, meme_name, top_text, bottom_text)
  
bot.run(my_secret)

import discord
import os
from discord.ext import commands

class Grind:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx):
        url = "https://www.youtube.com/watch?v=wLz9xU6J88k"
        if ctx.voice_client is None:
            await ctx.send("You are not connected to a voice channel")
        else:
            player = await YTDLSource.from_url(url)
            ctx.voice_client.play(player)
            vc = ctx.voice_client
            vc.play(player)
            await ctx.send("Playing")
        
    @commands.command()
    async def grindset(self, ctx):
        voice = discord.VoiceClient(self.client, ctx.author)
        await ctx.send('Sigma rule #0: turn that mindset into grindset')
        await self.play(ctx)
        # await ctx.send(file=discord.File('Grindset.mp3'))
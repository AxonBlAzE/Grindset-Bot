import discord
import os
from discord.ext import commands
import youtube_dl

class music:
    def __init__(self,client) -> None:
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You are not connected to a voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("You are not connected to a voice channel")
        else:
            await ctx.voice_client.disconnect()

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

def setup(client):
    client.add_cog(music(client))

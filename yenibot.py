import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
#sesin çalismasi icin "pip install PyNaCl" komutunu kullan

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("Hazir")
@client.command()
async def help(msg):
    await msg.send("!help yazılınca burası calisior")


@client.command(pass_context = True)
async def cal(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Herhangi Bir ses kanalında değilsin!")
    else:
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            source = FFmpegPCMAudio("Muzık Dosyası Yolu")
            player = voice.play(source)

@client.command(pass_context = True)
async def zzz(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("cikti")
    else:
        await ctx.send("Hata")




client.run("TOKEN")



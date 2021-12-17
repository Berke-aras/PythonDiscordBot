import discord
from discord.ext import commands, tasks
from functions import *
import os
import random
from random import randint as r


INSTAGRAM = "https://instagram.com/"
TWITTER = "https://twitter.com/"
YOUTUBE = "https://youtube.com/"


ext_file_types = ["png", "jpg", "jpeg", "gif"]


intents = discord.Intents(messages=True, guilds=True, reactions= True, members=True, presences=True)
Bot = commands.Bot(command_prefix=".",intents=intents)



@Bot.event              # Game ,Streaming(url eklenmeli)   Bot.change_presence(activity=discord.Streaming(name="Deneme",url="https://www.twitch.tv/berke_v"))
async def on_ready():                                                            #watching
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))
    uyarı.start()
    SosyalMedya.start()
    print("Ben Hazırım")


@Bot.event
async def on_member_join(member):
    channel= discord.utils.get(member.guild.text_channels, name="HANGİ KANALSA YAZ")
    await channel.send((f"{member.mention} aramıza Hoş Geldin 💕"))

@Bot.event
async def on_member_remove(member):
    channel= discord.utils.get(member.guild.text_channels, name="HANGİ KANALSA YAZ")
    await channel.send((f"{member.mention} aramızdan ayrıldı 🙁"))



@tasks.loop(seconds=990)
async def SosyalMedya():
    for c in Bot.get_all_channels():
        if c.id == "İSTENEN KANAL İD Sİ İNT OLARAK":
            await c.send(f"{INSTAGRAM}\n{TWITTER}\n{YOUTUBE}")

@tasks.loop(seconds=600)
async def uyarı():
    for c in Bot.get_all_channels():
        if c.id == "İSTENEN KANAL İD Sİ İNT OLARAK":
            await c.send("SAYGI")

@Bot.command()
async def zar(ctx):
    a = r(1, 7)
    await ctx.send(a)



@Bot.command(aliases=["temizle","cl"])
@commands.has_role("KOMUT YETKİLİSİ")
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)


@Bot.command(aliases=["copy","kopyala"])
@commands.has_role("KOMUT YETKİLİSİ")
async def clone_channel(ctx, amount=1):
    for i in range(amount):
        await ctx.channel.clone()


@Bot.command(aliases=["at"])
@commands.has_role("KOMUT YETKİLİSİ")
async def kick(ctx, member:discord.Member, *, reason="Yok"):
    await member.kick(reason=reason)

@Bot.command(aliases=["engelle"])
@commands.has_role("KOMUT YETKİLİSİ")
async def ban(ctx, member:discord.Member, *, reason="Yok"):
    await member.ban(reason=reason)


@commands.command(aliases=["çekiliş","çek"])
@commands.has_role("KOMUT YETKİLİSİ")
async def raffle(self, ctx):
    await ctx.send(random.choice(self.bot.guilds[0].members))

   
@Bot.command(aliases = ["ban_aç","ban_kaldır","engel_aç"])
@commands.has_role("KOMUT YETKİLİSİ")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")


@Bot.command(aliases = ["havalı"])
async def react(ctx):
    await ctx.message.add_reaction("😎")


@Bot.command()
async def myavatar(ctx):
    filename = "avatar1.jpg"
    await ctx.author.avatar_url.save(filename)
    file = discord.File(fp=filename)
    await ctx.send("Enjoy :>", file=file)



Bot.run("TOKEN")

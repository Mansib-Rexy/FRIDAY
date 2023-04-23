
import discord
import os
import io
from io import BytesIO
from typing import Union
import time
import asyncio
import re
import requests

import aiohttp
from aiohttp import request
import praw
import time
import aiohttp
import discord.ext
import random
import datetime
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import youtube_dl
import time
import os
from replit import db
import shutil
from discord.ext.commands import clean_content

funresponses = None
from discord.ext import commands
from langcodes import Language
from discord import DMChannel, GroupChannel
import langcodes
import pytz
from gtts import gTTS
from bs4 import BeautifulSoup

from discord.ext import tasks


import colour
from colour import Color
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check,clean_content
import os
from PIL import ImageColor

from discord.ext import tasks 
import json as j
json = j



import OpenAi


async def my_task():
    while True:
      guild = discord.utils.get(client.guilds, name='The Strangers')
      role1 = discord.utils.find(lambda r: r.name == 'lvl 5',guild.roles)
      role2 = discord.utils.find(lambda r: r.name == 'lvl 10',guild.roles)
      role3 = discord.utils.find(lambda r: r.name == 'lvl 20',guild.roles)
      role4 = discord.utils.find(lambda r: r.name == 'lvl 30',guild.roles)
      role5 = discord.utils.find(lambda r: r.name == 'lvl 40',guild.roles)
      role6 = discord.utils.find(lambda r: r.name == 'lvl 50',guild.roles)
      role7 = discord.utils.find(lambda r: r.name == 'lvl 60',guild.roles)        
      role8 = discord.utils.find(lambda r: r.name == 'lvl 70',guild.roles)
      role9 = discord.utils.find(lambda r: r.name == 'lvl 80',guild.roles)
      role10 = discord.utils.find(lambda r: r.name == 'lvl 90',guild.roles)
      for user in guild.members:   
       if role2 in user.roles:
         await asyncio.sleep(3)
         await user.remove_roles(role1)
       if role3 in user.roles:
         await asyncio.sleep(3)
         await user.remove_roles(role2,role1)
       if role4 in user.roles:   
         await asyncio.sleep(3)
         await user.remove_roles(role3,role2,role1)
       if role5 in user.roles:
         await asyncio.sleep(3)
         await user.remove_roles(role4,role3,role2,role1)
       if role6 in user.roles:
         await asyncio.sleep(3)
         await user.remove_roles(role5,role4,role3,role2,role1)
       if role7 in user.roles:
         await asyncio.sleep(3)
         await user.remove_roles(role6, role5, role4,role3,role2,role1) 
       if role8 in user.roles:
         await asyncio.sleep(3)
         await user.remove_roles(role7,role6,role5,role4,role3,role2,role1)
       if role9 in user.roles:
           await asyncio.sleep(3)
           await user.remove_roles(role8,role7,role6,role5,role4,role3,role2,role1)
       if role10 in user.roles:
          await asyncio.sleep(3)
          await user.remove_roles(role9,role8,role7,role6,role5,role4,role3,role2,role1)   
      
        
      await asyncio.sleep(60*1)
      print("refreshed")
    






hugs = [
    "https://c.tenor.com/oPIi24wF8ucAAAAM/hug-virtual-hug.gif",
    "https://c.tenor.com/wqCAHtQuTnkAAAAM/milk-and-mocha-hug.gif",
    "https://c.tenor.com/DxMIq9-tS5YAAAAM/milk-and-mocha-bear-couple.gif",
    "https://c.tenor.com/jX1-mxefJ54AAAAM/cat-hug.gif",
    "https://c.tenor.com/qj_wTx9dXVMAAAAM/cat-hug.gif",
    "https://c.tenor.com/6gFGYzv0dYkAAAAM/hug-dog.gif",
    "https://c.tenor.com/FM_386i6588AAAAM/dog-cat.gif",
    "https://c.tenor.com/9GDtH6bknsIAAAAM/i-love-you-dog.gif",
    "https://c.tenor.com/XyECfmRs0KMAAAAM/virtual-hug.gif"
]
loves = [
    "https://media.discordapp.net/attachments/783547639944839182/829669846676668416/bucket_of_love.jpg?width=427&height=427",
    "https://media.discordapp.net/attachments/783547639944839182/829669984274743306/wholesome.jpg?width=474&height=427"
]

intents = discord.Intents.all()


client = discord.Client(intents = intents)

client = commands.Bot(
    command_prefix=[",cr ", ",", "jarvis ", "friday ", "Friday ", "Jarvis "],
    intents=intents)


@client.command(help="see a users pfp clearly", aliases=["av", "pfp"])
async def avatar(ctx, *, member: discord.Member = None):
    if member == None:
        await ctx.send(ctx.author.avatar_url)
    url = member.avatar_url
    await ctx.send(url)


@client.command()
async def sup(ctx):
    await ctx.send("hello and wassup? Hope you're having a wonderful day")


@client.command()
async def free_nitro(ctx):
    embed = discord.Embed(
        description=
        "Never gonna give you up, never gonna let you down. Never gonna run around and desert you 🎵",
        color=discord.Color.random())
    embed.set_image(
        url="https://c.tenor.com/hTzv4T-zpjsAAAAM/hd-rick-rickroll-hd.gif")
    await ctx.send(embed=embed)


@client.event
async def on_ready():
    print("I'm alive")
    client.loop.create_task(my_task())
    await client.change_presence(activity=discord.Streaming(
        name="🤍💙", since=0.0, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                                 )


token = os.getenv("token")


@client.command()
async def hi(ctx):
    await ctx.send(
        f"hi and wassup {ctx.author.mention} hope you are having an awesome day!"
    )


@client.command()
async def gae(ctx):
    e = discord.Embed(description="im happy", color=discord.Color.random())
    e.set_image(
        url=
        "https://cdn.discordapp.com/attachments/783547639944839182/832216386724954122/gae.png"
    )
    await ctx.send(embed=e)


@client.command()
async def disappointment(ctx):
    e = discord.Embed(color=discord.Color.random())
    e.set_image(
        url=
        "https://cdn.discordapp.com/attachments/793108599869931583/832565182110236672/20210416_162929.jpg"
    )
    await ctx.send(embed=e)


@client.command()
async def banner(ctx, user: discord.Member):
    if user == None:
        user = ctx.author
    req = await client.http.request(
        discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.send(f"{banner_url}")


@client.command()
async def good_job(ctx, *, member=None):
    embed = discord.Embed(color=discord.Color.random())
    embed.set_image(
        url=
        "https://cdn.discordapp.com/attachments/793108599869931583/832565426302877726/image0.png"
    )
    await ctx.send(member, embed=embed)


@client.command()
async def WhyAreYouGay(ctx):
    await ctx.send(f"you are gay. {ctx.author.mention} ")


@client.command()
async def howareyou(ctx):
    await ctx.send(
        "i'm doing miserable to be honest. but who cares. its always the same for me. as long as you're doing great, im good "
    )


@client.command()
async def RexysMentalState(ctx):
    await ctx.send("https://c.tenor.com/6j2SVpHkSvQAAAAM/brain-loading.gif")


@client.command()
async def HowLazyAreYou(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/822906813119856720/826461854615339018/Screenshot_20210330-200319_YouTube.jpg"
    )
    await ctx.send(
        "This lazy, even for a bot. well, figures cause rexy coded me. lazy piece of....."
    )


@client.command()
async def hug(ctx, *, member=None):
    embed = discord.Embed(color=discord.Color.random())
    embed.set_image(url=random.choice(hugs))
    if "@everyone" in ctx.message.content or "@here" in ctx.message.content:
        await ctx.send(embed=embed)
    else:
        await ctx.send(member, embed=embed)


@client.command()
async def love(ctx, *, member=None):
    embed = discord.Embed(color=discord.Color.random())
    embed.set_image(url=random.choice(loves))
    await ctx.send(member, embed=embed)


@client.command()
async def k(ctx):
    embed = discord.Embed(title="K", color=discord.Color.random())
    embed.set_image(
        url=
        "https://media.discordapp.net/attachments/783547639944839182/838749309150560276/Annotation_2021-05-03_143007.png"
    )
    await ctx.send(embed=embed)


@client.command()
async def wheres_rexy(ctx):
    await ctx.send(
        f"Most likely studying, having suicidal thoughts, sleeping, napping or listening to music. {ctx.author.mention} "
    )


@client.command()
async def ping(ctx):
    if round(client.latency * 1000) <= 50:
        embed = discord.Embed(
            title="PING",
            description=
            f":gear:  The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
        embed = discord.Embed(
            title="PING",
            description=
            f":gear:  The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0xffd000)
    elif round(client.latency * 1000) <= 200:
        embed = discord.Embed(
            title="PING",
            description=
            f":gear:  The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0xff6600)
    else:
        embed = discord.Embed(
            title="PING",
            description=
            f":gear:  The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0x990000)
    hmm = await ctx.send(
        "https://images-ext-2.discordapp.net/external/uxVz2Dll6MKT1fO_g6v-KQDmpMzltfhUEf99506C91g/https/c.tenor.com/w-_4XMofAt4AAAAM/wait-brb-moment-working-on-it-just-a-moment.gif"
    )
    await asyncio.sleep(3)
    await hmm.edit(content=" ", embed=embed)


@client.command()
async def who_are_you(ctx):
    await ctx.send("I am Iron man")


@client.command(name='spam',
                help=">spam (message amount) (message)",
                hidden=True)
@has_permissions(kick_members=True)
async def spam(ctx, amount: int, *, message):
    for i in range(amount):

        if ctx.author.id != 612928662953656320:
            await asyncio.sleep(0.650)
            await ctx.send(message)


@client.command()
async def punch(ctx, *, member=None):
    embed = discord.Embed(color=discord.Color.random())
    embed.set_image(url="https://c.tenor.com/gIaioChTOloAAAAM/cat-cute.gif")

    if "@everyone" in ctx.message.content or "@here" in ctx.message.content:
        await ctx.send(embed=embed)
    else:
        await ctx.send(member, embed=embed)


@client.command()
async def slap(ctx, *, member=None):
    embed = discord.Embed(color=discord.Color.random())
    embed.set_image(
        url=
        "https://images-ext-1.discordapp.net/external/lkgvxjqPgqmSKd5O_L8RkjG20ddBomZ89M5D35F8hrI/https/c.tenor.com/QhsQeRQypMUAAAAM/slap-bear-slap.gif"
    )
    if "@everyone" in ctx.message.content or "@here" in ctx.message.content:
        await ctx.send(embed=embed)
    else:
        await ctx.send(member, embed=embed)


@client.command(hidden=True)
@has_permissions(kick_members=True)
async def dm(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)





















@client.command(help='>spam_dm (mention user) (amount) (message)', hidden=True)
@has_permissions(kick_members=True)
async def spam_dm(
    ctx,
    user: discord.User,
    amount: int,
    *,
    message=None,
):
    message = message or "the user doesn't know what to message. soooooooooo. idk"
    if ctx.author.id == 0:
        await ctx.send("No fuck off")
    else:
        for i in range(amount):
            await asyncio.sleep(0.650)
            await user.send(message)


client.sniped_messages = {}


@client.event
async def on_message_delete(message):
    if message.attachments:
        bob = message.attachments[0]
        client.sniped_messages[message.guild.id] = (bob.proxy_url,
                                                    message.content,
                                                    message.author,
                                                    message.channel.name,
                                                    message.created_at)
    else:
        client.sniped_messages[message.guild.id] = (message.content,
                                                    message.author,
                                                    message.channel.name,
                                                    message.created_at)


client.edited_messages = {}


@client.event
async def on_message_edit(before, after):
    if before.attachments:
        bob = before.attachments[0]
        client.edited_messages[before.guild.id] = (bob.proxy_url,
                                                   before.content,
                                                   after.content,
                                                   before.author,
                                                   before.channel.name,
                                                   before.created_at)
    else:
        client.edited_messages[before.guild.id] = (before.content,
                                                   after.content,
                                                   before.author,
                                                   before.channel.name,
                                                   before.created_at)


@client.command(aliases=["es"])
async def edit_snipe(ctx):
    try:
        bob_proxy_url, contents, edit_contents, author, channel_name, time = client.edited_messages[
            ctx.guild.id]
    except:
        contents, edit_contents, author, channel_name, time = client.edited_messages[
            ctx.guild.id]
    try:
        embed = discord.Embed(description=contents,
                              color=discord.Color.purple(),
                              timestamp=time)
        embed.set_image(url=bob_proxy_url)
        embed.set_author(name=f"{author.name}>{author.discriminator}",
                         icon_url=author.avatar_url)
        embed.set_footer(text=f"edited : #{channel_name}")
        embed.add_field(name="previous message", value=edit_contents)
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(description=contents,
                              color=discord.Color.purple(),
                              timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}",
                         icon_url=author.avatar_url)
        embed.add_field(name="previous message", value=edit_contents)
        embed.set_footer(text=f"Deleted in : #{channel_name}")
        if ctx.message.author.id == 862729009166417991:
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send("You're not rumi")


@client.command(aliases=["s"])
async def snipe(ctx):
    try:
        bob_proxy_url, contents, author, channel_name, time = client.sniped_messages[
            ctx.guild.id]
    except:
        contents, author, channel_name, time = client.sniped_messages[
            ctx.guild.id]
    try:
        embed = discord.Embed(description=contents,
                              color=discord.Color.purple(),
                              timestamp=time)
        embed.set_image(url=bob_proxy_url)
        embed.set_author(name=f"{author.name}>{author.discriminator}",
                         icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{channel_name}")
        await ctx.channel.send(embed=embed)
    except:
        embed = discord.Embed(description=contents,
                              color=discord.Color.purple(),
                              timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}",
                         icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{channel_name}")
        if ctx.message.author.id == 862729009166417991:
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send("You're not rumi")


@client.command(brief="Random picture of a meow")
async def cat(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://aws.random.cat/meow") as r:
                data = await r.json()
                embed = discord.Embed(title="Meow")
                embed.set_image(url=data['file'])
                embed.set_footer(text="http://random.cat/")
                await ctx.send(embed=embed)


@client.command()
async def bird(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/birb") as r:
                data = await r.json()
                res = str(data)
                hmm = res[10:-2]
                await ctx.send(hmm)


@client.command()
async def dog(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                data = await r.json()
                embed = discord.Embed(title="Good boi")
                embed.set_image(url=data["message"])
                embed.set_footer(text="http://random.dog/")
                await ctx.send(embed=embed)


reddit = praw.Reddit(client_id='O_-j1F6CdVOa0Q',
                     client_secret='	YBDDnzpwFjKlJygRScRprut2kLk03w',
                     username="Rexy_isBored",
                     password="mahin2016",
                     user_agent='Rexy',
                     check_for_async=False)

sent_memes = []
sent_irl = []
sent_wm = []
sent_pics = []
hugged = "<@725465774017478771> <@745674627845587004> <@612928662953656320>"


@client.command()
async def huggles(ctx):
    e = discord.Embed(color=discord.Color.random())
    e.set_image(url=random.choice(hugs))
    await ctx.send(hugged, embed=e)

@client.command()
@has_permissions(kick_members = True)
async def nick(ctx, member: discord.Member,*, nick):
    await member.edit(nick=nick)

@client.command(help="relatable stuff")
async def me_irl(ctx):
    reddit = praw.Reddit(client_id='O_-j1F6CdVOa0Q',
                         client_secret='YBDDnzpwFjKlJygRScRprut2kLk03w',
                         username="Rexy_isBored",
                         password="mahin2016",
                         user_agent='Rexy',
                         check_for_async=False)
    sub_submissions = reddit.subreddit("me_irl").top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sub_submissions if not x.stickied)
    if submission.url in sent_irl:
        return submission
    else:
        e = discord.Embed(title=f'{submission.author}',
                          description=f'{submission.title}',
                          color=discord.Color.random())
        e.set_image(url=submission.url)

        await ctx.send(embed=e)


@client.command(help="cool pictures")
async def pic(ctx):
    reddit = praw.Reddit(client_id='O_-j1F6CdVOa0Q',
                         client_secret='YBDDnzpwFjKlJygRScRprut2kLk03w',
                         username="Rexy_isBored",
                         password="mahin2016",
                         user_agent='Rexy',
                         check_for_async=False)
    sub_submissions = reddit.subreddit("pics").top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sub_submissions if not x.stickied)
    if submission.url in sent_pics:
        return submission
    else:
        e = discord.Embed(title=f'{submission.author}',
                          description=f'{submission.title}',
                          color=discord.Color.random())
        e.set_image(url=submission.url)

        await ctx.send(embed=e)


@client.command(help="ok")
async def meme(ctx):
    reddit = praw.Reddit(client_id='O_-j1F6CdVOa0Q',
                         client_secret='YBDDnzpwFjKlJygRScRprut2kLk03w',
                         username="Rexy_isBored",
                         password="mahin2016",
                         user_agent='Rexy',
                         check_for_async=False)
    sub_submissions = reddit.subreddit("memes").top()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in sub_submissions if not x.stickied)
    if submission.url in sent_pics:
        return submission
    else:
        e = discord.Embed(title=f'{submission.author}',
                          description=f'{submission.title}',
                          color=discord.Color.random())
        e.set_image(url=submission.url)

        await ctx.send(embed=e)


@client.command()
async def dance(ctx):
    embed = discord.Embed(color=discord.Color.random())
    embed.set_image(
        url="https://media.giphy.com/media/11lxCeKo6cHkJy/giphy.gif")
    await ctx.send(embed=embed)


@client.command(
    help=
    ",remind [(time)s,h or d] {for seconds use 's', for minutes use 'm' for hours use 'h' and for days use 'd' (stuff to remind you about)",
    aliases=["remind", "remindme", "remind_me"])
@commands.bot_has_permissions(attach_files=True, embed_links=True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=discord.Color.random())
    embed.set_footer(text="type [,help reminder] if you are having problems",
                     icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(
            name='Warning',
            value=' Dude, specify what do you want me to remind you about.')

    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(
            name='Im sorry wut?',
            value=
            'Please specify a proper duration, send `,help reminder` for more information.'
        )
    if "@everyone" in reminder.lower() or "@here" in reminder.lower():
        await ctx.send("buzz off -_-")

    else:
        await ctx.send(f"Aight, I'll remind you about {reminder} in {counter}."
                       )
        await asyncio.sleep(seconds)
        await ctx.send(
            f"Hi {ctx.author.mention}, you asked me to remind you about {reminder} {counter} ago."
        )
        return
    await ctx.send(embed=embed)


@client.command()
async def shut_down(ctx):
    if ctx.author.id == 647796364205359123:
        await ctx.send("Shutting down in 3.......2.........1")
        await client.logout()
    elif ctx.author.id == 745674627845587004:
        await ctx.send("Shutting down in 3.......2.........1")
        await client.logout()
    else:
        await ctx.send("you're not Rexy or hammmy")


@client.command()
async def wiki(ctx, *, messsage=None):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            link1 = "http://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&formatversion=2&titles=jjj"
            message1 = str(ctx.message.content[5::])
            link2 = link1.replace("jjj", message1)
            async with cs.get(link2) as r:
                data = await r.json()

                res = str(data)
                hmm = res[0:2000]
                hmmm = res[2000::]
                await ctx.send(hmm)
                await ctx.send(hmmm)


@client.command()
async def advice(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.adviceslip.com/advice") as r:
                data = await r.text()
                res = str(data)
                hmm = res[28::]
                await ctx.send(hmm)


@client.command()
async def echo(ctx):
    msg = str(ctx.message.content[6::])
    hmm = await ctx.send(msg)
    await asyncio.sleep(.750)
    await hmm.edit(content=f"‎‎‎‎. {msg}")
    await asyncio.sleep(.750)
    await hmm.edit(content=f"‎‎‎‎.              {msg}")
    await asyncio.sleep(.750)
    await hmm.edit(content=f"‎‎‎‎.                         {msg}")
    await asyncio.sleep(.750)
    await hmm.edit(
        content=f"‎‎‎‎.                                  {msg[0:-1]}")
    await asyncio.sleep(.750)
    await hmm.edit(
        content=f"‎‎‎‎.                                            {msg[0:-2]}"
    )
    await asyncio.sleep(.750)
    await hmm.edit(
        content=
        f"‎‎‎‎.                                                     {msg[0:-3]}"
    )


@client.command()
@has_permissions(kick_members=True)
async def mute(ctx, t, member: discord.Member, *, reason=None):
    guild = ctx.guild

    for role in guild.roles:
        if role.id == 783622936837226529:
            await member.add_roles(role)

            embed = discord.Embed(title="muted!",
                                  description=f"{member.mention} muted ",
                                  colour=discord.Colour.green())
            embed.add_field(name="reason:", value=reason, inline=False)
            embed.add_field(name="time left for the mute:",
                            value=f"{t}",
                            inline=False)
            await ctx.send(embed=embed)
            if t.lower().endswith("s"):
                s = int(t[:-1])
                await asyncio.sleep(s)
            if t.lower().endswith("m"):
                s = int(t[:-1] * 60)
                await asyncio.sleep(s)

            if t.lower().endswith("h"):
                s = int(t[:-1] * 60 * 60)
                await asyncio.sleep(s)

            if t.lower().endswith("d"):
                s = int(t[:-1] * 60 * 60 * 60 * 24)
                await asyncio.sleep(s)

            await member.remove_roles(role)

            embed = discord.Embed(title="unmute (temp) ",
                                  description=f"unmuted -{member.mention} ",
                                  colour=discord.Colour.green())
            await ctx.send(embed=embed)


@client.command(aliases=['mock'])
async def drunkify(ctx, *, s):
    lst = [str.upper, str.lower]
    newText = await commands.clean_content().convert(
        ctx, ''.join(random.choice(lst)(c) for c in s))
    if len(newText) <= 500:
        await ctx.message.delete()
        await ctx.send(newText)
    else:
        await ctx.author.send(newText)
        await ctx.send(
            f"{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:"
        )


@client.command()
async def urban(ctx, *, search):
    word = f"{search}"
    r = requests.get(
        "http://www.urbandictionary.com/define.php?term={}".format(word))
    soup = BeautifulSoup(r.content)
    await ctx.send(
        "------------------------------------------------------                       "
        + soup.find("div", attrs={
            "class": "meaning"
        }).text +
        "     --------------------------------------------------------------------"
    )


@client.command()
async def zakk(ctx):
    e = discord.Embed(description="to be zakk , you have to be",
                      color=discord.Color.random())
    e.set_image(
        url=
        "https://media.discordapp.net/attachments/823483489953382431/842342844152807434/zakk2.png"
    )
    await ctx.send(embed=e)


@client.command()
async def hammy(ctx):
    e = discord.Embed(description="to be hammy , you have to be",
                      color=discord.Color.random())
    e.set_image(
        url=
        "https://media.discordapp.net/attachments/823483489953382431/842342864168026112/hammy2.png"
    )
    await ctx.send(embed=e)


@client.command()
async def ryuk(ctx):
    e = discord.Embed(description="to be ryuk , you have to be",
                      color=discord.Color.random())
    e.set_image(
        url=
        "https://media.discordapp.net/attachments/823483489953382431/842345190349733908/afjahehe.png"
    )
    await ctx.send(embed=e)


@client.command()
async def Rexy(ctx):
    e = discord.Embed(description="to be rexy , you have to be",
                      color=discord.Color.random())
    e.set_image(
        url="https://i.kym-cdn.com/photos/images/facebook/001/328/854/8d6.jpg")
    await ctx.send(embed=e)


IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.datetime.now(IST)


@client.command(aliases=["add"])
@has_permissions(kick_members=True)
async def save(ctx, *, m: str):
    l = ctx.message.attachments
    if l:
      try:
        with open("snippets.json","r+")as f:
           db = json.load(f)
      
        
         
           db = json.loads(db)
           db[f"{m.lower()}"] = f"{l[0].proxy_url}"
           f.seek(0)
           json.dump(json.dumps(db),fp =f)
           await ctx.send(f"Snippet saved as {m.lower()}")
      except Exception as e:
        await ctx.send(str(e))


@client.command(aliases=["snippet", "snip"])
async def _snippet(ctx, *, m):
    with open("snippets.json","r") as f:
      h = json.load(f)
      h = json.loads(h)
      h = h[f"{m}"]
      e = discord.Embed(title=f"{m}", color=discord.Color.random())
      e.set_image(url=h)
      await ctx.send(embed=e)
      
    
    
    
    


@client.command()
async def snippets(ctx):
    m1 = sorted(db.keys())
    m2 = str(m1).replace("}", " ")
    m3 = m2.replace("[", " ")
    m4 = m3.replace("'", " ")
    m5 = m4.replace("]", " ")

    e = discord.Embed(title="List of this servers snippets",
                      color=discord.Color.random())
    e.add_field(name="Snippets", value=m3)
    await ctx.send(m5[0:2000])
    await ctx.send(m5[2000:4000])
    await ctx.send(m5[4000:6000])


@client.command()
async def delete(ctx, *, m):
    if ctx.author.id == 647796364205359123:
        del db[f"{m}"]
        await ctx.send(f"Deleted snippet {m}")
    else:
        await ctx.send("No , cause you're not Rexy ")


@client.command()
async def update(ctx):

    role1 = discord.utils.find(lambda r: r.name == 'lvl 5',
                               ctx.message.guild.roles)
    role2 = discord.utils.find(lambda r: r.name == 'lvl 10',
                               ctx.message.guild.roles)
    role3 = discord.utils.find(lambda r: r.name == 'lvl 20',
                               ctx.message.guild.roles)
    role4 = discord.utils.find(lambda r: r.name == 'lvl 30',
                               ctx.message.guild.roles)
    role5 = discord.utils.find(lambda r: r.name == 'lvl 40',
                               ctx.message.guild.roles)
    role6 = discord.utils.find(lambda r: r.name == 'lvl 50',
                               ctx.message.guild.roles)
    role7 = discord.utils.find(lambda r: r.name == 'lvl 60',
                               ctx.message.guild.roles)
    role8 = discord.utils.find(lambda r: r.name == 'lvl 70',
                               ctx.message.guild.roles)
    role9 = discord.utils.find(lambda r: r.name == 'lvl 80',
                               ctx.message.guild.roles)
    role10 = discord.utils.find(lambda r: r.name == 'lvl 90',
                                ctx.message.guild.roles)
    for user in ctx.guild.members:

        if role2 in user.roles:
            await user.remove_roles(role1)
        if role3 in user.roles:

            await user.remove_roles(role2)
        if role4 in user.roles:
            await user.remove_roles(role3)
        if role5 in user.roles:
            await user.remove_roles(role4)
        if role6 in user.roles:
            await user.remove_roles(role5)
        if role7 in user.roles:
            await user.remove_roles(role6)
        if role8 in user.roles:
            await user.remove_roles(role7)
        if role9 in user.roles:
            await user.remove_roles(role8)
        if role10 in user.roles:
            await user.remove_roles(role9)


@client.command()
async def upgrade(ctx):
    await ctx.send("are u dumb?")


@client.command(aliases=["ce"])
async def createemojiurl(ctx, url: str, *, name):
    guild = ctx.guild
    if ctx.author.guild_permissions.manage_emojis:
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:

                try:
                    img_or_gif = BytesIO(await r.read())
                    b_value = img_or_gif.getvalue()
                    if r.status in range(200, 1000):
                        emoji = await guild.create_custom_emoji(image=b_value,
                                                                name=name)
                        await ctx.send(
                            f'Successfully created emoji: <:{name}:{emoji.id}>'
                        )
                        await ses.close()
                    else:
                        await ctx.send(
                            f'Error when making request | {r.status} response.'
                        )
                        await ses.close()

                except discord.HTTPException:
                    await ctx.send('File size is too big!')


@client.command()
async def deleteemoji(ctx, emoji: discord.Emoji):
    guild = ctx.guild
    if ctx.author.guild_permissions.manage_emojis:
        await ctx.send(f'Successfully deleted (or not): {emoji}')
        await emoji.delete()


@client.command(aliases=["ee"])
async def urlsave(ctx, emoji: Union[discord.Emoji, discord.PartialEmoji],
                  name: str):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(str(emoji.url)) as r:
            guild = ctx.guild
            img_or_gif = BytesIO(await r.read())
            b_value = img_or_gif.getvalue()
            await guild.create_custom_emoji(image=b_value, name=name)

            await ctx.send(f"emoji saved as {name} ")


@client.command()
@has_permissions(manage_emojis=True)
async def say(ctx, *, text=None):

    if not text:

        await ctx.send(
            f"Hey {ctx.author.mention}, I need to know what to say please.")
        return

    vc = ctx.voice_client
    if not vc:

        await ctx.send(
            "I need to be in a voice channel to do this, please use the join command."
        )
        return

    tts = gTTS(text=f"{text}", lang="en")
    tts.save("voice/text.mp3")

    try:

        vc.play(discord.FFmpegPCMAudio('voice/text.mp3'),
                after=lambda e: print(f"Finished playing: {text}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 100
    except Exception:
        print("a problem occured")





@client.command(aliases=["swl"])
@has_permissions(manage_emojis=True)
async def say_with_language(ctx, n, *, text=None):

    if not text:

        await ctx.send(
            f"Hey {ctx.author.mention}, I need to know what to say please.")
        return

    vc = ctx.voice_client
    if not vc:

        await ctx.send(
            "I need to be in a voice channel to do this, please use the join command."
        )
        return

    m = Language.find(n.lower())
    tts = gTTS(text=f"{text}", lang=str(m))
    tts.save("voice/text.mp3")
    try:

        vc.play(discord.FFmpegPCMAudio('voice/text.mp3'),
                after=lambda e: print(f"Finished playing: {text}"))

        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 100
    except Exception:
        print("a problem occured")


@client.command(hidden=True)
async def load(ctx, extension):
    if ctx.author.id == 647796364205359123:
        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"loaded {extension}")
    else:
        ctx.send("You do not have permission to execute this command")


@client.command(hidden=True)
async def unload(ctx, extension):
    if ctx.author.id == 647796364205359123:
        client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"unloaded {extension}")
    else:
        ctx.send("You do not have permission to execute this command")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send("reloaded")


roles = {}



@client.command()
async def embed(ctx, *, m):

    msg1 = m.split('...')[0]
    msg2 = m.split("...")[1]
    e = discord.Embed(title=f"{msg1}",
                      description=f"{msg2}",
                      color=discord.Color.blue())

    await ctx.message.delete()
    await ctx.send(embed=e)





@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send("You do not have permissions to execute that command :("
                       )

        await ctx.message.add_reaction("❌")
    if isinstance(error, commands.CommandOnCooldown):
        msg = "You are on cooldown for this command for {:.2f} seconds".format(
            error.retry_after)
        await ctx.message.reply(msg)


@client.command(aliases=["v"])
async def verification(ctx):
    e = discord.Embed(title="Click here to join our verification server",
                      color=discord.Color.blue(),
                      url="https://discord.gg/dzTXXKUJYe")
    await ctx.send(embed=e)


@client.command(aliases=["ar"])
@has_permissions(kick_members=True)
async def add_reaction(ctx, msgid, *, reactions):
    add_reactions = reactions.split(" , ")

    msg = await ctx.fetch_message(msgid)
    print(add_reactions)
    for emoji in add_reactions:
        add_emoji = discord.utils.get(ctx.message.guild.emojis,
                                      name=str(emoji))
        if add_emoji == None:
            add_emojis = emoji
        print(add_emoji)
        try:
            await ctx.message.add_reaction(add_emoji)
            await msg.add_reaction(add_emoji)
        except Exception:
            await ctx.message.add_reaction(emoji)
            await msg.add_reaction(emoji)


@client.command()
@has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send("Done")

    else:
        await ctx.send("They weren't muted in the first place")


@client.command()
@has_permissions(kick_members=True)
async def add_role(ctx, member: discord.Member, *, role):
    role = discord.utils.get(ctx.guild.roles, name=f"{role}")
    await member.add_roles(role)
    await ctx.send("Done")


@client.command()
@has_permissions(kick_members=True)
async def unrole(ctx, member: discord.Member, *, role):
    get_role = discord.utils.get(ctx.guild.roles, name=f"{role}")
    await member.remove_roles(get_role)
    await ctx.send("Done")


async def timeout_user(*, user_id: int, guild_id: int, until):
    client.session = aiohttp.ClientSession()
    headers = {"Authorization": f"Bot {client.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() +
               datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with client.session.patch(url, json=json,
                                    headers=headers) as session:
        if session.status in range(200, 299):
            return True
        return False


@client.command(help=",timeout (member) (time in minutes)")
@has_permissions(kick_members=True)
async def timeout(ctx: commands.Context, member: discord.Member, until: int):
    handshake = await timeout_user(user_id=member.id,
                                   guild_id=ctx.guild.id,
                                   until=until)
    if handshake:
        return await ctx.send(
            f"Successfully timed out {member.mention} for {until} minutes.")
    await ctx.send("Something went wrong")


    
    
    
    
    
    
accepted_roles = [786070828118179840 , 853352353099808809, 853352347840544819 , 853352343562354698, 853505260194758676, 853352328106737714, 853352316216672288, 864437296358359080, 874396020300210206]


@client.command()
async def create(ctx, hex_code , *, name):
  global role
  color = ImageColor.getcolor(f"{hex_code}" , "RGB")
  color = list(color)
  print(color)
  print(ctx.author.roles)
  for role in accepted_roles:
    role = discord.utils.get(ctx.guild.roles, id = role)
    
    data = open("memberroles.json","r")
    db = j.load(data)
    db = j.loads(db)
    if role in ctx.author.roles and ctx.message.channel.id == 784758643722551326 and str(ctx.author.id) not in db["data"] :
      await ctx.send("This might take a few seconds. Pls wait ")
      role = await ctx.guild.create_role(name = name ,permissions = discord.Permissions(attach_files= True), colour = discord.Colour.from_rgb(color[0], color[1], color[2]))
      
      with open("memberroles.json", "r+") as f :
        data = j.load(f)
        data2 = j.loads(data)
        print(type(data2))
        data2["data"][f"{ctx.author.id}"]= f"{role.id}"
        f.seek(0)
        j.dump(j.dumps(data2), fp = f)
        
      await ctx.send(f"{ctx.author.mention} Congratulations! Your role was successfully created :D")
      await ctx.message.author.add_roles(role)
      break
    

@client.command(aliases = ["ec"])
async def exclusive_color(ctx, color_hex):
  color = ImageColor.getcolor(f"{color_hex}" , "RGB")
  color = list(color)
  for role in accepted_roles:
    role = discord.utils.get(ctx.guild.roles, id = role)
    
    if role in ctx.author.roles and ctx.message.channel.id == 784758643722551326:
       await ctx.send("Creating your color , please wait")
       for color_role in ctx.author.roles:
         
         if color_role.name == "ㅤ":
           await color_role.delete()
       role = await ctx.guild.create_role(name = "ㅤ" , colour = discord.Colour.from_rgb(color[0], color[1], color[2]))
       await ctx.message.author.add_roles(role)
       guild = ctx.message.guild
       positions = {role : 118}
       await guild.edit_role_positions(positions = positions)
       await ctx.send("Done")
       break 
       




    

  

  
  
  
  
  


@client.command()
async def edit(ctx, hex_code = None,*, name = None):
  if hex_code is not None:
    if hex_code != "none":
        color = list(ImageColor.getcolor(f"{hex_code}" , "RGB"))
        new_color = discord.Colour.from_rgb(color[0], color[1], color[2])
    else:
      new_color == None    
  if name is not None:
    if name != "none":
       new_name = name
    else:
      new_name == None
  try:
    with open("memberroles.json","r") as f :
      read = j.load(f)
      read = j.loads(read)
      
      role =  discord.utils.get(ctx.guild.roles, id = int(read['data'][f"{ctx.message.author.id}"]))
      
      await role.edit(server = ctx.guild, role = role, name = new_name ,permissions =  discord.Permissions(attach_files= True), color = new_color)
      await ctx.send(f"{ctx.message.author.mention} , Your custom role was successfully updated :D")
  except Exception as e:
    await ctx.send(str(e))
    await ctx.send("You do not have a custom role yet 0_0")


  
  

confirmation_msg = {}

@client.command()
async def share(ctx , member : discord.Member):
  global role_msg
  global owner
  owner = ctx.message.author.id
  try:
    with open("memberroles.json","r") as f :
      read = j.load(f)
      read = j.loads(read)
      
      role = discord.utils.get(ctx.guild.roles , id = int(read["data"][f"{owner}"]))
      text = f"{member.mention} do you want to accept the role {role.mention} from {ctx.author.name} ?"
      e = discord.Embed(color = discord.Color.random(), description = text)
      role_msg = await ctx.send(embed = e)
      await role_msg.add_reaction("👍")
      await role_msg.add_reaction("👎")
      confirmation_msg[f"{role_msg.id}"] = f"{member.id}"
    
  except Exception as e:
    print(e)
    await ctx.send("You do not own a custom role yet in order to share it 0_0")

  
  
  
  
  
   

@client.event
async def on_raw_reaction_add(payload = None):
  guild = discord.utils.get(client.guilds, name="The Strangers")
  with open("memberroles.json","r") as f :
    read = j.load(f)
    read = j.loads(read)
    role = discord.utils.get(guild.roles , id = int(read["data"][f"{owner}"]))
    
  
  
  if payload is not None:
     
     if payload.message_id == role_msg.id:
       if payload.member.id == int(confirmation_msg[f"{role_msg.id}"]):
          if str(payload.emoji) == "👍":
            await payload.member.add_roles(role)
            channel = client.get_channel(payload.channel_id)
            e = discord.Embed(title = 'Congrats' , description = f"{payload.member.mention} has accepted your custom role" )
            e.set_image(url = "https://c.tenor.com/p1d2kjAdg5oAAAAM/drink-drunk.gif")
            await channel.send(embed = e)
          elif str(payload.emoji) == "👎":
            channel = client.get_channel(payload.channel_id)
            delete_msg = await channel.fetch_message(role_msg.id)
            await delete_msg.delete()
            await channel.send("It appears that they did not accept ur custom role :(")
          else:
            return    
            



@client.command()
async def crhelp(ctx):
  title = "This is a reward for the people who have reached or are above lvl 30 or a booster in this server. With this You can make a custom role for yourself and share it with others! Lets look at the commands for it .  "
  e = discord.Embed(title = title , color = discord.Color.random())
  e.add_field(name = "***create***  :    (create your custom role , this wont work if you dont use this command in bots channel, if you are not at or above lvl 30 or already have a custom role)", value = "usage = ,cr create (your desired custom role colors hex code)  (your custom roles name)" )
  e.add_field(name = "***edit***   :   (edit the color and name of your already made custom role)", value = "usage = ,cr edit (the hex code of your roles new color)  (the new name of your role)")
  e.add_field(name = "***share***   :    (share your custom role with other members of the server)" , value = "usage = ,cr share (mention the member you want it to share it with)")
  e.add_field(name = "***hex***   :   (see a chart of color hex codes , you can also search in google for a colors hex and use that here)" , value = "usage = ,cr hex")
  e.add_field(name = "***ec***   :     (ec stands for exclusive color. if you want a color which is not available in the colors channel, if you are at or above lvl 30 you can make a color of your own !!)" , value = "usage = ,cr ec (the desired colors hex code)")
  e.set_footer(text = "Remember to use a '#' before your hex code :)" , icon_url = client.user.avatar_url)
  await ctx.send(embed = e)

@client.command()
async def hex(ctx):
  embed = discord.Embed(color = discord.Color.random()) 
  embed.set_image(url = "https://i.pinimg.com/564x/82/20/22/8220221e75ea712cc6a280c052f83455.jpg") 
  await ctx.send(embed = embed)



    


    
 
  
  


    
    
 
@client.event
async def on_raw_message(msg):
    global mod_channel
    global server
    global reporter_dm
    global close_embed
    if not msg.author.bot:
        if isinstance(msg.channel, DMChannel):
            
            
            
            await msg.add_reaction("📬")
            what_the_member_sends = discord.Embed(
                title=str(msg.author),
                
                timestamp=datetime.datetime.utcnow()
            )
            what_the_member_sends.add_field(name="Question/Report", value=f'📧 = {msg.content}')
            what_the_member_sends.set_thumbnail(url=f'{msg.author.avatar_url}')
            if msg.attachments : what_the_member_sends.set_image(url = msg.attachments[0].proxy_url)
            what_the_member_sends.set_footer(text ="Note to mod : after finishing your session, type #close to close the thread ")
            server = discord.utils.get(client.guilds, name='The Strangers')
            category = discord.utils.get(server.channels, name="Reports")

            name_without_punctuation = str(msg.author.id)


 
            if discord.utils.get(server.channels, name=name_without_punctuation) is None:
                
                
                mod_channel = await server.create_text_channel(f'{msg.author.id}', category=category)
                await mod_channel.send(embed=what_the_member_sends)

                print('channel not found, created one')
                print(msg.author.name)

            else:
                
                mod_channel = discord.utils.get(server.channels, name=name_without_punctuation)
                await mod_channel.send(embed=what_the_member_sends)

                print('channel found, message sent')

        if msg.channel is not DMChannel :

            what_the_mod_sends = discord.Embed(
                description=msg.content,
                timestamp=datetime.datetime.utcnow()
            )
            if msg.attachments: what_the_mod_sends.set_image(url = msg.attachments[0].proxy_url)
            what_the_mod_sends.set_footer(text='Mod', icon_url=f'{msg.author.avatar_url}')
            what_the_mod_sends.set_author(name=f'{msg.author.name}', url=f'{msg.author.avatar_url}')


            server = discord.utils.get(client.guilds, name='The Strangers')
            
            try:
              reporter = discord.utils.get(server.members , id = int(msg.channel.name))
              reporter_dm = await reporter.create_dm()
              if msg.content != "#close":
                await reporter_dm.send(embed = what_the_mod_sends)
                print("dm sent")
            except Exception:
              pass

            


            close_embed=discord.Embed(
                title='Thread closed',
                description='Replying will make a new thread.',
                timestamp=datetime.datetime.utcnow()
            )

        if  msg.content.startswith('#close') and msg.channel is not DMChannel and msg.channel.category_id == 838832020342964224:
          try:
            await reporter_dm.send(embed=close_embed)
            await msg.channel.delete()
          except Exception:
            await msg.channel.delete()  

            
            
        else:
            pass




  




    
    




   
    


client.run("ODIyODg2NTQ0OTgwNzA1MzMw.YFYy0A.Qlczn8xYe_IuS6yWii_1xbBu7wE")

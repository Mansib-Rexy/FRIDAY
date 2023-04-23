import os
import time
import discord 
import asyncio
import re
import json
import aiohttp
from aiohttp import request
import praw
import time
import aiohttp
import discord.ext
import random_topic
import random
import datetime
import asyncio
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import youtube_dl
import time
import os
import requests
from discord.ext.commands import clean_content
from replit import db
import random
hugging = {}
import randomstuff
class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Rexy is online boss.')
    @commands.command(name="rps", help = "rock , paper, scissors")
    async def rock_paper_scissors(self, context):
        choices = {
            0: "rock",
            1: "paper",
            2: "scissors"
        }
        reactions = {
            "🪨": 0,
            "🧻": 1,
            "✂": 2
        }
        embed = discord.Embed(title="Please choose", color= discord.Color.random())
        embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
        choose_message = await context.send(embed=embed)
        for emoji in reactions:
            await choose_message.add_reaction(emoji)

        def check(reaction, user):
            return user == context.message.author and str(reaction) in reactions

        try:
            reaction, user = await self.client.wait_for("reaction_add", timeout=10, check=check)

            user_choice_emote = reaction.emoji
            user_choice_index = reactions[user_choice_emote]

            bot_choice_emote = random.choice(list(reactions.keys()))
            bot_choice_index = reactions[bot_choice_emote]

            result_embed = discord.Embed(color= discord.Color.random())
            result_embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
            await choose_message.clear_reactions()

            if user_choice_index == bot_choice_index:
                result_embed.description = f"**That's a draw!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
                
            elif user_choice_index == 0 and bot_choice_index == 2:
                result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
               
            elif user_choice_index == 1 and bot_choice_index == 0:
                result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
                
            elif user_choice_index == 2 and bot_choice_index == 1:
                result_embed.description = f"**You won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
                
            else:
                result_embed.description = f"**I won!**\nYou've chosen {user_choice_emote} and I've chosen {bot_choice_emote}."
                

            await choose_message.edit(embed=result_embed)
        except asyncio.exceptions.TimeoutError:
            await choose_message.clear_reactions()
            timeout_embed = discord.Embed(title="Too late", color=discord.Color.random)
            timeout_embed.set_author(name=context.author.display_name, icon_url=context.author.avatar_url)
            await choose_message.edit(embed=timeout_embed)
    @commands.command(aliases = ["qu"], help = "generates a random conversation starter")
    async def question(self, ctx):
      topic=random_topic.get_topic()
      await ctx.send(topic)
    @commands.Cog.listener()
    async def on_message(self,msg):
      if msg.channel.id == 783547639944839182 and msg.author != self.client.user:
        hugging[msg.author.mention] = msg.author
        
        
      else:
        pass  

    @commands.command(aliases = ["sav"])
    async def server_avatar(self , ctx , member : discord.Member):
      userAvatar = member.display_avatar
      embed = discord.Embed(title=f"Member Avatar", description="", color=0xffff00)
      embed.set_image(url=userAvatar.url)
      await ctx.send(embed = embed)
      
    @commands.command()
    async def hugs(self,ctx):
      hugs = [
     "https://c.tenor.com/oPIi24wF8ucAAAAM/hug-virtual-hug.gif",
     "https://c.tenor.com/wqCAHtQuTnkAAAAM/milk-and-mocha-hug.gif",
     "https://c.tenor.com/DxMIq9-tS5YAAAAM/milk-and-mocha-bear-couple.gif",
     "https://c.tenor.com/jX1-mxefJ54AAAAM/cat-hug.gif",
     "https://c.tenor.com/qj_wTx9dXVMAAAAM/cat-hug.gif"]
      mm = str(list(hugging.keys()))
      mm2 = mm.replace("[" ," ")
      mm3 = mm.replace("]" , " ")
      mm4 = mm.replace("'", " ")
      e = discord.Embed(color = discord.Color.random(), description = mm4)
      e.set_image(url = random.choice(hugs))
      await ctx.send(embed = e)
      hugging.clear()
      
    @commands.command(aliases = ["c"]) 
    async def chat_(self, ctx,*,msg):
        with randomstuff.Client(api_key='0sSteSVSNPYR') as client:
            response = client.get_ai_response(msg.content.lower())
            if "@everyone" not in ctx.message.content.lower() and "@here" not in ctx.message.content.lower():
                await ctx.send(response)
            else:
                await ctx.send("No")
                
      


      

        

      
      


     
        
    @commands.command()
    async def describe(self, ctx , member:discord.User,*,description):
      db[f"member:{member.id}"] = f'Description provided by {ctx.message.author}        description:                  .............................................................    {description}'
      await ctx.send("Described")
      await ctx.message.delete()



    @commands.command(help = "Use the , describe command to describe your friend which will enlist them in the database . And when you play trvia there is a chance that they will appear in the question . if the description matches a person you know , mention them before the timer runs out , and you win!")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def trivia(self , ctx):
      key = random.choice(db.prefix("member:"))
      description = db[f"{key}"]
      
      await ctx.send(description)
      await asyncio.sleep(3)
      await ctx.send("Guess who this person is")


      keys = []
      dude = discord.utils.get(ctx.guild.members , id = int(str(key.split("member:")[1])))
      try:
        
        msg = await self.client.wait_for("message",timeout = 13 , check = lambda message: discord.utils.get(ctx.guild.members , id = int(str(key.split("member:")[1]))) in message.mentions and message.author.bot == False and id not in keys and message.channel == ctx.message.channel )
        await msg.reply("Bingo!") 
        keys.append(id)
      except asyncio.TimeoutError:
        await ctx.send(f"Timeout , The person is {dude}")
      except Exception as e:
        print(e)
      


      
      
        
      
      
      
      
    @commands.command() 
    async def aww(self, ctx):
      headers = {"Authorization" : "BWlDbwTGnMGl"}
      url = "https://api.pgamerx.com/v5/image"
      query = {"type" : "aww"}
      response = requests.request("GET", url, headers = headers, params = query)
      res = response.json()
      if "@everyone" in ctx.message.content.lower():
        return
      else:  
        await ctx.send(res)
      

      



      
      
      


def setup(client):
  client.add_cog(fun(client))
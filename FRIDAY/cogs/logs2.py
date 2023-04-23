import discord
from discord.ext import commands
from datetime import datetime
from discord import utils
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
from discord import guild
import random
import asyncio
import os 
from chatbot import Chat, register_call
import wikipedia
import OpenAi


















class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
      self.lc = self.bot.get_channel(859113481860153374)
      self.lc1 = self.bot.get_channel(855509152738443324)
      self.lc2 = self.bot.get_channel(783547639944839182)

      
      print("Logs ready")




    @commands.Cog.listener()
    async def on_message(self,msg):
      hugs = [
     "https://c.tenor.com/oPIi24wF8ucAAAAM/hug-virtual-hug.gif",
     "https://c.tenor.com/wqCAHtQuTnkAAAAM/milk-and-mocha-hug.gif",
     "https://c.tenor.com/DxMIq9-tS5YAAAAM/milk-and-mocha-bear-couple.gif",
     "https://c.tenor.com/jX1-mxefJ54AAAAM/cat-hug.gif",
     "https://c.tenor.com/qj_wTx9dXVMAAAAM/cat-hug.gif"]
      list_user = []
      responses = 0
      if msg.channel.id == 1026400240342937630 and msg.author.id != 822886544980705330:
        chat_log = ""
        list_user.append(msg.author.id)
        question = msg.content
        answer = OpenAi.ask(question, chat_log)
        chat_log = OpenAi.append_interaction_to_chat_log(question, answer,chat_log)
        await msg.channel.send(answer)
        f = open("log_user.txt", "w")
        for it in list_user:
          f.write("%i\n" % it)
          f.close()






            





   
    @commands.Cog.listener()
    async def on_message_delete(self,msg):
      e = discord.Embed(title = f"Message Deleted by {msg.author}", color = discord.Color.red())
      if msg.attachments:
        mm = msg.attachments[0].proxy_url
        e.set_image(url = mm)
      if msg.content:
        e.add_field(name = "Content", value = f"{msg.content}")

      e.set_thumbnail(url=msg.author.avatar_url)
      e.timestamp = datetime.utcnow()
      e.set_footer( text = f"deleted in {msg.channel.name}") 
      try:
        await asyncio.sleep(2)
        await self.lc1.send(embed=e)
      except Exception:
        pass






      

      
      if msg.guild.id == 783547639944839178:
        try:
          await self.lc.send(embed = e)
        except Exception:
          pass



      
      
        

      
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
      e = discord.Embed(title = f'Message Edit by {before.author}', color = discord.Color.blue())
      e.add_field(name = "Before", value = f"{before.content}")
      e.add_field(name = "after", value = f"{after.content}")
      e.set_thumbnail(url=before.author.avatar_url)
      e.timestamp = datetime.utcnow()
      if before.attachments:
        e.set_image(url = before.attachments[0].proxy_url)
      e.set_footer( text = f"edited in {before.channel.name}") 

      
      if before.guild.id == 783547639944839178:
        await asyncio.sleep(2)
        try:
          await self.lc.send(embed = e)
        except Exception:
          pass
      await asyncio.sleep(2)
      try:
        await self.lc1.send(embed=e) 
      except Exception:
        pass
          

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
      if before.avatar_url != after.avatar_url:
        e = discord.Embed(title = f"Profile picture changed by {before.name}",description = "The small picture is previous avatar and the large one is new avatar", color = discord.Color.dark_gold())
        e.set_image(url = after.avatar_url)
        e.set_thumbnail(url =before.avatar_url)
        
        await self.lc1.send(embed = e)

      if before.name != after.name:
        e = discord.Embed(title = f"Username change by {before.name}", color = discord.Color.dark_gold())
        e.add_field(name = "New username", value = f"{after.name}")
      try:
        if before.guild.id == 783547639944839178:
          await self.lc.send(embed = e)
        await self.lc1.send(embed=e)
      except Exception:
        pass
        
      
        
      
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
      if before.display_name != after.display_name:

        e = discord.Embed(title =f"Nickname change by {before.display_name}", color = discord.Color.dark_gold()) 
        e.add_field(name = "New nickname", value = f"{after.display_name}")

 
        
     
        await self.lc1.send(embed=e)  
      if before.guild.id == 783547639944839178:
        try:
          await asyncio.sleep(2)
          await self.lc.send(embed = e) 
        except Exception:
          pass   
                  
    @commands.Cog.listener()
    async def on_member_remove(self,member):
      await self.lc.send(f"{member.name}#{member.discriminator} has left the server")
    @commands.Cog.listener()
    async def on_member_join(self, member):
      server = discord.utils.get(self.bot.guilds, name= "The Strangers")
      welcome = discord.utils.get(server.roles , id = 894547700106797057)      
      
      channel = self.bot.get_channel(783547639944839182)
      if member.guild.id == 783547639944839178:
        await channel.send(f"{welcome.mention}")

      
      
    @commands.Cog.listener() 
    async def on_raw_reaction_add(self, payload = None):
      msgid1 = 0
      msgid2 = 892487208525783071
      msgid3 = 892487843686002729
      msgid4 = 905399635395362816
      msgid5 = 926889750034538517
      msgid6 = 923274781338517535
      gender_roles = [892444369070723083, 892444612361342996 , 892444721547448330]
      pronoun_roles = [892444852283904010 , 892445302437593108 , 892445411502071838, 892504872484757634]
      age_roles = [892446370504511508, 892446457364373525, 892446567150268476, 892446652328210482, 892446740026904676, 892490432360112158]
      continent_roles = [905393094302773250, 905393490089885717, 905393347571638282, 905393417675219014, 905393857540272158, 905393733258854432, 905395549006618625]
      accepted_roles = [853352361589866576,853352357788909588,853352353099808809, 853352347840544819 , 853352343562354698, 853505260194758676, 853352328106737714, 853352316216672288, 864437296358359080, 874396020300210206]
      event_roles = [923270065082744903,923270345501311066,869219796468768838]
      gender = {"1️⃣" : "892444369070723083" , "2️⃣": "892444612361342996" ,"3️⃣" : "892444721547448330" }
      pronoun = {"1️⃣" : "892444852283904010" , "2️⃣" : " 892445302437593108" ,"3️⃣": "892445411502071838" , "4️⃣" : "892504872484757634" }
      age = {"1️⃣" : "892446370504511508" , "2️⃣" : " 892446457364373525" , "3️⃣" : "892446567150268476" , "4️⃣" : " 892446652328210482" , "5️⃣" : " 892446740026904676", "6️⃣" : "892490432360112158"}
      continent = {"1️⃣" : "905393094302773250" , "2️⃣" : "905393490089885717" , "3️⃣" : "905393347571638282" , "4️⃣" : "905393417675219014" , "5️⃣" : "905393857540272158", "6️⃣" : "905393733258854432" , "7️⃣" : "905395549006618625" }      
      event = {"1️⃣" : "923270065082744903" , "2️⃣" : "923270345501311066" , "3️⃣" : "869219796468768838" } 
      if payload is not None:
        if payload.message_id == msgid1:
          for role in gender_roles:
            server = discord.utils.get(self.bot.guilds, name= "The Strangers")
            get_role = discord.utils.get(server.roles, id = role)
            try:
               await payload.member.remove_roles(get_role)
            except Exception:
              pass   
          for emoji in gender:
            if str(payload.emoji) == f"{emoji}":
              await asyncio.sleep(3)
              await payload.member.add_roles(discord.utils.get(server.roles, id =int(gender[f"{emoji}"])))
        if payload.message_id == msgid2:
          for role in pronoun_roles:
            server = discord.utils.get(self.bot.guilds, name= "The Strangers")
            get_role = discord.utils.get(server.roles, id = role)
            try:
               await payload.member.remove_roles(get_role) 
            except Exception:
              pass            


          for emoji in pronoun:
            if str(payload.emoji) == f"{emoji}":
              await asyncio.sleep(3)
              await payload.member.add_roles(discord.utils.get(server.roles, id =int(pronoun[f"{emoji}"])))
        if payload.message_id == msgid3:
          for role in age_roles:
            server = discord.utils.get(self.bot.guilds, name= "The Strangers")
            get_role = discord.utils.get(server.roles, id = role)
            try:
              await payload.member.remove_roles(get_role)
            except Exception:
              pass                                 
          for emoji in age:
            if str(payload.emoji) == f"{emoji}":
              await asyncio.sleep(3)
              await payload.member.add_roles(discord.utils.get(server.roles, id =int(age[f"{emoji}"])))       
        if payload.message_id == msgid4:
          for role in continent_roles:
            server = discord.utils.get(self.bot.guilds, name= "The Strangers")
            get_role = discord.utils.get(server.roles, id = role)
            try:
              await payload.member.remove_roles(get_role)
            except Exception:
              pass                                 
          for emoji in continent:
            if str(payload.emoji) == f"{emoji}":
              await asyncio.sleep(3)
              await payload.member.add_roles(discord.utils.get(server.roles, id =int(continent[f"{emoji}"])))     
        if payload.message_id == msgid5:
          server = discord.utils.get(self.bot.guilds, name= "The Strangers")
          welcome = discord.utils.get(server.roles , id = 894547700106797057)
          channel = self.bot.get_channel(payload.channel_id)
          msg = await channel.fetch_message(payload.message_id)

          user = payload.member 
          if str(payload.emoji) == "👍":
            emoji = payload.emoji
            for role in accepted_roles:
              role = discord.utils.get(server.roles , id = role)
              if role in payload.member.roles:
                await payload.member.add_roles(welcome)

            
            await msg.remove_reaction(emoji, user)         
          if str(payload.emoji) == "👎":
            emoji = payload.emoji
            await payload.member.remove_roles(welcome) 
            await msg.remove_reaction(emoji , user)
          if not str(payload.emoji) == "👍" or str(payload.emoji) == "👎":
            emoji = payload.emoji

            await msg.remove_reaction(emoji, user)
        if payload.message_id == msgid6:
         


          for emoji in event:
            server = discord.utils.get(self.bot.guilds, name= "The Strangers")
            if str(payload.emoji) == f"{emoji}":
              await payload.member.add_roles(discord.utils.get(server.roles, id =int(event[f"{emoji}"])))
                                     
              
            
              
              

              
                 

    


def setup(bot):
	bot.add_cog(Logs(bot))      

      

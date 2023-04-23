import discord
from discord.ext import commands
from discord.utils import get 
from PIL import Image , ImageEnhance
import requests
from discord.ext.commands import check
import json
import asyncio
import requests
from io import BytesIO
###################################################
nx = -50
ny = 0
nw = 0
nh = 0
con = 150
qu = 500
users = []

class new_task(commands.Cog):
  def __init__(self , bot):
  
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
     print("ready")
     users.clear()
     print("cleared users")
     

    
   
  @commands.Cog.listener()
  async def on_message(self, msg):
    if msg.content.lower() ==("!rank") and msg.guild.id == 783547639944839178:
      
      await msg.channel.send("receiving")
      try:
        
        print(users)
        original_msg = msg
        msg = await self.bot.wait_for("message" , check = lambda message: message.author.bot == True)
        image = msg.attachments[0].proxy_url
    
        response = requests.get(image)
        img = Image.open(BytesIO(response.content))
        img = img.crop((798+ nx,36 + ny ,119+798 + nw,36+106+ nh))
        
        


        img.save("images/cropped.png", quality=qu)
        enhancer = ImageEnhance.Contrast(Image.open("images/cropped.png"))
        enhancer = ImageEnhance.Contrast(Image.open("images/cropped.png"))
        enhancer.enhance(con).save("images/cropped.png", quality=qu)
                                               

        img = await msg.channel.send(file=discord.File('images/cropped.png'))
        await msg.channel.send("analysing with computer vision ai ")
        image = img.attachments[0].proxy_url
        
        
        
        print(image)
      
        url = None
 
        querystring = {"detectOrientation":"false","language":"en"}
        payload = {"url" : f"{image}"}
        payload = json.dumps(payload)
        
        headers = None
        if int(original_msg.author.id) not in users:
          headers = {'content-type': "application/json",
    'x-rapidapi-host': "microsoft-computer-vision3.p.rapidapi.com",
    'x-rapidapi-key': "60d723ef7cmshe33123bd214fa25p1c43c3jsn32ca6e303e26"}
          url = "https://microsoft-computer-vision3.p.rapidapi.com/ocr"
        else:
          headers = None
          url = None
        
        

       
        response = requests.request("POST" , url , data = payload , headers = headers , params = querystring)
        print(response.json())
        lvl= response.json()["regions"][0]["lines"][0]['words'][0]['text']
        await msg.channel.send("your level is " + lvl +". The info is being sent to my database")
        print(lvl)
        with open("roles.json" , "r") as rolefile:
          data = json.load(rolefile)
          print('json file loaded')
        
        for x in data['roles']:
         if x["level"] <= int(lvl) and x["level"] > int(int(lvl)-9):
           getrole = get(msg.guild.roles, id = int(x["id"]))
           print("found role")
           if getrole in original_msg.author.roles:
             print("user already has that role")
             await msg.channel.send("Seems like your lvl roles are already updated")
             users.append(int(original_msg.author.id))
             print(users)
           else:
             await original_msg.author.add_roles(getrole)
             await msg.channel.send("your lvl roles were updated")
             users.append(int(original_msg.author.id))
             print(users)

           
           

           

            
        
      except Exception as e:
        print(e)
        await msg.channel.send("User was already updated to database")
  
      
      
      
      


def setup(bot):
  bot.add_cog(new_task(bot))
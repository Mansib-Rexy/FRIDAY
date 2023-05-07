import discord
import shutil
import os
from langcodes import Language
import asyncio
from google_images_search import GoogleImagesSearch
from bs4 import BeautifulSoup
from googletrans import Translator
import discord.ext
from discord.ext import commands 
from discord.utils import get
from discord.ext.commands.cooldowns import BucketType


apikeyfile = open("apikey.txt", 'r')
apikey = apikeyfile.read()
apikeyfile.close()

cxfile = open("cx.txt", 'r')
cx = cxfile.read()
cxfile.close()

gis = GoogleImagesSearch(apikey, cx)
translator = Translator()

class Google(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command(aliases=["gi","googleimages","googlei","gimage","gimages"])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def googleimage(self, ctx, num:int,*,imaged):
        Images_infile = os.path.isdir("Images")
        if num <= 10:
          await ctx.send("This might take a few seconds. Please wait and before typing the command a second time , pleease type ```,rq``` to reload my image queue")
        else:
          pass  

        
        try:
            Images_folder = "Images"
            if Images_infile is True:
                shutil.rmtree(Images_folder)
                print("Removed old Images folder")
                os.mkdir("Images")
                print("Made new Images folder")
            else:
                os.mkdir("Images")
                print("images_infile was false, making images folder")
        except:
            print("No old images folder")
            os.mkdir("jpg")
            print("Made new images folder")
        Images_infile2 = os.path.isdir("Images")
        if Images_infile2 is False:
            return await ctx.send("Error: something happened. Try again if you like.")
        q = " ".join(imaged)
        start = 1
        _search_params = {
            'q': q,
            'searchType': 'image',
            'num': num,
            'start': start,
            'safe': 'medium',
            'fileType': 'jpg',
            'imgType': None,
            'imgSize': None,
            'imgDominantColor': None
        }
        if num >=10:
          await ctx.send("The limit is 10 images")
        else:

           gis.search(search_params=_search_params, path_to_dir='Images', custom_image_name = "image")
           for file in os.listdir('Images'):
                if file.endswith(".jpg"):
                 await asyncio.sleep(.1)
                 await ctx.send(file = discord.File(f"Images/{file}"))
                
    @commands.command()
    async def rq(self,ctx):

        for file in os.listdir("./cogs"):
          if file.endswith(".py"):
            self.client.unload_extension("cogs.web")
            self.client.load_extension("cogs.web")
        await ctx.send("reloaded image queue")      

     



     

            



def setup(client):
    client.add_cog(Google(client))

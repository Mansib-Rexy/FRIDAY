import discord
from discord.ext import commands
import json

def register(file, guild):
    with open(file, 'r+') as f:
        data = json.load(f)
    if str(guild.id) not in list(data):
        data[str(guild.id)] = {
            "AFK": {}
        }
        with open(file, 'w') as f:
            json.dump(data, f, indent = 4)




class afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['afk', 'Afk', 'aFk', 'afK','AFk', 'aFK', 'AfK'])
    async def AFK(self, ctx, *, reason=None):
        if reason == None:
            reason2 = "I've set your offline status"
            reason = ''
        else:
            reason2 = f"I've set your offline status. reason: {reason}"
        with open("enabled.json", "r") as f:
            data = json.load(f)
        print(list(data[str(ctx.guild.id)]['AFK']))
        if str(ctx.author.id) in list(data[str(ctx.guild.id)]['AFK']):
            await ctx.channel.send("Bruh. you've already set an offline status")
            return

        
        data[str(ctx.guild.id)]['AFK'][str(ctx.author.id)] = reason
        await ctx.channel.send(f'{ctx.author.mention} {reason2}')
        

        with open("enabled.json", "w") as f:
            json.dump(data,f, indent = 4)
        try:
            await ctx.message.add_reaction("👍")
        except:
            pass
    @commands.Cog.listener()
    async def on_message(self, message):
        
        register('enabled.json', message.guild)
        if message.content.startswith('#'): 
            return
        with open("enabled.json", "r") as f:
            data = json.load(f)
        
        if str(message.author.id) in list(data[str(message.guild.id)]['AFK']):
            data[str(message.guild.id)]["AFK"].pop(str(message.author.id))
            with open("enabled.json", "w") as f:
                json.dump(data, f, indent=4)
            await message.channel.send(f'Welcome Back, I removed your offline status!')
        
        for i in message.mentions:
            if str(i.id) in list(data[str(message.guild.id)]['AFK']) and message.author != self.bot.user:
                if data[str(message.guild.id)]['AFK'][str(i.id)] != '':
                    reason = 'Reason: ' + data[str(message.guild.id)]['AFK'][str(i.id)]
                else:
                    reason = ''
                await message.channel.send(f'{message.author.mention}, {i.name} is offline. {reason}')
                break
    

def setup(bot):
  bot.add_cog(afk(bot))
import discord, asyncio, time
from time import ctime
from discord.ext import commands
from discord import utils
from discord.utils import get

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

      


      
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, user : discord.Member, *, reason=None):
        if ctx.author.top_role > user.top_role :
            if user == ctx.author:
                return await ctx.send(f"**:no_entry: {user.mention} You can't kick yourself... just, leave the server?**")
            await user.kick(reason=reason) 
            if not reason:
                msg = await ctx.send(f"**{user} was kicked :wave:**")                
                await msg.add_reaction("a:SpectrumOkSpin:466480898049835011")
                await user.send(f"**You were kicked from {ctx.guild.name}**")
            else:
                msg = await ctx.send(f"**{user} was kicked :wave: Reason:** {reason}")                
                await msg.add_reaction("a:SpectrumOkSpin:466480898049835011")
                await user.send(f"**You were kicked from {ctx.guild.name}. Reason:** {reason}")

    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user : discord.Member, *, reason=None):
        if ctx.author.top_role > user.top_role :
            if user == ctx.author:
                return await ctx.send(f"***:no_entry: {user.mention} You can't ban yourself... just, uninstall Discord?***")
            await user.ban(reason=reason)
            if not reason:
                msg = await ctx.send(f"**{user} was banned :hammer:**")                
                await msg.add_reaction("a:SpectrumOkSpin:466480898049835011")
            else:
                msg = await ctx.send(f"**{user} was banned :hammer: Reason:** {reason}")                
                await msg.add_reaction("a:SpectrumOkSpin:466480898049835011")
    @commands.has_permissions(kick_members = True)
    @commands.command()
    async def warn(self , ctx , member : discord.Member,*,reason : str):
      e = discord.Embed(color = discord.Color.red(), title = "Warning", description = f"Member {member.mention} has been warned for " + reason)
      e.set_thumbnail(url = member.avatar_url)
      e.set_footer(text ="Please do not continue further or else it will lead to mute or ban, Thanks!")
      await ctx.send(embed = e)             
    
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command(aliases=['sb'])
    async def softban(self, ctx, user : discord.Member, *, reason=None):
        if ctx.author.top_role > user.top_role :
            if user == ctx.author:
                return await ctx.send("***:no_entry: You can't softban yourself...***")
            await user.ban(reason=reason)
            await user.unban(reason=reason)
            if not reason:
                msg = await ctx.send(f"**{user} was softbanned :wave:**")                
                await msg.add_reaction("a:SpectrumOkSpin:466480898049835011")
            else:
                msg = await ctx.send(f"**{user} was softbanned :wave: Reason:** {reason}")                
                await msg.add_reaction("a:SpectrumOkSpin:466480898049835011")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clean(self, ctx, number: int):
        msg = "message"
        if number != 1:
            msg+='s'
        amt = await ctx.channel.purge(limit = (int(number) + 1))
        await asyncio.sleep(1)
        clearConfirmation = await ctx.send(f"**Cleared `{len(amt) - 1}` {msg} from this channel**", delete_after=4.0)        
    
    
    @commands.has_permissions(manage_nicknames = True)
    async def nickname(
        self, ctx, member: discord.Member = None, *, name: commands.clean_content = None
    ):
        """``nickname [@user] [newname]`` changes the nickname of a member"""
        await member.edit(nick=name) if (name != None) else None
    @commands.Cog.listener()
    async def on_message(self,msg):
      if msg.author != self.bot.user:
        return
      elif msg.content.startswith("No command called"):
          await msg.delete()
      else:
        return
        




        
def setup(client):
    client.add_cog(Mod(client))
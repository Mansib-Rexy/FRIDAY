import discord
from discord.ext import commands
from datetime import datetime, timedelta
listed = []
class Helpful(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_member_join(self , member):
      listed.clear()
    @commands.Cog.listener()
    async def on_message(self, msg):

      if len(listed) == 0:
        
          if msg.author.id not in listed:
            if msg.content.lower().startswith("welcome"):

               await msg.add_reaction("🥇")
               listed.append(msg.author.id)
               
      elif len(listed) == 1:
        
          if msg.author.id not in listed:
            if msg.content.lower().startswith("welcome"):

               await msg.add_reaction("🥈")
               listed.append(msg.author.id)
               
      elif len(listed) == 2:
        
          if msg.author.id not in listed:
            if msg.content.lower().startswith("welcome"):

               await msg.add_reaction("🥉")
               listed.append(msg.author.id)
                   




             
           
     


    @commands.command(aliases=["channel_stats", "channel_health", "channel_info", "channel_information"])
    async def channel_status(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            channel = ctx.channel

        server_id = self.client.get_guild(self.client.guilds[0].id)

        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Channel Health:")

        async with ctx.channel.typing():
            count = 0
            async for message in channel.history(limit=5000, after=datetime.today() - timedelta(days=1)): count += 1

            if count >= 500:
                average = "OVER 500!"
                healthiness = "VERY HEALTHY"

            else:
                try:
                    average = round(count / 100, 2)

                    if 0 > server_id.member_count / average: healthiness = "VERY HEALTHY"
                    elif server_id.member_count / average <= 5: healthiness = "HEALTHY"
                    elif server_id.member_count / average <= 10: healthiness = "NORMAL"
                    elif server_id.member_count / average <= 20: healthiness = "UNHEALTHY"
                    else: healthiness = "VERY UNHEALTHY"

                except ZeroDivisionError:
                    average = 0
                    healthiness = "VERY UNHEALTHY"

            embed.add_field(name="­", value=f"# of members: {server_id.member_count}", inline=False)
            embed.add_field(name="­", value=f'# of messages per day on average in "{channel}" is: {average}', inline=False)
            embed.add_field(name="­", value=f"Channel health: {healthiness}", inline=False)

            await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Helpful(client))            
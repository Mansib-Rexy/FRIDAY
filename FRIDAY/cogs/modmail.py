import discord
import os
import requests
import json
import random
from replit import db
from discord import DMChannel, GroupChannel
import datetime
import pytz
import googletrans
import asyncio
import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import re
from discord.ext import commands
import discord
from discord.ext import commands
from discord import DMChannel, GroupChannel
import datetime
import pytz
class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        global mod_channel
        global server
        global reporter_dm
        global close_embed
        if not msg.author.bot:
            if isinstance(msg.channel, DMChannel):
                await msg.add_reaction("📬")
                what_the_member_sends = discord.Embed(
                    title=str(msg.author), timestamp=datetime.datetime.utcnow()
                )
                what_the_member_sends.add_field(
                    name="Question/Report", value=f"📧 = {msg.content}"
                )
                what_the_member_sends.set_thumbnail(url=f"{msg.author.avatar_url}")
                if msg.attachments:
                    what_the_member_sends.set_image(url=msg.attachments[0].proxy_url)
                what_the_member_sends.set_footer(
                    text="Note to mod : after finishing your session, type #close to close the thread "
                )
                server = discord.utils.get(self.bot.guilds, name="The Strangers")
                category = discord.utils.get(server.channels, name="Reports")
                name_without_punctuation = str(msg.author.id)
                if (
                    discord.utils.get(server.channels, name=name_without_punctuation)
                    is None
                ):
                    mod_channel = await server.create_text_channel(
                        f"{msg.author.id}", category=category
                    )
                    await mod_channel.send(embed=what_the_member_sends)
                    print("channel not found, created one")
                    print(msg.author.name)
                else:
                    mod_channel = discord.utils.get(
                        server.channels, name=name_without_punctuation
                    )
                    await mod_channel.send(embed=what_the_member_sends)
                    print("channel found, message sent")

            if msg.channel is not DMChannel:
                what_the_mod_sends = discord.Embed(
                    description=msg.content, timestamp=datetime.datetime.utcnow()
                )
                if msg.attachments:
                    what_the_mod_sends.set_image(url=msg.attachments[0].proxy_url)
                what_the_mod_sends.set_footer(
                    text="Mod", icon_url=f"{msg.author.avatar_url}"
                )
                what_the_mod_sends.set_author(
                    name=f"{msg.author.name}", url=f"{msg.author.avatar_url}"
                )
                server = discord.utils.get(self.bot.guilds, name="The Strangers")
                try:
                    reporter = discord.utils.get(
                        server.members, id=int(msg.channel.name)
                    )
                    reporter_dm = await reporter.create_dm()
                    if msg.content != "#close":
                        await reporter_dm.send(embed=what_the_mod_sends)
                        print("dm sent")
                except Exception:
                    pass
                close_embed = discord.Embed(
                    title="Thread closed",
                    description="Replying will make a new thread.",
                    timestamp=datetime.datetime.utcnow(),
                )
            if (
                msg.content.startswith("#close")
                and msg.channel is not DMChannel
                and msg.channel.category_id == 838832020342964224
            ):
                try:
                    await reporter_dm.send(embed=close_embed)
                    await msg.channel.delete()
                except Exception:
                    pass


def setup(bot):
    bot.add_cog(Logs(bot))

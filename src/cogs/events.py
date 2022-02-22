# events.py
# By: thekraftyman

# import packages
import discord
import asyncio
from src.lib.core_funcs import *
from time import sleep
from discord.ext import commands

class Bot_Events(commands.Cog):
    def __init__(self,client):
        self.client = client

    # ---------------------------
    # Add events below

    # triggers when someone reacts to a message
    @commands.Cog.listener() # for use with events
    async def on_reaction_add(self, reaction, user):
        pass

    # be the first to post in a new chat
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        ''' will post "first" in a new channel '''
        await channel.send("First!")

    # add roles to user on guild join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    # Don't add below line
    # ---------------------------


# add the cog
def setup(client):
    client.add_cog(Bot_Events(client))

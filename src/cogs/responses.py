# responses.py
# By: thekraftyman

# import packages
import discord
from discord.ext import commands
from src.lib.core_funcs import *
import re
import asyncio
import random

class Bot_Responses(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.generic_responses = import_generic_responses()
        self.default_name = load_config()["bot_name"]

    # ---------------------------
    # Add responses below

    # default reponses
    @commands.Cog.listener() # for use with events
    async def on_message(self, message):

        # add role moderation here
        await self.role_moderation_react( message )

        # skip if the bot said it (no loops)
        if message.author == self.client.user:
            return

        await self.reset_nickname( message )

    # ---------------------------
    # Add extra function below to add to the main function ^^^

    async def reset_nickname(self, message):
        '''
        Change nickname back if it isn't the default name
        '''
        if message.guild.me.nick:
            await asyncio.gather(
                async_change_nickname(message.guild.me, self.default_name)
            )


    # Don't add below line
    # ---------------------------

# add the cog
def setup(client):
    client.add_cog(Bot_Responses(client))

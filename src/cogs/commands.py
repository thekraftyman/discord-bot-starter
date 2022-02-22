# commands.py
# By: thekraftyman

# import packages
import discord
from discord.ext import commands
from src.lib.core_funcs import *
from random import choice
import subprocess
import asyncio
import random
import json
import os

class Bot_Commands(commands.Cog):
    def __init__(self,client):
        self.client = client

    # ---------------------------
    # Add commands below

    # Sarcasm command
    @commands.command(name='sarcasm', help='Returns your input... but sarcastically')
    async def sarcasm(self,ctx, *args):
        # escape if not arg
        for arg in args:
            if type(arg) != str:
                return

        # combine the args into one arg
        arg = ' '.join(args)

        toreturn = '' # string to return
        arg_list = list(arg) # exploded argument
        odd = True # is on odd char (starting at 1)

        for char in arg_list:
            if not char.isalpha(): # is not a letter
                toreturn = toreturn + char
                continue

            if odd: # capitalize the upper case
                toreturn = toreturn + char.upper()
                odd = False # switch
            else: # make lowercase
                toreturn = toreturn + char.lower()
                odd = True # switch

        # print out the sarcastic message and delete the invoking command
        await asyncio.gather(
            async_message_send_with_context(ctx, toreturn),
            async_delete_message_with_context(ctx)
        )


    # return bot version
    @commands.command(name='version', help='Returns the bot version')
    async def version(self,ctx, *args):
        await ctx.send(get_version())


    # for choosing between inputs randomly
    @commands.command(name='choose', help='Returns on of multiple inputs randomly')
    async def choose(self,ctx, *args):
        for arg in args:
            if type(arg) != str:
                return
        await ctx.send(choice(args))

    # Don't add below line
    # ---------------------------

# add the cog
def setup(client):
    client.add_cog(Bot_Commands(client))

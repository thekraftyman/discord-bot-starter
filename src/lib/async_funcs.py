# async_funcs.py
# By: thekraftyman

import asyncio
from src.lib.non_async_funcs import *

'''
A collection of async function that can be used easily with
    asyncio.gather()
'''

async def async_change_nickname(user, nickname):
    '''
    changes the nickname of a user
    '''
    await user.edit(nick=nickname)

async def async_add_role( member, role ):
    '''
    adds a role to a member
    '''
    await member.add_roles(role)

async def async_channel_send(channel, content):
    '''
    send content to channel
    '''
    await channel.send(content)

async def async_delete_message(message):
    '''
    delete message
    '''
    await message.delete()

async def async_delete_message_with_context(context):
    '''
    Deletes a message with given context
    '''
    await context.message.delete()

async def async_message_send_with_context(context, content, **kwargs):
    '''
    Sends content with given context
    '''
    await context.send(content, **kwargs)

async def async_message_react_with_emoji( message, emoji ):
    '''
    reacts to a message with an emoji
    '''
    await message.add_reaction(emoji)
    

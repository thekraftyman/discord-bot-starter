# bot_init.py
# By: thekraftyman

# import packages
import discord
from discord.ext import commands
from src.lib.core_funcs import *
import re

class Bot_Init(commands.Cog):
    def __init__(self,client):
        self.client = client

    # ---------------------------
    # Add bot_init below

    @commands.Cog.listener() # for use with events
    async def on_ready(self):
        # print connection
        print(f'{self.client.user.name} has connected to Discord!')

        self.version = get_version()
        self.has_updated = has_updated()
        self.config = load_config()
        
        if self.has_updated:
            update_text = f'{self.client.user.name} has updated to version {get_version()} from version {last_version()}'

            # get changelog stuff
            changelog_version = f'## [{self.version}]'
            changes = []
            in_version = False
            with open( 'CHANGELOG.md', 'r' ) as infile:
                for line in infile:
                    is_version_line = bool(re.search("## \[\d+.\d+.\d+\] - \d{4}-\d+-\d+",line))
                    # within the correct version
                    if is_version_line and self.version in line:
                        in_version = True

                    # not in correct version
                    if is_version_line and in_version and not self.version in line:
                        in_version = False

                    if in_version:
                        changes.append(line)

            # filter newline-only lines
            changes = [line for line in changes if line != '\n']
            if changes:
                update_text = update_text + '\n```\n' + ''.join(changes) + '\n```'

            # print out the changes (You should put in a bot chat)
            print(update_text)

            # set the tmp version
            put_version()

    # Don't add below line
    # ---------------------------

# add the cog
def setup(client):
    client.add_cog(Bot_Init(client))

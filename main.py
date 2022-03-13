# main.py
# By: thekraftyman

# import packages
from discord.ext import commands
import discord
from src.lib.core_funcs import *

def main():
    # get the token and save it
    TOKEN = import_key()

    # a bot object used by discord add functions to it
    intents = discord.Intents.default()
    intents.members = True
    intents.messages = True
    intents.guilds = True
    client = commands.Bot(command_prefix="$", intent=intents)

    # modules to be loade
    modules = ['bot_init','commands','events','responses']
    loaded  = []

    # load the modules into the client
    for module in modules:
        try:
            client.load_extension(f'src.cogs.{module}')
            loaded.append(module)
        except Exception as error:
            print('{} could not be loaded: [{}]'.format(module,error))

    #print loaded modules
    loaded = ', '.join(loaded)
    print(f'Successfully loaded cogs: {loaded}')

    # run the bot
    client.run(TOKEN)

# run main() if this file is called by python
if __name__ == '__main__':
    main()

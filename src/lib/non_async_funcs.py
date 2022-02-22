# non_async_funcs.py
# By: thekraftyman
import json
from os import mkdir, path

def import_key():
    '''
    returns the authentication token for the bot
    '''
    with open('defaults/auth.json','r') as infile:
        return json.loads(infile.read())['token'] # returns the token as a string from auth.json

def tmp_check():
    '''
    creates the tmp file/dir if doesn't exist
    '''
    version_loc = load_config()['version_loc']
    version_loc_dir = '/'.join(version_loc.split('/')[:-1])
    # version folder doesn't exist, make it
    if not path.exists( version_loc_dir ):
        mkdir( version_loc_dir )

    # version file doesn't exist... make it
    if not path.exists( version_loc ):
        put_version()

def last_version():
    '''
    reads the last version saved in the tmp folder
    '''
    version_loc = load_config()['version_loc']
    with open( version_loc, 'r' ) as infile:
        return infile.read().strip()

def put_version():
    '''
    saves the current version to a tmp file
    '''
    version_loc = load_config()['version_loc']
    with open( version_loc, 'w' ) as outfile:
        outfile.write(get_version())

def load_config():
    '''
    loads the config file
    '''
    with open( 'defaults/config.json', 'r' ) as infile:
        return json.loads(infile.read())

def has_updated():
    '''
    returns the comparison of last and current versions
    '''
    tmp_check()

    if last_version() == get_version():
        return False
    return True

def get_version():
    '''
    returns the bot version as a string
    '''
    with open('version','r') as infile:
        return infile.read().strip()
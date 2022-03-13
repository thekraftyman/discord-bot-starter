# discord-bot-starter
A boiler-plate set for creating a discord bot in python using the discord.py package

## Setup

To start, you'll want to fork this repo so you can make your own edits.

In order to make the bot work with Discord, you'll need to fill the 

Next, you'll need to install the python packages included in the `requirements.txt` file. For example you can install it with:
```bash
$ python3 -m pip install -r requirements.txt
```

After that, you'll want to supply an authentication token in the `auth.json` file. This is generated from the [Discord developer application portal](https://discord.com/developers/applications).

Finally, you'll want to make the bot auto-run. For example, if you are running on a linux system, you can use cron to run the bot by adding this line to your crontab:
```
@reboot sudo sleep 60 && cd ~/discord-bot/ && python3 main.py
```
*note: this assumes your bot is in your home directory and you've titled it "discord-bot"*

## Contributing
Pull requests are welcome. Please read CONTRIBUTING.md for instructions.

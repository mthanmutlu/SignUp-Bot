import os
import discord
from discord.ext import commands
from discord_components import *
from components.settings import load_requirements
from utils.randomColor import randColor
from components.button import onClick


config = load_requirements()

TOKEN = os.environ.get('TOKEN')
prefix = config['prefix']
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)
# client.remove_command('help')
ddb = DiscordComponents(client)


@client.event
async def on_ready():
    print('Bot is online....')
    await onClick(client)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'**Loaded extension of {extension}**')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'**Unloaded extension of {extension}**')


if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.extensions
            client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)

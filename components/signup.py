import asyncio
import discord
from discord_components import *
from discord.ext import commands
from discord.channel import TextChannel, VoiceChannel
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.member import Member, VoiceState
from discord.message import Message
from utils.randomColor import randColor
from components.settings import load_requirements


async def signup(interaction: Interaction):
    guild = interaction.guild
    user = interaction.user
    member: Member = discord.utils.find(
        lambda m: m.id == user.id, guild.members)
    config = load_requirements()
    roles = []
    for role_id in config['roles']:
        role = discord.utils.find(lambda r: r.id == role_id, guild.roles)
        roles.append(role)
    else:
        await member.add_roles(*roles)

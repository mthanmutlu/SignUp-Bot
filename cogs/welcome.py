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


class Welcome(commands.Cog):
    def __init__(self, client: Bot) -> None:
        self.client = client
        self.config = load_requirements()

    @commands.has_permissions(administrator=True)
    @commands.command(name='welcome')
    async def send_welcome_message(self, ctx: Context):
        embed = discord.Embed(color=0x00ff33)
        embed.description = '**Hoş geldin. `Kayıt Ol` butonuna basarak devam edebilirsin.**'
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
        if self.config['message_image_url'] != '':
            embed.set_image(
                url=self.config['message_image_url'])
        message = await ctx.send(
            embed=embed,
            components=[
                [
                    Button(
                        label='✔ Kayıt Ol',
                        style=ButtonStyle.green,
                        id='signup-btn'
                    )
                ]
            ]
        )
        await ctx.message.delete()


def setup(client: Bot):
    client.add_cog(Welcome(client))

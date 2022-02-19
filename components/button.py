from discord import *
from discord.ext import commands
from discord_components import *
from components.signup import signup


async def onClick(client: commands.Bot):
    while True:
        interaction: Interaction = await client.wait_for('button_click')
        button_type = interaction.component.id
        if button_type == 'signup-btn':
            await interaction.respond(
                type=InteractionType.UpdateMessage,
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
            try:
                await signup(interaction)
            except Exception as err:
                print('Error =>', err)

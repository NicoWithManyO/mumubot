
import discord
from discord.ext import commands
from Helpers.eventUtils import auto_add_member_to_event, auto_remove_member_to_event
from event.models import Event

class Confirm(discord.ui.View):
    def __init__(self, instantiator, e):
        super().__init__()
        self.instantiator = instantiator
        self.e = e

    @discord.ui.button(label="S'inscrire", style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        event = Event.objects.filter(id=int(self.e))
        await auto_add_member_to_event(event[0], self.instantiator)
        self.stop()
        
    @discord.ui.button(label="S'enlever", style=discord.ButtonStyle.red)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        event = Event.objects.filter(id=int(self.e))
        await auto_remove_member_to_event(event[0], self.instantiator)
        self.stop()    


    # @discord.ui.button(label="no", style=discord.ButtonStyle.red)
    # async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
    #     if interaction.user == self.instantiator:
    #         self.value = False
    #         self.stop()
    #     else:
    #         await interaction.response.send_message(f"> 🚫 Désolé, {interaction.user.display_name}, seul {self.instantiator.display_name} peut faire cela !", ephemeral=False)

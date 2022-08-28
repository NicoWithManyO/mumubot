
import discord
from discord.ext import commands
from Helpers.eventUtils import auto_add_member_to_event, auto_remove_member_to_event
from event.models import Event
from Helpers.templatesToPublish import event_embed

class Confirm(discord.ui.View):
    def __init__(self, instantiator, e, confirmator):
        super().__init__()
        self.instantiator = instantiator
        self.e = e
        self.confirmator = confirmator

    @discord.ui.button(label="S'inscrire", style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        event = Event.objects.filter(id=int(self.e))
        await auto_add_member_to_event(event[0], interaction.user)
        await self.confirmator.edit(embed=await event_embed(event[0]) )
        await interaction.response.send_message(f"> ✅ `{interaction.user}` ajouté à l'évènement `{event[0]}`")
        # self.stop()
        
    @discord.ui.button(label="S'enlever", style=discord.ButtonStyle.red)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        event = Event.objects.filter(id=int(self.e))
        await auto_remove_member_to_event(event[0], interaction.user)
        await self.confirmator.edit(embed=await event_embed(event[0]) )
        await interaction.response.send_message(f"> 🚫 `{interaction.user}` retiré de `{event[0]}`")
        # self.stop() 

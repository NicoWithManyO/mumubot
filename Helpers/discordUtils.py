
import discord
from discord.ext import commands
from Helpers.eventUtils import auto_add_member_to_event, auto_remove_member_to_event
from event.models import Event
from Helpers.templatesToPublish import event_embed, details_event_embed

class Confirm(discord.ui.View):
    def __init__(self, instantiator, e, confirmator):
        super().__init__()
        self.value = None
        self.instantiator = instantiator
        self.e = e
        self.confirmator = confirmator
        self.event = Event.objects.filter(id=int(self.e))
        self.home = True

    @discord.ui.button(label="Inscription", style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        await auto_add_member_to_event(self.event[0], interaction.user)
        await self.confirmator.edit(embed=await event_embed(self.event[0]) )
        self.home = True
        await interaction.response.send_message(f"> ✅ `{interaction.user}` ajouté à l'évènement `{self.event[0]}`")
        
    @discord.ui.button(label="Désinscription", style=discord.ButtonStyle.red)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        
        await auto_remove_member_to_event(self.event[0], interaction.user)
        await self.confirmator.edit(embed=await event_embed(self.event[0]) )
        self.home = True
        await interaction.response.send_message(f"> 🚫 `{interaction.user}` retiré de `{self.event[0]}`")

    @discord.ui.button(label="Détails", style=discord.ButtonStyle.grey)
    async def details(self, button: discord.ui.Button, interaction: discord.Interaction):
        print(self.home)
        if not self.home:
            await self.confirmator.edit(embed=await event_embed(self.event[0]) )
            await interaction.response.send_message(f"> home de l'évènement", ephemeral=True)
            self.home = True
        else:
            await self.confirmator.edit(embed=await details_event_embed(self.event[0]))
            await interaction.response.send_message(f"> détails de l'évènement", ephemeral=True)
            self.home = False
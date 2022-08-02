import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import option

import django
from django.utils.text import slugify

from event.models import Event

class ReferentCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(name="addevent", description="(admin) Créer un évènement", guild_ids=[778509735397031936, 269040955380858880])
    async def addevent(self, ctx, name: str):
        temp = slugify(name)
        if Event.objects.filter(slug=temp).exists():
            await ctx.respond(f"> 🚫 L'évènement {name} existe déjà. {Event.objects.filter(slug=temp)} ")
            return
        to_save = Event(name=name, slug=temp)
        to_save.save()
        await ctx.respond(f"> ✅ {Event.objects.filter(slug=temp)}")

    @slash_command(name="event", guild_ids=[778509735397031936, 269040955380858880])
    async def event(self, ctx, option: str):
        if option == "list":
            for e in Event.objects.all():
                await ctx.send(f"{e}")
        await ctx.respond(f"> ✅ FIN")
            
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self} ready")

def setup(bot):
    bot.add_cog(ReferentCommand(bot))
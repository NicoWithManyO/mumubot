import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import option
from Helpers.eventUtils import auto_add_event, auto_add_member, auto_add_member_to_event
from Helpers.templates_to_publish import event_embed

import django
from django.utils.text import slugify

from member.models import Member
from event.models import Event

class ReferentCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(name="addevent", description="(admin) Créer un évènement", guild_ids=[778509735397031936, 269040955380858880])
    async def addevent(self, ctx, name: str):
        e = await auto_add_event(name, ctx.user)      
        if not e[1]:
            await ctx.respond(f"> 🚫 {e[0]} déjà existant")
        else:
            await ctx.respond(f"> ✅ {e[0]} ajouté")
    
    @slash_command(name="register", guild_ids=[778509735397031936, 269040955380858880])
    async def register(self, ctx, user_to_add: discord.Member=None):
        if not user_to_add:
            user_to_add = ctx.user
        m = await auto_add_member(user_to_add, ctx.guild)
        if not m[1]:
            await ctx.respond(f"> ✅ `{m[0]}` déjà existant")
        else:
            await ctx.respond(f"> ✅ `{m[0]}` ajouté")

    @slash_command(name="addme", guild_ids=[778509735397031936, 269040955380858880])
    async def addMe(self, ctx, event: int):
        e = Event.objects.filter(id=int(event))
        try:
            await auto_add_member_to_event(e[0], ctx.user)
            await ctx.respond(f"> ✅ `{ctx.user}` ajouté à l'évènement `{e[0]}`")
        except:
            await ctx.respond(f"> 🚫 error")

    @slash_command(name="view", guild_ids=[778509735397031936, 269040955380858880])
    async def view(self, ctx, event: str):
        try:
            e = Event.objects.filter(id=int(event))
            await ctx.send(embed=await event_embed(e[0]))
        except:
            await ctx.send(f"> 🚫 error, liste des events disponibles :")
            for e in Event.objects.all():
                await ctx.send(f"`{e}`")
        await ctx.respond(f"> ✅ end")

    @slash_command(name="viewevent", guild_ids=[778509735397031936, 269040955380858880])
    async def viewevent(self, ctx, option: str):
        try:
            option = int(option)
            o = Event.objects.filter(id=int(option))
            await ctx.send(f"inscrits")
            for m in o[0].engaged_members.all():
                await ctx.send(f"`{m.name}`")
            await ctx.respond(f"> ✅ `{Event.objects.filter(id=int(option))[0]}`")
        except:
            if option == "l":
                for e in Event.objects.all():
                    await ctx.send(f"`{e}`")
            await ctx.respond(f"> ✅ end")
     
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self} ready")

def setup(bot):
    bot.add_cog(ReferentCommand(bot))
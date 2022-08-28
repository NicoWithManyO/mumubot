import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import option
from Helpers.eventUtils import auto_add_event, auto_add_member, auto_add_member_to_event
from Helpers.templatesToPublish import event_embed
from Helpers.discordUtils import Confirm

import django
from django.utils.text import slugify

from member.models import Member
from event.models import Event
from event.admin import EventResource

class ReferentCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(name="temp", guild_ids=[778509735397031936, 269040955380858880])
    async def  temp(self, ctx):
        data = EventResource().export()
        await ctx.respond(data.csv)
    
    @slash_command(name="event", guild_ids=[778509735397031936, 269040955380858880])
    async def event(self, ctx, event: int):
        e = Event.objects.filter(id=int(event))
        if not e:
            await ctx.respond(f"> 🚫 L'évènement n'existe pas")
            for e in Event.objects.all():
                await ctx.send(f"`{e}`")
            return
        confirmator = await ctx.send("MuMuBot Event Module")
        await ctx.respond(f"event ok")
        view = Confirm(ctx.user, event, confirmator)
        await confirmator.edit(embed=await event_embed(e[0]), view=view)


    @slash_command(name="addevent", description="(admin) Créer un évènement", guild_ids=[778509735397031936, 269040955380858880])
    async def addevent(self, ctx, name: str):
        e = await auto_add_event(name, ctx.user)      
        if not e[1]:
            await ctx.respond(f"> 🚫 {e[0]} déjà existant")
        else:
            await ctx.respond(f"> ✅ {e[0]} ajouté")
    
    @slash_command(name="adduser", guild_ids=[778509735397031936, 269040955380858880])
    async def adduser(self, ctx, user_to_add: discord.Member=None):
        role = discord.utils.get(ctx.guild.roles, name="root")
        if role in ctx.user.roles:
            print("is root")
        if not user_to_add:
            user_to_add = ctx.user
        m = await auto_add_member(user_to_add, ctx.guild)
        if not m[1]:
            await ctx.respond(f"> ✅ `{m[0]}` déjà existant")
        else:
            await ctx.respond(f"> ✅ `{m[0]}` ajouté")

    @slash_command(name="addme", guild_ids=[778509735397031936, 269040955380858880])
    async def addme(self, ctx, event: int, user_to_add: discord.Member=None):
        e = Event.objects.filter(id=int(event))
        if not user_to_add:
            user_to_add = ctx.user
        try:
            await auto_add_member_to_event(e[0], user_to_add)
            await ctx.respond(f"> ✅ `{user_to_add.name}` ajouté à l'évènement `{e[0]}`")
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
     
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self} ready")

def setup(bot):
    bot.add_cog(ReferentCommand(bot))
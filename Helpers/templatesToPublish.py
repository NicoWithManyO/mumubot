
import discord, random

async def event_embed(event):
    e = discord.Embed(color=random.randint(0, 16777215))
    e.set_author(name=f"{event}")
    e.set_footer(text="EventManager")
    participants = []
    e.add_field(name=f":date: start", value=event.start_date, inline=False)
    e.add_field(name=f":timer:", value=event.duration, inline=False)
    if len(event.engaged_members.all()) > 0:
        for m in event.engaged_members.all():
            participants.append(f"▶️ {m.name}")
        e.add_field(name=f"Inscrits ({len(event.engaged_members.all())})", value='\n'.join(participants))
    else:
        e.add_field(name=f"Inscrits", value="aucun")
    return e

async def details_event_embed(event):
    e = discord.Embed(color=random.randint(0, 16777215))
    e.set_author(name=f"{event}")
    e.set_footer(text="EventManager")
    e.add_field(name=f":timer: duration", value=event.duration, inline=False)
    e.add_field(name=f":date: start", value=event.start_date, inline=True)
    e.add_field(name=f":date: end", value=event.end_date, inline=True)
    e.add_field(name=f"event owner", value=event.owner, inline=False)
    e.add_field(name=f"is public", value=event.is_public, inline=False)
    e.add_field(name=f"number participants", value=len(event.engaged_members.all()), inline=True)
    e.add_field(name=f"max size", value=event.max_participants, inline=True)
    return e
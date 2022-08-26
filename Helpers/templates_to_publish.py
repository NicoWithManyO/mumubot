
import discord, random

async def event_embed(event):
    e = discord.Embed(color=random.randint(0, 16777215))
    e.set_author(name=f"{event}")
    e.set_footer(text="EventManager")
    participants = []
    if len(event.engaged_members.all()) > 0:
        for m in event.engaged_members.all():
            participants.append(f"▶️ {m.name}")
        e.add_field(name=f"Inscrits", value='\n'.join(participants))
    else:
        e.add_field(name=f"Inscrits", value="aucun")
    return e
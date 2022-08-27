from event.models import Event
from member.models import Member
from django.utils.text import slugify

async def auto_add_member(member, origin):
    return Member.objects.get_or_create(discord_id=member.id, name=member.display_name, discriminator=member.discriminator, guild=origin)
    
async def auto_add_event(event, owner):
    g = Event.objects.get_or_create(name=event)
    if g[1]:
        g[0].owner = Member.objects.all().filter(discord_id=owner.id)[0]
        g[0].save()
    return g

async def auto_add_member_to_event(event, member):
    m = Member.objects.all().filter(discord_id=member.id)
    event.engaged_members.add(m[0])
    return m

async def auto_remove_member_to_event(event, member):
    m = Member.objects.all().filter(discord_id=member.id)
    event.engaged_members.remove(m[0])
    return m


    
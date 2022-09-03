from event.models import Event
from member.models import Member, Guild
from django.utils.text import slugify

async def auto_add_member(member, origin):
    g = Guild.objects.all().filter(discord_id=origin.id)
    return Member.objects.get_or_create(discord_id=member.id, name=member.display_name, discriminator=member.discriminator, guild=origin, origin=g[0])
    
async def auto_add_event(event, owner, origin):
    g = Guild.objects.all().filter(discord_id=origin.id)
    e = Event.objects.get_or_create(name=event, origin=g[0])
    if e[1]:
        e[0].owner = Member.objects.all().filter(discord_id=owner.id)[0]
        e[0].save()
    return e

async def auto_add_member_to_event(event, member):
    m = Member.objects.all().filter(discord_id=member.id)
    event.engaged_members.add(m[0])
    return m

async def auto_remove_member_to_event(event, member):
    m = Member.objects.all().filter(discord_id=member.id)
    event.engaged_members.remove(m[0])
    return m


    
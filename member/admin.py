from django.contrib import admin
from .models import Member, Guild

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    pass

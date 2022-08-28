from django.contrib import admin
from import_export import resources
from .models import Event
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class EventResource(resources.ModelResource):
    class Meta:
        model = Event

class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource
admin.site.register(Event, EventAdmin)
from django.contrib import admin

from apps.events.models import Location, Event


class LocationAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)

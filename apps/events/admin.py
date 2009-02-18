from django.contrib import admin

from apps.events.models import Location, Event


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'post_code')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('title', 'date', 'location')
    list_display_filter = ('location',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'copy')


admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)

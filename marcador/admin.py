from django.contrib import admin

from .models import Route, Tag


class RouteAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'is_public', 'date_updated')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'owner__username')
    search_fields = ['url', 'title', 'latitude','longitude']
    readonly_fields = ('date_created', 'date_updated')


admin.site.register(Route, RouteAdmin)
admin.site.register(Tag)

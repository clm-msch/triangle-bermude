from django.contrib import admin

from . import models

# admin.site.register(models.Event)
admin.site.register(models.Occurrence)
admin.site.register(models.Price_type)
admin.site.register(models.Access_type)
admin.site.register(models.Tag)
admin.site.register(models.Audience)
admin.site.register(models.Group)
# admin.site.register(models.Adresse)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_description', 'group_id', 'display_tags')
    search_fields = ['title']
    
    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    display_tags.short_description = "Tags"
    list_filter = ['tags', 'group_id']
    
admin.site.register(models.Event, EventAdmin)

class AdresseAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'address_street', 'address_zipcode')
    search_fields = ['address_name']
    list_filter = ['address_name']

admin.site.register(models.Adresse, AdresseAdmin)
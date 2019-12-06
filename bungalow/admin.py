from django.contrib import admin
from .models import PropertyModel

# change the admin list display so it's not quite as ugly
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('zillow_id', 'address', 'state', 'city', 'zipcode')
admin.site.register(PropertyModel, PropertyModelAdmin)

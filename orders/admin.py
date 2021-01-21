from django.contrib import admin

from .models import *


# @admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'actors', 'description', 'position', 'department', 'created_at', 'updated_at', 'is_published',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(Actor)
admin.site.register(Position)
admin.site.register(Department)

from django.contrib import admin
from .views import *

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ComponentsAdmin(admin.ModelAdmin):
    list_display = ("comp_name", "amount", "category")
    list_display_links = ("comp_name", "amount")
    fields = ("comp_name", "amount", "category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("cat_name",)
    fields = ("cat_name",)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("device_name", )


class ConnectionAdmin(admin.ModelAdmin):
    list_display = ("device_id", )


admin.site.register(Components, ComponentsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Devices, DeviceAdmin)
admin.site.register(Connection, ConnectionAdmin)

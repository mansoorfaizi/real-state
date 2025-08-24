from django.contrib import admin
from .models.area import Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "district", "timestamp")   
    search_fields = ("name",)                                
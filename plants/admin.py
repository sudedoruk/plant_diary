from django.contrib import admin

# Register your models here.
from .models import Plant,CareLog


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ["name", "added_date"]
    list_filter = ["added_date"]
    search_fields =["name"]
   


@admin.register(CareLog)
class CareLogAdmin(admin.ModelAdmin):
    list_display = ["plant", "date"]
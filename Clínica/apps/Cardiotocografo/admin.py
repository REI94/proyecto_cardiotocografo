from django.contrib import admin

# Register your models here.
from .models import Historia

class HistoriaAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'enfermedad_padecida',]
    list_display = ('codigo','enfermedad_padecida',)

admin.site.register (Historia, HistoriaAdmin)
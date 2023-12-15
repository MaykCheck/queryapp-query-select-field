from django.contrib import admin
from queryapp.models import Devlet, Şehirler

# Register your models here.

class DevletAdmin(admin.ModelAdmin):
    list_display = ('ülke', 'başkent')
    prepopulated_fields = {"slug": ('ülke','başkent',)}

admin.site.register(Devlet, DevletAdmin)

admin.site.register(Şehirler)
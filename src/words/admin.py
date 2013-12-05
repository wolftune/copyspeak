from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'alignment')
    list_filter = ('alignment',)
    prepopulated_fields = {"slug": ("word",)}

admin.site.register(Word, WordAdmin)

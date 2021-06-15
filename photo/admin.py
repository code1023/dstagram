from django.contrib import admin

from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_date', 'updated_date']
    raw_id_fields = ['author']
    list_filter = ['created_date', 'updated_date', 'author']
    search_fields = ['text', 'created_date']
    ordering = ['-updated_date', '-created_date']


admin.site.register(Photo, PhotoAdmin)

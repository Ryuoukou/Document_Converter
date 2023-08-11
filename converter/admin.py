from django.contrib import admin
from .models import MyDocument


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'converted_file')
    search_fields = ('title',)
    list_filter = ('converted_file',)
    ordering = ('-id',)


admin.site.register(MyDocument, DocumentAdmin)

from django.contrib import admin

from quotidian import models


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('content', 'source', 'public')
    list_filter = ('public',)
    search_fields = ('content',)


# Register models
admin.site.register(models.Quote, QuoteAdmin)

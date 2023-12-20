from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show'
    # ordering = 'id', #-id
    # list_filter = 'created_date',
    # search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'first_name', 'last_name', 'show'
    # list_display_links = 'id', 'phone',
    ...

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
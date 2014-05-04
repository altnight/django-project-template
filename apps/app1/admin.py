# -*- coding: utf-8 -*-
from django.contrib import admin

from {{ app_name }}.models import {{ app_name|title }}


# class {{ app_name|title }}Admin(admin.ModelAdmin):
    # list_display = ()

# admin.site.register({{ app_name|title }}, {{ app_name|title }}Admin)
admin.site.register({{ app_name|title }})

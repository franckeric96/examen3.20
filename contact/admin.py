from django.contrib import admin

# Register your models here.

from . import models

from autres.actions import Action


class ContactAdmin(Action):
    list_display = ('name','email', 'subject',
                    'date_add', 'date_update', 'status')
    list_filter = ('name', )
    search_fields = ('name', )
    date_hierarchy = 'date_add'
    list_display_links = ['name']
    ordering = ['date_add']
    list_per_page = 15
    fieldsets = [('Info Contact', {'fields': ['name','email', 'subject', 'message']}),
                 ('Standard', {'fields': ['status']})
                 ]


class NewsletterAdmin(Action):
    list_display = ('email','date_add', 'date_update', 'status')
    list_per_page = 10
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    ordering = ['date_add']



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.Newsletter, NewsletterAdmin)
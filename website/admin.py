from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from autres.actions import Action


# Register your models here.



class PresentationAdmin(Action):
    list_display = ('images_view', 'nom', 'date_add',
                    'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Presentation', {'fields': ['nom', 'description', 'logo', 'message_welcome']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.logo.url))







class InfositeAdmin(Action):
    list_display = ('image','nom', 'numero', 'date_add','date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['numero']
    ordering = ['nom']
    list_per_page = 10

    fieldsets = [
        ('Info Infosite', {
            'fields': ['nom', 'adress','numero','email','site','message','image']
        }),
        ('Standard', {
            'fields': ['status']
        })
    ]


    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Infosite, InfositeAdmin)
_register(models.Presentation, PresentationAdmin)


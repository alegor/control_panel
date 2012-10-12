# -*-encoding: utf-8 -*-
from django.contrib import admin
from library.models import *

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name',
		                'email')
	list_display_links = ('first_name', 'last_name')                                             
	list_editable = ('email',)                                              
	ordering  = ('last_name', 'first_name')  
                                                                             
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'print_version',
                        'publisher')
	list_display_links = ('title',)                                             
	list_editable = ('publisher',)                                              
	list_filter = ('authors', 'publisher',
                        'publication_date')
	ordering  = ('publication_date',)                                                      
	search_fields = ('title',)                      
	date_hierarchy = 'publication_date'		      
	fieldsets = (
		(None, {'fields': ('title', 'authors')}),
		('Выходные данные', {
		'description': u'Данные об издательстве и издании',
		'fields': ('publisher', 'publication_date'),
		}),
		    )
admin.site.register(Book)


class PublisherAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'address',
		                'city', 'country', 'website',)
	list_display_links = ('title',)                                             
	list_editable = ('country',) 
	list_editable = ('city',)                                              
	list_filter = ('country', )
	list_filter = ('city', )
	ordering  = ('title',)                                                      
	search_fields = ('title',) 
        fieldsets = (
                        (None, {'fields': ('country', 'city', 'address')}),
                        ('Контактная информация', {
                            'description': u'Данные об издательстве и издании',
                            'fields': ('country', 'city', 'address'),
                            }),
                    )                  
admin.site.register(Publisher)



from django.contrib import admin

from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['book_name', 'author_name', 'book_type', 'edition']}),
        ('Library Contains', {'fields': ['no_of_books']})
    ]
    list_filter = ['book_type']
    search_fields = ['book_name', 'author_name', 'book_type']


admin.site.register(Book, BookAdmin)
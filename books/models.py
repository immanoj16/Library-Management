from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Book(models.Model):
    isbn_no = models.CharField(max_length=100, null=False)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    book_type = models.CharField(max_length=50)
    edition = models.IntegerField()
    no_of_books = models.IntegerField()

    def __unicode__(self):
        return self.book_name

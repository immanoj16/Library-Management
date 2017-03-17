from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


BRANCH_CHOICES = (
    ('B.Tech', 'B.Tech'),
    ('MCA', 'MCA'),
)

YEAR_CHOICES = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    roll_no = models.CharField(max_length=10)
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=6)
    year = models.CharField(choices=YEAR_CHOICES, max_length=3)
    birth_date = models.DateField(blank=False, null=False)
    phone = models.CharField(max_length=10, default='')


class Book(models.Model):
    isbn_no = models.CharField(max_length=100, null=False)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    book_type = models.CharField(max_length=50)
    edition = models.IntegerField()
    no_of_books = models.IntegerField()

    def __unicode__(self):
        return self.book_name

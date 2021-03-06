from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     roll_no = models.CharField(max_length=10)
#     branch = models.CharField(choices=BRANCH_CHOICES, max_length=6)
#     year = models.CharField(choices=YEAR_CHOICES, max_length=3)
#     birth_date = models.DateField(blank=False, null=False)
#     phone = models.CharField(max_length=10, default='')

BOOK_CHOICES = (
    ('Programming', 'Programming'),
    ('Computer', 'Computer'),
    ('Math', 'Math'),
    ('Economics', 'Economics'),
    ('Accounting', 'Accounting'),
    ('Others', 'Others')
)


class Book(models.Model):
    isbn_no = models.CharField(max_length=100, null=False)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    book_type = models.CharField(max_length=15, choices=BOOK_CHOICES)
    edition = models.IntegerField()
    no_of_books = models.IntegerField()

    def __unicode__(self):
        return self.book_name

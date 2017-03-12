from django import forms
from django.contrib.auth.models import User
from .models import Book


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class BookForm(forms.Form):
    # to take the input of username
    isbn_no = forms.CharField(max_length=100)
    book_name = forms.CharField(max_length=100)
    author_name = forms.CharField(max_length=100)
    book_type = forms.CharField(max_length=50)
    edition = forms.IntegerField()
    no_of_books = forms.IntegerField()


class RemoveBookForm(forms.Form):
    isbn_no = forms.CharField(max_length=100)

    class Meta:
        model = Book
        fields = ['isbn_no']
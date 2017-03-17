from django import forms
from django.contrib.auth.models import User
from .models import Book, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name',]


class DateInput(forms.DateInput):
    input_type = 'date'


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


class UserProfileForm(forms.ModelForm):
    branch = forms.ChoiceField(choices=BRANCH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)

    class Meta:
        model = UserProfile
        fields = ['roll_no', 'branch', 'year', 'birth_date', 'phone']
        widgets = {
            'birth_date': DateInput(),
        }


class BookForm(forms.Form):
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
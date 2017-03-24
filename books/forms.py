from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book, Profile


class UserForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )


# class DateInput(forms.DateInput):
#     input_type = 'date'


# BRANCH_CHOICES = (
#     ('B.Tech', 'B.Tech'),
#     ('MCA', 'MCA'),
# )

# YEAR_CHOICES = (
#     ('1st', '1st'),
#     ('2nd', '2nd'),
#     ('3rd', '3rd'),
#     ('4th', '4th'),
#     ('5th', '5th'),
# )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location')


# class ProfileForm(forms.ModelForm):
#     branch = forms.ChoiceField(choices=BRANCH_CHOICES)
#     year = forms.ChoiceField(choices=YEAR_CHOICES)

#     class Meta:
#         model = Profile
#         fields = ['roll_no', 'branch', 'year', 'birth_date', 'phone']
#         widgets = {
#             'birth_date': DateInput(),
#         }

BOOK_CHOICES = (
    ('Programming', 'Programming'),
    ('Computer', 'Computer'),
    ('Math', 'Math'),
    ('Economics', 'Economics'),
    ('Accounting', 'Accounting'),
    ('Others', 'Others')
)


class BookForm(forms.Form):
    isbn_no = forms.CharField(max_length=100)
    book_name = forms.CharField(max_length=100)
    author_name = forms.CharField(max_length=100)
    book_type = forms.ChoiceField(choices=BOOK_CHOICES)
    edition = forms.IntegerField()
    no_of_books = forms.IntegerField()


class RemoveBookForm(forms.Form):
    isbn_no = forms.CharField(max_length=100)

    class Meta:
        model = Book
        fields = ['isbn_no']
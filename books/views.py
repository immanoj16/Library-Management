from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout

from .forms import UserForm, BookForm, RemoveBookForm
from .models import Book


def home(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')

    username = request.user.username
    book_list = Book.objects.order_by('book_name')[:50]
    return render(request, 'books/home.html', {'book_list': book_list, 'username': username})


def detail(request, book_id):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')

    username = request.user.username
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book, 'username': username})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'books/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                book_list = Book.objects.order_by('id')[:50]
                username = request.user.username
                return render(request, 'books/home.html', {'book_list': book_list, 'username': username, })
            else:
                return render(request, 'books/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'books/login.html', {'error_message': 'Invalid login'})
    return render(request, 'books/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'books/home.html', {})
    context = {
        'form': form,
    }
    return render(request, 'books/register.html', context)


def addbook(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')

    username = request.user.username
    if username == 'kanhu':
        if request.method == 'GET':

            form = BookForm(request.GET)

            if form.is_valid():

                isbn_no = request.GET.get('isbn_no', '')
                book_name = request.GET.get('book_name', '')
                author_name = request.GET.get('author_name', '')
                book_type = request.GET.get('book_type', '')
                edition = request.GET.get('edition', '')
                no_of_books = request.GET.get('no_of_books', '')

                book = Book(
                    isbn_no=isbn_no,
                    book_name=book_name,
                    author_name=author_name,
                    book_type=book_type,
                    edition=edition,
                    no_of_books=no_of_books
                )
                book.save()

                book_list = Book.objects.order_by('book_name')[:50]

                context = {
                    'success_message': "New book is added",
                    'book_list': book_list,
                    'username': username,
                }
                return render(request, 'books/home.html', context)
            else:
                return render(request, 'books/addbook.html', {'error_message': "Data is invalid"})


def removeBook(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')

    username = request.user.username
    if username == 'kanhu':

        if request.method == 'GET':
            form = RemoveBookForm(request.GET)

            if form.is_valid():
                isbn_no = request.GET.get('isbn_no','')
                try:
                    book = Book.objects.get(isbn_no=isbn_no)
                    book.delete()
                    book_list = Book.objects.order_by('book_name')[:50]
                    context = {
                        'success_message': "The book is removed",
                        'book_list': book_list,
                        'username': username,
                    }
                    return render(request, 'books/home.html', context)
                except:
                    return render(request, 'books/removebook.html', {'error_message': "Give correct Id or Name"})
            else:
                return render(request, 'books/removebook.html', {'error_message': "Give correct Id or Name"})


def search(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')

    username = request.user.username
    try:
        query = request.GET['book_name']
        if Book.objects.filter(book_name__startswith=query):
            book_list = Book.objects.filter(book_name__startswith=query)
            return render(request, 'books/search.html', {'book_list': book_list, 'username': username})
        if User.objects.filter(username__startswith=query):
            user_list = User.objects.filter(username__startswith=query)
            return render(request, 'books/search.html', {'user_list': user_list, 'username': username})
        else:
            context = {
                'book_list': Book.objects.order_by('book_name')[:50],
                'username': username,
            }
            return render(request, 'books/home.html', context)
    except:
        book_list = Book.objects.order_by('book_name')[:50]
        context = {
            'error_message': "Please Give the book name or username",
            'book_list': book_list,
            'username': username,
        }
        return render(request, 'books/home.html', context)


def profile(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')

    username = request.user.username
    user = User.objects.get(username=username)
    return render(request, 'books/profile.html', {'user': user, 'username': username,})

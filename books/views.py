from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import logout

from .forms import UserForm, ProfileForm, BookForm, RemoveBookForm
from .models import Book


@login_required
def home(request):
    username = request.user.username
    book_list = Book.objects.order_by('book_name')[:50]
    return render(request, 'books/home.html', {'book_list': book_list, 'username': username})


def detail(request, book_id):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')

    username = request.user.username
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book, 'username': username})


# def logout_user(request):
#     logout(request)
#     user_form = UserForm(request.POST or None)
#     context = {
#         "user_form": user_form,
#     }
#     return render(request, 'books/login.html', context)


# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 book_list = Book.objects.order_by('book_name')[:50]
#                 username = request.user.username
#                 return render(request, 'books/home.html', {'book_list': book_list, 'username': username, })
#             else:
#                 return render(request, 'books/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'books/login.html', {'error_message': 'Invalid login'})
#     return render(request, 'books/login.html')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.profile.bio = profile_form.cleaned_data.get('bio')
            user.profile.location = profile_form.cleaned_data.get('location')
            user.profile.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = user_form.cleaned_data.get('birth_date')
            user.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def addbook(request):
    username = request.user.username
    if username == 'admin':
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


@login_required
def removeBook(request):
    username = request.user.username
    if username == 'admin':

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


@login_required
def search(request):
    username = request.user.username
    query = request.GET['book_name']
    if query:
        book_list = Book.objects.filter(Q(book_name__icontains=query)).distinct()
        user_list = User.objects.filter(Q(username__startswith=query)).distinct()
        context = {
            'book_list': book_list,
            'user_list': user_list,
            'username': username,
        }
        return render(request, 'books/search.html', context)
    else:
        book_list = Book.objects.order_by('book_name')[:50]
        context = {
            'error_message': "Please Give the book name or username",
            'book_list': book_list,
            'username': username,
        }
        return render(request, 'books/home.html', context)


@login_required
def profile(request):
    username = request.user.username
    user = User.objects.get(username=username)
    return render(request, 'books/profile.html', {'user': user, 'username': username,})


def edit(request):

    if request.POST.get('username'):
        username = request.POST.get('username','')
        user = User.objects.get(username=request.user.username)
        user.username = username
        user.save()

        context = {
            'user': User.objects.get(username=username),
            'username': username,
            'success_message': "Username is changed successfully",
        }
        return render(request, 'books/profile.html', context)

    elif request.POST.get('email'):
        email = request.POST.get('email','')
        user = User.objects.get(username=request.user.username)
        user.email = email
        user.save()

        context = {
            'user': User.objects.get(username=request.user.username),
            'success_message': "Email is changed successfully",
        }
        return render(request, 'books/profile.html', context)

    else:
        if request.user.check_password(request.POST['opassword']):
            npassword = request.POST.get('npassword','')
            cpassword = request.POST.get('cpassword','')

            username = request.user.username
            user = User.objects.get(username=username)

            if npassword == cpassword:
                user.set_password(npassword)
                user.save()

                context = {
                    'user': user,
                    'success_message': "Password is successfully changed."
                }
                return render(request, 'books/profile.html', context)
            else:
                context = {
                    'user': user,
                    'error_message': "Didn't match password!!!"
                }
                return render(request, 'books/profile.html', context)
        else:
            user = User.objects.get(username=request.user.username)
            context = {
                'user': user,
                'error_message': "Old password was incorrect!!!"
            }
            return render(request, 'books/profile.html', context)


def adduser(request):
    if not request.user.is_authenticated():
        return render(request, 'books/login.html')

    username = request.user.username
    if username == 'admin':
        if request.method == 'POST':

            form = BookForm(request.GET)

            if form.is_valid():



                book = User(

                )
                book.save()



                context = {
                    'success_message': "New book is added",
                    'user_list': user_list,
                    'username': username,
                }
                return render(request, 'books/home.html', context)
            else:
                return render(request, 'books/addbook.html', {'error_message': "Data is invalid"})
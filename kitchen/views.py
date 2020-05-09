from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from api.models import Category, Course, Topic, Content


# Create your views here.
def index(request):
    logout(request)
    return render(request, 'kitchen/index.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return render(request, 'kitchen/awaiting.html')
    else:
        return render(request, 'kitchen/index.html')

def authLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('kitchen:dashboard'))
    else:
        return HttpResponseRedirect(reverse('index'))


@login_required
def dashboard(request):
    return render(request, 'kitchen/dashboard.html')

# category
def category(request):
    categories = Category.objects.all()
    return render(request, 'kitchen/categories.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Category.objects.create(title=title, description=description)
        return HttpResponseRedirect(reverse('kitchen:category'))
    return render(request, 'kitchen/add_category.html')

def update_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category.title = title
        category.description = description
        category.save()
        return HttpResponseRedirect(reverse('kitchen:category'))
    return render(request, 'kitchen/update_category.html', {'category': category})

# course
def course(request):
    courses = Course.objects.all()
    return render(request, 'kitchen/courses.html', {'courses': courses})

def add_course(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        cat = request.POST.get('category')
        category = Category.objects.get(pk=cat)
        title = request.POST['title']
        code = request.POST['code']
        description = request.POST['description']
        Course.objects.create(category=category, title=title, code=code, description=description)
        return HttpResponseRedirect(reverse('kitchen:course'))
    return render(request, 'kitchen/add_course.html', {'categories': categories})

def update_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        title = request.POST['title']
        code = request.POST['code']
        description = request.POST['description']
        course.title = title
        course.code = code
        course.description = description
        course.save()
        return HttpResponseRedirect(reverse('kitchen:course'))
    return render(request, 'kitchen/update_course.html', {
        'course': course, 
    })
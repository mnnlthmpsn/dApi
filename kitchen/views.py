from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from api.models import Category, Course, Topic, Content
from .models import Profile


# Create your views here.
def index(request):
    logout(request)
    return render(request, 'kitchen/index.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            User.objects.create_user(username=username, email=email, password=password)
            return render(request, 'kitchen/awaiting.html')
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
@login_required
def category(request):
    categories = Category.objects.all()
    return render(request, 'kitchen/categories.html', {'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Category.objects.create(title=title, description=description)
        return HttpResponseRedirect(reverse('kitchen:category'))
    return render(request, 'kitchen/add_category.html')

@login_required
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
@login_required
def course(request):
    courses = Course.objects.all()
    return render(request, 'kitchen/courses.html', {'courses': courses})

@login_required
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

@login_required
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

# topic
@login_required
def topic(request):
    topics = Topic.objects.all()
    return render(request, 'kitchen/topics.html', {'topics': topics})

@login_required
def add_topic(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        crs = request.POST.get('course')
        course = Course.objects.get(pk=crs)
        title = request.POST['title']
        description = request.POST['description']
        Topic.objects.create(course=course, title=title, description=description)
        return HttpResponseRedirect(reverse('kitchen:topic'))
    return render(request, 'kitchen/add_topic.html', {'courses': courses})

@login_required
def update_topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        topic.title = title
        topic.description = description
        topic.save()
        return HttpResponseRedirect(reverse('kitchen:topic'))
    return render(request, 'kitchen/update_topic.html', {
        'topic': topic, 
    })

# content
@login_required
def content(request):
    contents = Content.objects.all()
    return render(request, 'kitchen/contents.html', {'contents': contents})

@login_required
def add_content(request):
    topics = Topic.objects.all()
    if request.method == 'POST':
        tpc = request.POST.get('topic')
        topic = Topic.objects.get(pk=tpc)
        content = request.POST['content']
        Content.objects.create(topic=topic, content=content)
        return HttpResponseRedirect(reverse('kitchen:content'))
    return render(request, 'kitchen/add_content.html', {'topics': topics})

@login_required
def update_content(request, content_id):
    content = Content.objects.get(pk=content_id)
    if request.method == 'POST':
        content_from_template = request.POST['content']
        content.content = content_from_template
        content.save()
        return HttpResponseRedirect(reverse('kitchen:content'))
    return render(request, 'kitchen/update_content.html', {
        'content': content, 
    })

# user settings
@login_required
def settings(request):
    return render(request, 'kitchen/settings.html')

@login_required
def update_settings(request):
    if request.method == 'POST':
        """
        note: Username has been disabled to avoid
        conflicts when changing.
        Accept inputs from templates, below
        """
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        

        # save user
        user = User.objects.get(id=request.user.id)
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.save()
        return HttpResponseRedirect(reverse('kitchen:settings'))
    return render(request, 'kitchen/settings.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user.id
        school = request.POST['school']
        dob = request.POST['dob']
        phone = request.POST['phone']

        profile = Profile.objects.get(id=request.user.profile.id)
        profile.school = school
        profile.date_of_birth = dob
        profile.phone = phone
        profile.save()
        return HttpResponseRedirect(reverse('kitchen:settings'))
    return render(request, 'kitchen/settings.html')

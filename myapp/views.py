from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import MyModel
from django.http import HttpResponse
from .form import MyModelForm
from rest_framework import viewsets
from .serializers import MyModelSerializer


def home(request):
    return HttpResponse("Welcome to the Home Page!")

def list_posts(request):
    # Retrieve all objects from MyModel
    posts = MyModel.objects.all()
    
    # Pass the objects to the template
    return render(request, 'list.html', {'posts': posts})

class PostListView(ListView):
    model = MyModel
    template_name = 'list.html'
    context_object_name = 'posts'


def create_mymodel(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the post list view
    else:
        form = MyModelForm()
    
    return render(request, 'create_mymodel.html', {'form': form})

def create_object(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        new_object = MyModel.objects.create(
            name=name,
            age=age,
            email=email,
            first_name=first_name,
            last_name=last_name,
            address=address
        )
        new_object.save()
        return redirect('post_list')  # Redirect to a list view or success page

    return render(request, 'create_object.html')

def get_object(request, object_id):
    try:
        object_instance = MyModel.objects.get(id=object_id)
    except MyModel.DoesNotExist:
        object_instance = None
    return render(request, 'get_object.html', {'object_instance': object_instance})

def update_object(request, object_id):
    try:
        object_instance = MyModel.objects.get(id=object_id)

        if request.method == 'POST':
            object_instance.name = request.POST.get('name')
            object_instance.age = request.POST.get('age')
            object_instance.email = request.POST.get('email')
            object_instance.first_name = request.POST.get('first_name')
            object_instance.last_name = request.POST.get('last_name')
            object_instance.save()
            return redirect('post_list')  # Redirect to a list view or success page
    except MyModel.DoesNotExist:
        object_instance = None

    return render(request, 'update_object.html', {'object_instance': object_instance})

def delete_object(request, object_id):
    try:
        object_instance = MyModel.objects.get(id=object_id)
        if request.method == 'POST':
            object_instance.delete()
            return redirect('post_list')  # Redirect to a list view or success page
    except MyModel.DoesNotExist:
        object_instance = None

    return render(request, 'delete_object.html', {'object_instance': object_instance})

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
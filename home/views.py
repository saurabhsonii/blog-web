from django.shortcuts import render
from .form import *
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')

def blog_post(request):
    return render(request, "single-post.html")


def UserRegister(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Process the data
            data = form.cleaned_data
            # Perform operations with data...
            # Redirect or render a success template
            return render(request, 'success.html')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})
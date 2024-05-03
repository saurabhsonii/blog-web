from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')

def blog_post(request):
    return render(request, "single-post.html")
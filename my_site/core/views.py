from django.shortcuts import render

# Create your views here.
def splash(request):
    return render(request, "splash.html", {})

def about_me(request):
    return render(request, "about_me.html", {})

def teaching(request):
    return render(request, "teaching.html", {})

def music(request):
    return render(request, "music.html", {})

def projects(request):
    return render(request, "projects.html", {})

def career(request):
    return render(request, "career.html", {})

def blog(request):
    return render(request, "blog.html", {})

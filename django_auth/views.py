from django.shortcuts import render, redirect

from search.models import User


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        if User.objects.filter(username=username, password=password):
            request.session["username"] = username
            return redirect("/index/")

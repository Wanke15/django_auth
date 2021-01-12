from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    ctx = {}
    if request.method == "GET":
        username = request.session.get("username")
        if username:
            ctx["username"] = username
            return render(request, 'index.html', context=ctx)
        else:
            return redirect("/login")

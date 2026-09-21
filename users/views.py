from django.shortcuts import redirect, render

from users.forms import RegisterForm
from django.contrib.auth import authenticate, login


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(
                request,
                "users/register_success.html"
            )

    else:
        form = RegisterForm()

    return render(
        request,
        "users/register.html",
        {"form": form},
    )


def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            return redirect("home")

    return render(
        request,
        "users/login.html"
    )
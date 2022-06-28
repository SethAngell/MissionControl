# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            if form.cleaned_data.get("phone_number")[:2] != "+1":
                form.cleaned_data[
                    "phone_number"
                ] = f'+1{form.cleaned_data["phone_number"]}'
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(request, email=user.email, password=raw_password)

            user.name = form.cleaned_data.get("name")
            user.save()

            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect("home")
        else:
            return render(request, "registration/signup.html", {"form": form})

    else:
        form = CustomUserCreationForm()
        return render(request, "registration/signup.html", {"form": form})

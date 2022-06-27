from django.db.models import Case, When
from django.shortcuts import render


def HomepageView(request):
    return render(request, "polls/home.html", {})

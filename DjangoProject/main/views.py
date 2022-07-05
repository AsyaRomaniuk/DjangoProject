from django.shortcuts import render
from django.db import connection
from .models import User


def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def index(request):
    # users = User.objects.all()
    # HttpResponse("<h1>Привіт, світ!</h1>")
    # Model.objects.all().order_by('business_id', '-date').distinct('business_id')
    # a = User.objects.all().order_by('creation_date', '-date')
    with connection.cursor() as cursor:
        query = """
            SELECT name, creation_date, profile FROM main_user
            ORDER BY creation_date DESC LIMIT 3
            """
        cursor.execute(query)
        context = {
            "recent_users": dictfetchall(cursor),
        }
    return render(request, "main/index.html", context)  # , {"title": "Головна сторінка", "user": "users"})


def about(request):
    return render(request, "main/about.html")


def devProjects(request):
    return render(request, "main/devProjects.html")


def traitorsList(request):
    return render(request, "main/traitorsList.html")


def signIn(request):
    return render(request, "main/signIn.html")


def signUp(request):
    return render(request, "main/signUp.html")
# Create your views here.

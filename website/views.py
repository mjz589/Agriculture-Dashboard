from django.shortcuts import render
from .models import *
# Create your views here.

def dashboard_view(request, *args, **kwargs):
    projects = Project.objects.all()
    done_projects = Project.objects.filter(completion=100).count()
    context = {'projects':projects , 'done_projects':done_projects}
    return render(request, 'dashboard.html', context)

def billing_view(request, *args, **kwargs):
    return render(request, 'billing.html')

def notifications_view(request, *args, **kwargs):
    return render(request, 'notifications.html')

def tables_view(request, *args, **kwargs):
    return render(request, 'tables.html')

def weather_view(request, *args, **kwargs):
    return render(request, 'weather.html')
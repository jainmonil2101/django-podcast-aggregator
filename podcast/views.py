from django.shortcuts import render, redirect
from .models import Episode
from django.core.paginator import Paginator
from selenium import webdriver

# Create your views here.

def index(request):
    if request.method == 'GET':
        driver = webdriver.Chrome('chromedriver.exe')
        url = driver.current_url
        search = request.GET.get('search', '')
        episodes = Episode.objects.filter(title__icontains=search).order_by('-published')
        if search == "" or search == None or search == " ":
            paginator = Paginator(episodes, per_page=10)
        else:
            paginator = Paginator(episodes, per_page=100)
            
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {   
            'episodes':page_obj,            
        }
        return render(request, 'index.html', context)
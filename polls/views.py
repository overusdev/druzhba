from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_name = "list.html"
    return render(request, template_name, {'user_list': ['tom', 'jerry', 'spike']})

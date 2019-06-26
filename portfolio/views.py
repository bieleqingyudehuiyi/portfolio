from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    gallerys = Gallery.objects  # objects表示有多个,description被替换为objects
    return render(request, 'home.html', {'gallerys':gallerys})
from django.shortcuts import render
from .models import Gallery
# Create your views here.
def gallery(request):
    galleryImages = Gallery.objects
    return render(request, 'gallery/galleryHome.html', {'gallery':galleryImages})

from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    carousle = Carousel.objects.all()
    category = Category.objects.all()[:12]
    context = {
        'carousle' : carousle,
        'category' : category
    }
    return render(request,"home.html",context=context)


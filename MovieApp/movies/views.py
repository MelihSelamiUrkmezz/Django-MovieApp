from django.shortcuts import render
from .models import Category,Movies


def home(request):
    data={
        
        "kategori":Category.objects.all(),
        "filmler":Movies.objects.all()
    }
    return render(request,"index.html",data)

def movies(request):
        data={
        
        "kategori":Category.objects.all(),
        "filmler": Movies.objects.all()
    }
        return render(request,"movies.html",data)
    
def movie_details(request,id):
    data={
        "movie":Movies.objects.get(id=id)
    }  
    return render(request,"details.html",data)

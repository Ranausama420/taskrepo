from django.shortcuts import render, get_object_or_404
from .models import moviedata
import json
import ast

# Create your views here.

def index(request):
    f = open('movies.json', 'r')
    # returns JSON object as a dictionary
    data = json.load(f)
    for li in data:
        try:
            # if data already exists it dose not save
            if not moviedata.objects.filter(id=li["id"]).exists():
                dbobj=moviedata.objects.create(**li)
        except Exception as e:
            print(str(e))
    context ={"data":data,}
    return render(request, 'movieApp/index.html',context)

def detail(request,id,title):
    name=title
    movieobj = get_object_or_404(moviedata,id=id,name=name)
    rating = ast.literal_eval(movieobj.mpaaRating) #to convert string into dictionry
    genre=ast.literal_eval(movieobj.genre)
    context ={
        "data":movieobj,
        "rating":rating,
        "genre": genre
    }
    return render(request, 'movieApp/detail.html',context)
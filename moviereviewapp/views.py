from django.shortcuts import render, get_object_or_404
from .models import MovieType, Movie, Review
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import MovieForm

# Create your views here.
def index(request):
    return render(request, 'moviereviewapp/index.html')

def gettypes(request):
    type_list=MovieType.objects.all()
    return render(request, 'moviereviewapp/types.html' ,{'type_list' : type_list})

def getmovies(request):
    movies_list=Movie.objects.all()
    return render(request, 'moviereviewapp/movies.html', {'movies_list' : movies_list})

def moviedetails(request, id):
    mov=get_object_or_404(Movie, pk=id)
    reviews=Review.objects.filter(movie=id)
    context={
        'mov' : mov,
        'reviews' : reviews
    }
    return render(request, 'moviereviewapp/moviedetails.html', context=context)

def newMovie(request):
     form=MovieForm
     if request.method=='POST':
          form=MovieForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MovieForm()
     else:
          form=MovieForm()
     return render(request, 'moviereviewapp/newmovie.html', {'form': form})

def loginmessage(request):
    return render(request, 'techapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'techapp/logoutmessage.html')
import json
from math import ceil
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import User, Game, Genre, Developer, Publisher, Rating,genres
from .forms import New_Game_Form, Review_Form
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def index(request):
    lenght = ceil((Game.objects.filter(verified=True).count())/28)
    return render(request, 'gamepedia/index.html',{
        'max_page' : lenght
    })


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'gamepedia/login.html')
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["Password"]
        user = authenticate(username=username, password=password)

        # Check if authentication successful
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "gamepedia/login.html", {
                "message_login": "Invalid username and/or password."
            })


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["createusername"]

        # Ensure password matches confirmation
        password = request.POST["createpassword"]
        confirmation = request.POST["passwordconfirm"]
        if password != confirmation:
            return render(request, "gamepedia/login.html", {
                "message_register": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, password)
            user.set_password(password)
            user.save()
        except IntegrityError:
            return render(request, "gamepedia/login.html", {
                "message_register": "Username already taken."
            })
        auth_login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "gamepedia/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


@login_required
@csrf_exempt
def new_game(request):
    if request.method == 'GET':
        return render(request, 'gamepedia/new_game.html', {
            'new_game_form': New_Game_Form,
            'devs' : ['CDProjectRed', 'Ubisoft', 'konami', 'Activision', 'Square Enix', 'Electronic Arts ', 'Epic Games'],
            'pubs' : ['CDProjectRed', 'Ubisoft', 'konami', 'Activision', 'Square Enix', 'Electronic Arts ', 'Epic Games'],
        })
    elif request.method == 'POST':
        data = New_Game_Form(request.POST) 
        if data.is_valid():
            if Developer.objects.filter(developer=data.cleaned_data['dev']).exists():
                dev = Developer.objects.get(developer=data.cleaned_data['dev'])
            else:
                dev = Developer(developer=data.cleaned_data['dev'])
                dev.save()

            if Publisher.objects.filter(publisher=data.cleaned_data['pub']).exists():
                pub = Publisher.objects.get(publisher=data.cleaned_data['pub'])
            else:
                pub = Publisher(publisher=data.cleaned_data['pub'])
                pub.save()


            game_genres = request.POST.getlist('genres')
            game = Game(title=data.cleaned_data['title'], poster=data.cleaned_data['image'], description=data.cleaned_data['description'], relasedate=data.cleaned_data['release_date'], developer=dev, publisher=pub)
            game.save()
            for genre in game_genres:
                game.genres.add(Genre.objects.get(id=genre))
            game.save()
            return(HttpResponseRedirect(reverse('home')))


def getgames(request, page_number):
    games = Game.objects.filter(verified=True)
    games = sorted(games, key=lambda x: x.avg_rating(), reverse=True)
    result = [game.serialize() for game in games]
    result = Paginator(result, 28)
    return JsonResponse(result.page(page_number).object_list, safe=False)


def quicksearch(request, input):
    games = Game.objects.filter(title__contains=input, verified=True)[:5]
    result = [game.serialize() for game in games]
    return JsonResponse(result, safe=False)


def game(request, game_id):
    userreview = None
    reviewd = False
    reviews = None
    game = Game.objects.get(id=game_id)
    if request.user.is_authenticated:
        reviewd = game.ratings.filter(reviewer=request.user).exists()
        user = User.objects.get(id=request.user.id)
        reviews = game.ratings.filter(~Q(reviewer=request.user))
        is_paylist = game in user.playlist.all()
        if game.ratings.filter(reviewer=request.user).exists():
            userreview = game.ratings.get(reviewer=request.user)
    else:
        user = None
        is_paylist = None
    return render(request, 'gamepedia/game.html', {
        'game': game,
        'genres' : [genre.genre for genre in game.genres.all()],
        'review_form': Review_Form,
        'reviewd': reviewd,
        'userreview': userreview,
        'reviews': reviews,
        'avg_rating': game.serialize()['avg_rating'],
        'is_paylist': is_paylist,
    })

@csrf_exempt
@login_required
def postrating(request):
    data = json.loads(request.body)
    task = data.get('task')
    if task == 'post':
        rating_value = data.get('rating')
        review = data.get('review')
        game = Game.objects.get(id=data.get('game_id'))
        rating = Rating(reviewer=request.user, rating=float(rating_value), review=review)
        rating.save()
        game.ratings.add(rating)
        game.save()
        return JsonResponse({'message': 'rated succefully'})
    elif task == 'change':
        game = Game.objects.get(id=data.get('game_id'))
        rating = game.ratings.get(reviewer=request.user)
        rating_value = data.get('rating')
        review = data.get('review')
        rating.rating = rating_value
        rating.review = review
        rating.save()
        game.save()
        return JsonResponse({'message': 'rating changed succefully'})


def grnres(request):
    return render(request, 'gamepedia/genres.html',{
        'genres': [genre.genre for genre in Genre.objects.all()]
    })

def genregames(request, genre):
        genreo = Genre.objects.get(genre=genre)
        lenght = ceil((Game.objects.filter(genres=genreo ,verified=True).count())/28)
        return render(request, 'gamepedia/genre.html', {
            'genre': genre,
            'max_page' : lenght
        })


def getgenregames(request, genre, page_number):
    genre_object = Genre.objects.get(genre=genre)
    games = Game.objects.filter(genres=genre_object, verified=True)
    games = sorted(games, key=lambda x: x.avg_rating(), reverse=True)
    result = [game.serialize() for game in games]
    result = Paginator(result, 28)
    return JsonResponse(result.page(page_number).object_list, safe=False)


def devsearch(request, input):
    devs = Developer.objects.filter(developer__contains=input, verified=True)[:5].all()
    result = [{'dev': dev.developer} for dev in devs]
    return JsonResponse(result, safe=False)

def pubsearch(request, input):
    devs = Publisher.objects.filter(publisher__contains=input, verified=True)[:5].all()
    result = [{'pub': dev.publisher} for dev in devs]
    return JsonResponse(result, safe=False)


def getdevgames(request, genre_id, page_num):
    dev_object = Developer.objects.get(id=genre_id)
    games = Game.objects.filter(developer=dev_object, verified=True)
    games = sorted(games, key=lambda x: x.avg_rating(), reverse=True)
    result = [game.serialize() for game in games]
    result = Paginator(result, 28)
    return JsonResponse(result.page(page_num).object_list, safe=False)


def developer(request, dev_id):
    dev = Developer.objects.get(id=dev_id)
    lenght = ceil((Game.objects.filter(developer=dev ,verified=True).count())/28)
    return render(request, 'gamepedia/dev.html', {
        'dev': dev,
        'max_page' : lenght,
    })

@csrf_exempt
def addtoplaylist(request):
    data = json.loads(request.body)
    game = Game.objects.get(id=data.get('game_id'))
    user = User.objects.get(id=request.user.id)
    task = data.get('task')
    if task == 'add':
        user.playlist.add(game)
        user.save()
        return JsonResponse({'message': 'Added to playlit succefully'})
    else:
        user.playlist.remove(game)
        user.save()
        return JsonResponse({'message': 'remove from playlit succefully'})

@login_required
def playlist(request):
    user = User.objects.get(id=request.user.id)
    lenght = ceil((user.playlist.all().count()) / 28)
    return render(request, 'gamepedia/palylist.html', {
        'max_page' : lenght
    })

@login_required
def getplaylist(request, page_number):
    user = User.objects.get(id=request.user.id)
    games = user.playlist.all()
    games = sorted(games, key=lambda x: x.avg_rating(), reverse=True)
    result = [game.serialize() for game in games]
    result = Paginator(result, 10)
    return JsonResponse(result.page(page_number).object_list, safe=False)

@staff_member_required
def unverifiedgames(request):
    lenght = ceil((Game.objects.filter(verified=False).count())/28)
    return render(request, 'gamepedia/unverifiedgames.html',{
        'max_page' : lenght
    })


@staff_member_required
def getunverifeiedgames(request, page_number):
    games = Game.objects.filter(verified=False)
    result = [game.serialize() for game in games]
    result = Paginator(result, 28)
    return JsonResponse(result.page(page_number).object_list, safe=False)


def unverfiedgame(request, game_id):
    game = Game.objects.get(id=game_id)
    if game.verified == False:
        return render(request, 'gamepedia/unverifiedgame.html', {
            'game': game,
            'genres' : [genre.genre for genre in game.genres.all()],
        })
    else:
        return HttpResponse('<h1>this game is verified<h1>', safe=True)


@csrf_exempt
@staff_member_required
def verifyordelete(request):
    data = json.loads(request.body)
    game = Game.objects.get(id=data.get('game_id'))
    task = data.get('task')
    if task == 'verify':
        game.verified = True
        dev = game.developer
        pub = game.publisher
        dev.verified = True
        pub.verified = True
        dev.save()
        pub.save()
        game.save()
        return JsonResponse({'message': 'Game Verified succefully'})
    elif task == 'delete':
        game.delete()
        return JsonResponse({'message': 'Game Deleted succefully'})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('newgame', views.new_game, name='new_game'),
    path('getgames/<int:page_number>', views.getgames, name='getgames'),
    path('quicksearch/<str:input>', views.quicksearch, name='quicksearch'),
    path('game/<int:game_id>', views.game, name="game"),
    path('postrating', views.postrating, name='postrating'),
    path('genres', views.grnres, name='genres'),
    path('genres/<str:genre>', views.genregames),
    path('getgenregames/<str:genre>/<int:page_number>', views.getgenregames),
    path('quicksearchdev/<str:input>', views.devsearch),
    path('quicksearchpub/<str:input>', views.pubsearch),
    path('dev/<int:dev_id>', views.developer),
    path('getdevgames/<int:genre_id>/<int:page_num>', views.getdevgames),
    path('addtopl', views.addtoplaylist),
    path('playlist', views.playlist),
    path('getplaylist/<int:page_number>', views.getplaylist),
    path('unverifiedgames', views.unverifiedgames),
    path('getunverifeiedgame/<int:page_number>', views.getunverifeiedgames),
    path('unverifiedgame/<int:game_id>', views.unverfiedgame),
    path('verifyordelete', views.verifyordelete),
]
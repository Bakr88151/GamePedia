from django.contrib import admin
from .models import User, Game, Genre, Developer, Publisher, Rating

# Register your models here.

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Rating)

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

genres = ['Action', 'Adventure', 'Battle Royale', "Beat 'em up", 'Board game', 'Co-Op', 'Competitive', 'Educational', 'Esports', 'FPS', 'Fighting', 'Horror', 'Interactive movie', 'MMO', 'Metroidvania', 'Multiplayer', 'Party', 'Platform', 'Puzzles', 'RPG', 'Racing', 'Rhythm', 'Roguelikes', 'Sandbox', 'Shooter', 'Simulation', 'Sports', 'Stealth', 'Strategy', 'Survival', 'Tactical', 'Text Based', 'Third Person Shooting', 'Tower defense', 'Turn-based', 'Visual novel', 'open world', 'Zombie', 'Other']

def avg(lst):
    if len(lst) == 0:
        return '--'
    return float(sum(lst) / len (lst))

class User(AbstractUser):
    playlist = models.ManyToManyField('Game' ,blank=True, related_name='playlist')


class Game(models.Model):
    title = models.CharField(blank=False, max_length=256)
    poster = models.CharField(blank=False, max_length=1000)
    description = models.CharField(blank=False, max_length=4096)
    relasedate = models.DateField(auto_created=False)
    genres = models.ManyToManyField('Genre', blank=False, related_name='genres')
    ratings = models.ManyToManyField('Rating', blank=True, related_name='ratings')
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE, related_name='games')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='games')
    verified = models.BooleanField(default=False, blank=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'poster': self.poster,
            'description': self.description,
            'relasedate': self.relasedate.strftime("%b %d %Y, %I:%M %p"),
            'genres': [genre.genre for genre in self.genres.all()],
            'ratings': [{'reviewer': rating.reviewer.id, 'rating': rating.rating, 'review': rating.review} for rating in self.ratings.all()],
            'avg_rating' : self.avg_rating(),
            'developer': self.developer.developer,
            'dev_id': self.developer.id,
            'publisher': self.publisher.publisher,
            'pub_id': self.publisher.id
        }
    
    def avg_rating(self):
            rating = avg([float(rating.rating) for rating in self.ratings.all()])
            if rating == '--':
                return -1
            else:
                return round(rating, 1)
    
    def __str__(self) -> str:
        return self.title



class Genre(models.Model):
    genre = models.CharField(blank=False, choices=[(genres.index(genre) + 1, genre) for genre in genres], max_length=256, default='Other')
    def __str__(self) -> str:
        return str(self.genre)


class Developer(models.Model):
    developer = models.CharField(blank=False, unique=True, max_length=512)
    verified = models.BooleanField(default=False, blank=False)


class Publisher(models.Model):
    publisher = models.CharField(blank=False, unique=True, max_length=512)
    verified = models.BooleanField(default=False, blank=False)


class Rating(models.Model):
    reviewer = models.ForeignKey('User', on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField(blank=False ,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    review = models.CharField(blank=True, max_length=2064)

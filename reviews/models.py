from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie
# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação mínima é 0'),
            MaxValueValidator(5, 'Avaliação máxima é 5'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie
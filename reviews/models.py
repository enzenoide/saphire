from django.db import models
from django.contrib.auth.models import User
from games.models import Games
# Create your models here.
class Review(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "Reviews"
    def __str__(self):
        return self.name
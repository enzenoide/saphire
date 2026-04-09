from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    platforms = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='games/covers/', null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Games"
            
    def __str__(self):
        return self.name
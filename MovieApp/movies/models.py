from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Movies(models.Model):
    film_adi=models.CharField(max_length=150)
    film_aciklamasi=models.TextField()
    film_resmi=models.CharField(max_length=50)
    anasayfa=models.BooleanField(default=False)
    
    def __str__(self):
        return self.film_adi
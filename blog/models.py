from django.db import models
from django.utils import timezone

class Post(models.Model): #dedime ze tridy models.Model
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) # default will be current time
    published_date = models.DateTimeField(blank=True, null=True) # null - this value can be empty

    # metody jsou funkce v tride, umoznuji pracovat s objeky teto tridy; prvni argument je self, ten objekt, na kterem prave pracuji
    def publish(self):
        self.published_date = timezone.now()
        self.save() # fce save se dedi z modelu, nemusime definovat

    def __str__(self): # spacialni metoda - jak se bude prispevek prevadet na retezec
        return self.title

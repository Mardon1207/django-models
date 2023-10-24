from django.db import models


class Person(models.Model):
    first = models.TextField()
    
    last = models.TextField()
    passwoard= models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id}. {self.first} {self.last}"
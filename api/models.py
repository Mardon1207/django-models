from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()


    def __str__(self):
        return f"{self.id}. {self.name}"
    

class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.TextField(default='')
    birth_day = models.DateField()
    joined_date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        max_length=1, 
        choices=[
            ("F", "Female"),
            ("M", "Male"),
        ]
    )
    age = models.IntegerField(
        validators=[MinValueValidator(limit_value=18), MaxValueValidator(limit_value=35)]
    )
    username = models.CharField(max_length=64, unique=True)

    def __str__(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"

        return self.first_name
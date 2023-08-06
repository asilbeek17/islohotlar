from django.db import models
from django.db.models import TextChoices


class Category(models.Model):
    image = models.ImageField(upload_to='Base_Category/')
    title = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    # class PriceChopice(TextChoices):
    #     a = '0.5-1 Million'
    #     b = '1-5 Million'
    #     c = '5-10 Million'
    #     d = '10-15 Million'
    #     e = '15-20 Million'
    #     f = '20-25 Million'
    #     g = '25 + Million'

    PriceChopice = (
        ("0.5 - 1 million $", "0.5 - 1 million $"),
        ("1 - 5 million $", "1 - 5 million $"),
        ("5 - 10 million $", "5 - 10 million $"),
        ("10 - 15 million $", "10 - 15 million $"),
        ("15 - 20 million $", "15 - 20 million $"),
        ("20 - 25 million $", "20 - 25 million $"),
        ("25 - 30 million $", "25 - 30 million $"),
        ("30 + million $", "30 + million $"),
    )

    image = models.ImageField(upload_to='Project/')
    title = models.CharField(max_length=155)
    pdf = models.FileField(upload_to='PDF/')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=155, choices=PriceChopice)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    text = models.TextField()

    def __str__(self):
        return self.first_name
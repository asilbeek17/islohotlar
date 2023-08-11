from django.db import models
from django.db.models import TextChoices


class CategoryUz(models.Model):
    image = models.ImageField(upload_to='Category_UZ/')
    title = models.CharField(max_length=155, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Tavsif')

    def __str__(self):
        return self.title


class CategoryRu(models.Model):
    image = models.ImageField(upload_to='Category_RU/')
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class CategoryEN(models.Model):
    image = models.ImageField(upload_to='Category_EN/')
    title = models.CharField(max_length=155, verbose_name='Title')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title


class Project(models.Model):

    PriceChopiceUzEn = (
        ("0.5 - 1 million $", "0.5 - 1 million $"),
        ("1 - 5 million $", "1 - 5 million $"),
        ("5 - 10 million $", "5 - 10 million $"),
        ("10 - 15 million $", "10 - 15 million $"),
        ("15 - 20 million $", "15 - 20 million $"),
        ("20 - 25 million $", "20 - 25 million $"),
        ("25 - 30 million $", "25 - 30 million $"),
        ("30 + million $", "30 + million $"),
    )

    PriceChopiceRu = (
        ("0.5 - 1 миллион $", "0.5 - 1 миллион $"),
        ("1 - 5 миллион $", "1 - 5 миллион $"),
        ("5 - 10 миллион $", "5 - 10 миллион $"),
        ("10 - 15 миллион $", "10 - 15 миллион $"),
        ("15 - 20 миллион $", "15 - 20 миллион $"),
        ("20 - 25 миллион $", "20 - 25 миллион $"),
        ("25 - 30 миллион $", "25 - 30 миллион $"),
        ("30 + миллион $", "30 + миллион $"),
    )

    image = models.ImageField(upload_to='Project/')
    title_uz = models.CharField(max_length=155, verbose_name='Sarlavha')
    title_ru = models.CharField(max_length=155, verbose_name='Заголовок')
    title_en = models.CharField(max_length=155, verbose_name='Title')
    pdf_uz = models.FileField(upload_to='PDF_uzb/', verbose_name="Uzbekcha PDF")
    pdf_ru = models.FileField(upload_to='PDF_rus/', verbose_name="Русский PDF")
    pdf_en = models.FileField(upload_to='PDF_eng/', verbose_name="English PDF")
    category_uz = models.ForeignKey(to=CategoryUz, on_delete=models.CASCADE, verbose_name='Kategoriya')
    category_ru = models.ForeignKey(to=CategoryRu, on_delete=models.CASCADE, verbose_name='Категория')
    category_en = models.ForeignKey(to=CategoryEN, on_delete=models.CASCADE, verbose_name='Category')
    price_uz = models.CharField(max_length=155, choices=PriceChopiceUzEn, verbose_name='Narxi')
    price_ru = models.CharField(max_length=155, choices=PriceChopiceRu, verbose_name='Цена')
    price_en = models.CharField(max_length=155, choices=PriceChopiceUzEn, verbose_name='Price')
    description_uz = models.TextField(verbose_name='Tavsif')
    description_ru = models.TextField(verbose_name='Описание')
    description_en = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title_uz


class Contact(models.Model):
    first_name = models.CharField(max_length=155, verbose_name='Ism')
    last_name = models.CharField(max_length=155, verbose_name='Familya')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam')
    text = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.first_name
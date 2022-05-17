from django.db import models
from django.forms import ImageField


class About_Us(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name ='О нас'
        ordering = ['text']



class Choose_Us(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Почему выбирают нас'
        ordering = ['title']



class Our_Services(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Наши сервисы'
        ordering = ['title']



class Services(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name ='Наши услуги'
        ordering = ['text']



class Partners(models.Model):
    image = models.ImageField(upload_to='main', null=True, blank=True)


    class Meta:
        verbose_name ='Партнеры'
        ordering = ['image']



class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=150)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='Контакты'
        ordering = ['name']

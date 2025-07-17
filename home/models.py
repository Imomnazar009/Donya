from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Home(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WhatAreWeDoing(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='home_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title.name}'


class Catalog(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='catalog_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description}'

class Sertificate(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='sertificate_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title.name}'


class Klient(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='klient_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title.name}'

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
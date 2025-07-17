from django.db import models
from home.models import Title


class About(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about/',blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title.name}"


class AboutServices(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True)
    icon = models.ImageField(upload_to='about/',blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title.name}"


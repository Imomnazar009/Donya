from django.db import models


class Footer(models.Model):
    email = models.EmailField()
    map_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=13)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number


class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    image = models.ImageField(upload_to='social_media_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

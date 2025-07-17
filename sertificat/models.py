from django.db import models


class Sertificat(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    image = models.ImageField(upload_to='sertificats/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

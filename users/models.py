from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.png',
                                         upload_to='profile_pictures')

    def __str__(self):
        return f'Profile: {self.user}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            size = (img.height, img.width)
            img.thumbnail = size
            img.save(self.profile_picture.path, 
                    optimize=True, 
                    quality=50)
        


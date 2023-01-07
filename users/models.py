from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pics/default_profile_pic.png", upload_to="profile_pics")

    def __str__(self):
        return self.user.username + "'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300,300))
            img.save(self.image.path)




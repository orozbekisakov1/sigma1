from PIL import Image
from django.db import models

from django.db.models import Model
from django.contrib.auth.models import User


class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if delete user the profile will be deleted authomatically
    image = models.ImageField(default='user_default.jpg', upload_to='profile_image/')

    def __str__(self):
        return f'{self.user.username} profile image'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)









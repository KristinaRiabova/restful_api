from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

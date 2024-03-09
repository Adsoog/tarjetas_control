from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLES = (
        ('empleado', 'Empleado'),
        ('jefe', 'Jefe'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=100, choices=ROLES)
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


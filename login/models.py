from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    CHOISE = (
        (1, 'admin'),
        (2, 'user')
    )
    roles = models.PositiveSmallIntegerField(default=1,choices=CHOISE) 
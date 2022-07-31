from tokenize import blank_re
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    ]

    프로필 = models.ImageField(blank=True)
    성별 = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    최애메뉴 = models.TextField(default="", blank="True")
    생일 = models.DateField(null=True)
    착한사용자 = models.BooleanField(default=False)

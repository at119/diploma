from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from apps.information.models import University



# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)




class User(AbstractUser):
    GENDER_CHOICES = [
    ('M', 'МУЖСКОЙ'),
    ('F', 'ЖЕНСКИЙ'),
    ('O', 'ДРУГОЕ'),
    ]
    username = None
    email = models.EmailField("Email", unique=True)
    avatar =  models.ImageField(
        "Аватарка",
        upload_to = "user/images/",
        null=True, blank=True
    )
    mobile = models.CharField("Номер телефона", max_length=15, null=True, blank=True)
    gender = models.CharField("Пол", max_length=2, choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField("Дата рождения", null=True,blank=True)
    list_uni = models.ManyToManyField("information.University")
    


    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
            verbose_name = "Пользователь"
            verbose_name_plural = "Пользователи"
        
    def  __str__(self):
            return self.email
        
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
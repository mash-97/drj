from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None, *args, **kwargs):
        print(f"===> args: {args} kwargs: {kwargs}")
        if not email:
            raise ValueError('Users must have an email address')

        print(f"email: {email}, name: {name}, password: {password}")
        email = self.normalize_email(email)
        email = email.lower()

        return super().create_user(email, name, password)


    def create_employee(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.is_employee = True
        user.save()

        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user

# user model 
class UserAccount(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_employee = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


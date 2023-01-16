from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):

    def create_user(self,email,password,name,phone,gender, **extra_fields):

        if not email:
            raise ValueError(_('Users must have an email address'))
    
        email = self.normalize_email(email)
        user = self.model(email=email,name=name,phone=phone,gender=gender,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,name,phone,gender, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password,name,phone,gender, **extra_fields)



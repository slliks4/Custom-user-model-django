from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Myaccount_manager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,birth_day,password=None):
        if not email:
            raise ValueError("users must have an email address")
        if not username:
            return ValueError("users must have a username")
        user = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_day=birth_day,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,first_name,last_name,birth_day,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_day=birth_day,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email or username', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    birth_day = models.DateField(blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name='date joined')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='last login')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name','birth_day']
    objects = Myaccount_manager()

    def __str__(self) -> str:
        return f"{self.email} || {self.username}"
    
    def has_perm(self,perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
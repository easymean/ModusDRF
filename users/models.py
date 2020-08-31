import bcrypt
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    user_in_migrations = True

    def create(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_pwd(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(raw_password=password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250, unique=True,)
    username = models.CharField(max_length=100, unique=True,)
    phone_number = models.CharField(max_length=14, default="", blank=True,)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"  # email을 id로 사용합니다.
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return f"id: {self.pk} email: {self.email}"

    def set_pwd(self, raw_password):
        hashed_password = bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt())
        self.password = hashed_password.decode("utf-8")

    def check_pwd(self, input):
        if bcrypt.checkpw(input.encode("utf-8"), self.password.encode("utf-8")):
            return True
        else:
            return False

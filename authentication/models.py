from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str, is_staff: bool = False,
                    is_superuser: bool = False):
        """
        Creates a new user with given parameters and returns the created model.
        """
        if first_name is None:
            raise TypeError('Exception: first_name is None.')
        elif isinstance(first_name, str) and not first_name.strip():
            raise ValueError("Exception: empty first_name.")

        if last_name is None:
            raise TypeError('Exception: last_name is None.')
        elif isinstance(last_name, str) and not last_name.strip():
            raise ValueError("Exception: empty last_name.")

        if email is None:
            raise TypeError('Exception: username is None.')
        elif isinstance(email, str) and not email.strip():
            raise ValueError("Exception: empty email.")

        if password is None:
            raise TypeError('Exception: password is None.')
        elif isinstance(password, str) and not password.strip():
            raise ValueError("Exception: empty password.")

        user = self.model(first_name=first_name, last_name=last_name, email=email, is_staff=is_staff,
                          is_superuser=is_superuser)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name: str, last_name: str, email: str, password: str, is_staff=True,
                         is_superuser=True):
        """ Creates an admin, is_staff & is_superuser is True """
        user = self.create_user(first_name, last_name, email, password, True, True)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, verbose_name="Имя", null=False, blank=False)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", null=False, blank=False)
    email = models.EmailField(db_index=True, max_length=255, unique=True, verbose_name="Почта", null=False, blank=False)
    password = models.CharField(max_length=255, validators=[MinLengthValidator(8)], verbose_name="Пароль")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'is_staff']

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        s = ""
        if self.is_staff:
            s = " +staff"
        return f"User email:{self.email}" + s

    def get_full_name(self):
        """ Default method that returns only username instead of using name and surname. """
        return self.email

    def get_short_name(self):
        """ Default method that returns only username instead of using name and surname. """
        return self.email[: self.email.index("@")]

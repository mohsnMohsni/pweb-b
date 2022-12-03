# Core imports.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Local imports.
from apps.common.models.abstracts import (
    AbstractBaseModel,
    AbstractSoftDeleteModel,
)
from apps.common.validators.models import (
    birthdate_validator,
    phone_number_validator,
    national_code_validator,
    persian_character_validator,
)
from .managers import UserManager
from .constants import messages, models_verbose_names


class User(AbstractSoftDeleteModel, AbstractUser):
    username = models.CharField(
        error_messages={"unique": messages.USER_NAME_UNIQUE},
        verbose_name=models_verbose_names.USERNAME,
        validators=[phone_number_validator],
        max_length=11,
        unique=True,
    )
    national_code = models.CharField(
        verbose_name=models_verbose_names.NATIONAL_CODE,
        validators=[national_code_validator],
        max_length=10,
        blank=True,
    )
    first_name = models.CharField(
        verbose_name=models_verbose_names.FIRST_NAME,
        validators=[persian_character_validator],
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=models_verbose_names.LAST_NAME,
        validators=[persian_character_validator],
        max_length=150,
        blank=True,
    )
    full_name = models.CharField(
        verbose_name=models_verbose_names.FULL_NAME,
        max_length=300,
        blank=True,
    )
    birthdate = models.DateField(
        verbose_name=models_verbose_names.BIRTHDATE,
        validators=[birthdate_validator],
        blank=True,
        null=True,
    )

    objects = UserManager()

    class Meta:
        verbose_name = models_verbose_names.USER_VERBOSE_NAME
        verbose_name_plural = models_verbose_names.USER_VERBOSE_NAME_PLURAL

    def save(self, *args, **kwargs) -> None:
        self.full_name = self.get_full_name()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return '{} {}'.format(self.username, self.full_name)

    @property
    def has_profile(self) -> bool:
        return bool(self.national_code and self.full_name)


class VerificationCodeModel(AbstractBaseModel):
    ip = models.GenericIPAddressField(default='1.1.1.1')
    code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=12, validators=[phone_number_validator])
    updated_at = None

    class Meta:
        verbose_name = models_verbose_names.VERIFICATIONCODE_VERBOSE_NAME
        verbose_name_plural = models_verbose_names.VERIFICATIONCODE_VERBOSE_NAME_PLURAL

    def __str__(self) -> str:
        return '{} / {}'.format(self.phone_number, self.code)

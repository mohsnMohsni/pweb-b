# Core imports.
from django.db.models import QuerySet
from django.contrib.auth.models import UserManager as DefaultUserManager

# Local imports.
from apps.common.models.managers import Manager
from .querysets import UserModelQuerySet


class UserManager(Manager, DefaultUserManager):
    def get_queryset(self):
        return UserModelQuerySet(self.model, using=self._db).exclude(deleted=True)

    def deleted_set(self) -> QuerySet:
        return UserModelQuerySet(self.model, using=self._db).exclude(deleted=False)

    def without_profile(self) -> QuerySet:
        return self.get_queryset().without_profile()

    def with_profile(self) -> QuerySet:
        return self.get_queryset().with_profile()

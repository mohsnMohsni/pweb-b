# Core imports.
from django.db.models.manager import Manager as CoreManager

from .querysets import QuerySet


class Manager(CoreManager):
    def get_queryset(self) -> QuerySet:
        return QuerySet(self.model, using=self._db).exclude(deleted=True)

    def deleted_set(self) -> QuerySet:
        return QuerySet(self.model, using=self._db).filter(deleted=True)

    def delete(self) -> int:
        return self.get_queryset().delete()

    def restore(self) -> int:
        return self.deleted_set().restore()

# Core imports.
from django.db import models

from .managers import Manager
from ..constants import models_verbose_names


class AbstractSoftDeleteModel(models.Model):
    deleted = models.BooleanField(editable=False, default=False)

    objects = Manager()

    class Meta:
        abstract: bool = True

    def delete(self, using: str = None, keep_parents: bool = False) -> None:
        if self.pk is None:
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        if self.deleted:
            return
        self.deleted: bool = True
        self.save()

    def restore(self, *args: list, **kwargs: dict) -> None:
        if self.pk is None:
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        if not self.deleted:
            return
        self.deleted: bool = False
        self.save()

    def __getattribute__(self, item):
        _item = super().__getattribute__(item)
        if isinstance(_item, AbstractSoftDeleteModel) and _item.deleted:
            raise AttributeError()
        return _item


class AbstractBaseModel(AbstractSoftDeleteModel):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=models_verbose_names.CREATED_AT)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=models_verbose_names.UPDATED_AT)

    class Meta:
        abstract: bool = True

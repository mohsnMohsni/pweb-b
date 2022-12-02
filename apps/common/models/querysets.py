# Core imports.
from django.db.models.query import QuerySet as CoreQuerySet


class QuerySet(CoreQuerySet):
    def deleted_set(self) -> CoreQuerySet:
        return self.filter(deleted=True)

    def delete(self) -> int:
        return self.update(deleted=True)

    def restore(self) -> int:
        return self.update(deleted=False)

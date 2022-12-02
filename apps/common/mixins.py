# Local imports.
from apps.common.models.querysets import QuerySet


class RequestUserRelatedQuery:
    user_key = 'user'

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        _lookup = {self.user_key: self.request.user}
        return super().get_queryset(*args, **kwargs).filter(**_lookup)

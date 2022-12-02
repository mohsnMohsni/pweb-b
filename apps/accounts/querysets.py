# Local imports.
from apps.common.models.querysets import QuerySet


class UserModelQuerySet(QuerySet):
    def without_profile(self) -> QuerySet:
        return self.filter(national_code='', full_name='')

    def with_profile(self) -> QuerySet:
        return self.exclude(national_code='', full_name='')

# Standard imports
from datetime import datetime, timedelta

# Core imports.
from django.utils import timezone

# Third-party imports.
from rest_framework.serializers import (
    ValidationError as SerializerValidationError,
)

from ..models import VerificationCodeModel
from ..constants.messages import TO_MANY_REQUEST_TRY_AGAIN


def verification_code_spammer_validator(ip: str, phone_number: str) -> None:
    maximum_number_of_trys_per_day: int = 30
    critical_point: datetime = timezone.now() - timedelta(days=1)

    try_count = VerificationCodeModel.objects.filter(ip=ip, created_at__gt=critical_point).count()
    if try_count >= maximum_number_of_trys_per_day:
        raise SerializerValidationError({'ip': TO_MANY_REQUEST_TRY_AGAIN})

    try_count = VerificationCodeModel.objects.filter(phone_number=phone_number, created_at__gt=critical_point).count()
    if try_count >= maximum_number_of_trys_per_day:
        raise SerializerValidationError({'phone_number': TO_MANY_REQUEST_TRY_AGAIN})

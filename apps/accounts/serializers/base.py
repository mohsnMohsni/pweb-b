# Third-party imports.
from rest_framework import serializers

# Local imports.
from apps.common.validators.serializers import phone_number_validator
from ..models import User, VerificationCodeModel
from ..constants import variables


class BaseVerificationCodeModelSerializer(serializers.ModelSerializer):
    count_down_duration = serializers.ReadOnlyField(default=variables.AUTH_LOGIN_COUNTDOWN_DURATION)

    class Meta:
        model = VerificationCodeModel
        fields = (
            'id',
            'ip',
            'code',
            'phone_number',
            'count_down_duration',
        )
        extra_kwargs = {
            'ip': {'required': False},
            'code': {'required': False},
        }


class BaseUserModelSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[phone_number_validator], source='username')

    class Meta:
        model = User
        fields = (
            'id',
            'birthdate',
            'last_name',
            'first_name',
            'has_profile',
            'phone_number',
            'national_code',
        )

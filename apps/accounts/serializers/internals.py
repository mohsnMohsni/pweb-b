# Standard imports
from random import randint
from datetime import datetime, timedelta

# Core imports.
from django.utils import timezone
from django.db.models import Model
from django.contrib.auth.models import update_last_login

# Third-party imports.
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# Local imports.
from apps.common.helpers import get_user_ip
from apps.notifications.sms.accounts import VerificationCodeSMS
from .base import BaseUserModelSerializer, BaseVerificationCodeModelSerializer
from ..models import User, VerificationCodeModel
from ..constants.messages import VERIFY_CODE_NOT_VALID
from ..validators.serializers import verification_code_spammer_validator


class InternalVerificationCodeModelSerializer(BaseVerificationCodeModelSerializer):
    def validate(self, attrs: dict) -> dict:
        attrs['code'] = str(randint(10000, 99999))
        attrs['ip']: str = get_user_ip(self.context['request'])
        verification_code_spammer_validator(attrs['ip'], attrs['phone_number'])
        return super().validate(attrs)

    def create(self, validated_data: dict) -> Model:
        expiration_point: datetime = timezone.now() - timedelta(minutes=1, seconds=30)
        instance: Model = VerificationCodeModel.objects.filter(
            phone_number=validated_data['phone_number'], created_at__gt=expiration_point
        ).first()
        if not instance:
            instance: Model = VerificationCodeModel.objects.create(**validated_data)
        VerificationCodeSMS(instance.phone_number, instance.code).send()
        return instance


class InternalLoginOrRegisterUserByJWTModelSerializer(BaseUserModelSerializer):
    refresh_token_instance: RefreshToken = None
    code = serializers.CharField(max_length=5, write_only=True)
    refresh_token = serializers.SerializerMethodField()
    access_token = serializers.SerializerMethodField()

    class Meta(BaseUserModelSerializer.Meta):
        fields = BaseUserModelSerializer.Meta.fields + (
            'code',
            'is_employee',
            'access_token',
            'refresh_token',
            'is_origin_laboratory_employee',
            'is_reference_laboratory_employee',
        )

    def validate(self, attrs: dict) -> dict:
        expiration_point: datetime = timezone.now() - timedelta(minutes=3)
        verify_code_is_not_valid: bool = not (
            VerificationCodeModel.objects.filter(
                code=attrs['code'],
                phone_number=attrs['username'],
                created_at__gt=expiration_point,
            ).exists()
        )
        if verify_code_is_not_valid:
            raise serializers.ValidationError({'code': VERIFY_CODE_NOT_VALID})
        return super().validate(attrs)

    def create(self, validated_data: dict) -> Model:
        created: bool
        user_instance: User
        user_instance, created = User.objects.get_or_create(username=validated_data['username'])
        update_last_login(None, user_instance)
        self.refresh_token_instance = RefreshToken.for_user(user_instance)
        return user_instance

    def get_refresh_token(self, obj: Model) -> str:
        return self.refresh_token_instance.__str__()

    def get_access_token(self, obj: Model) -> str:
        return self.refresh_token_instance.access_token.__str__()

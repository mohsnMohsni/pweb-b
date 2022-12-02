# Standard imports
from datetime import date

from .models import (
    birthdate_validator as _birthdate_validator,
    phone_number_validator as _phone_number_validator,
    national_code_validator as _national_code_validator,
    persian_character_validator as _persian_character_validator,
)


def persian_character_validator(text: str) -> str:
    _persian_character_validator(text)
    return text


def birthdate_validator(_date: date) -> date:
    _birthdate_validator(_date)
    return _date


def national_code_validator(national_code: str) -> str:
    _national_code_validator(national_code)
    return national_code


def phone_number_validator(phone_number: str) -> str:
    _phone_number_validator(phone_number)
    return phone_number

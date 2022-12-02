# Standard imports
import re
from typing import Any, Callable
from datetime import date

# Core imports.
from django.core.exceptions import ValidationError as DBValidationError

from ..constants import messages


def required_validator(value: Any, function: Callable = None) -> None:
    if not value:
        raise DBValidationError(messages.THIS_FIELD_IS_REQUIRED)
    if callable(function):
        function(value)


def persian_character_validator(text: str) -> None:
    if text and re.search(r'[A-Za-z]', text):
        raise DBValidationError(messages.FULLNAME_SHOULD_BE_PERSIAN)


def birthdate_validator(_date: date) -> None:
    if _date and not (date.today().year - 120 < _date.year <= date.today().year):
        raise DBValidationError(messages.YEAR_OF_BIRTHDATE_MUST_BE_BETWEEN_1921_AND_NOW)


def national_code_validator(national_code: str) -> None:
    if national_code and len(national_code) != 10 or not str(national_code).isdigit():
        raise DBValidationError(messages.NATIONAL_CODE_NOT_VALID)


def phone_number_validator(phone_number: str) -> None:
    if phone_number and (len(phone_number) != 11 or not phone_number.isdigit() or not phone_number.startswith('09')):
        raise DBValidationError(messages.PHONE_NUMBER_NOT_VALID)

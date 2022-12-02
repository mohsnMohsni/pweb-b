# Core imports.
from django.http.request import HttpRequest


def get_user_ip(request: HttpRequest) -> str:
    x_forwarded: str = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        return x_forwarded.split(',')[0]
    return request.META.get('REMOTE_ADDR')

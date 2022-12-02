# Third-party imports.
from rest_framework.throttling import UserRateThrottle


class ClientUploadThrottle(UserRateThrottle):
    scope = 'upload'
    rate = '20/day'


class ClientRequestThrottle(UserRateThrottle):
    scope = 'client_request'
    rate = '10/day'

from .base import BaseSMS


class VerificationCodeSMS(BaseSMS):
    def __init__(self, receptor: str, verification_code: str) -> None:
        self.template: str = 'verificationSMS'
        self.token: str = verification_code
        super().__init__(receptor)

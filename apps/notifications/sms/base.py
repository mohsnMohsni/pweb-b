from ..tasks import send_sms


class BaseSMS:
    template: str

    def __init__(self, receptor: str) -> None:
        self.receptor: str = receptor

    def send(self) -> None:
        send_sms.delay(self.__dict__)

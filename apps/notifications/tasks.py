# Third-party imports.
from celery import shared_task
from kavenegar import APIException, KavenegarAPI, HTTPException


@shared_task
def send_sms(params: dict) -> str:
    try:
        params['type']: str = 'sms'
        api: KavenegarAPI = KavenegarAPI('kavenegar api')
        api.verify_lookup(params)
        return 'sms sent to {}'.format(params.get('receptor'))
    except APIException as e:
        return 'sms failed for {}: {}'.format(params.get('receptor'), str(e))
    except HTTPException as e:
        return 'sms failed for {}: {}'.format(params.get('receptor'), str(e))

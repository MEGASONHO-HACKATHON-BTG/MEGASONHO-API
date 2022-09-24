import requests
from decouple import config
from pydantic import BaseModel

from src.shared.exceptions.bad_exception import BadRequestException
from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.forbidden_exception import ForbiddenException
from src.shared.exceptions.unauthorized_exception import UnauthorizedException


class SubscriberPayload(BaseModel):
    id: int
    full_name: str
    first_name: str
    last_name: str
    phone: str
    ddd: str
    created_at: str
    live_chat: str
    referral_count: str


class BotConversaApi:

    def __init__(self):
        super().__init__()
        self._url = config("BOT_CONVERSA_URL")
        self._api_key = config("BOT_CONVERSA_API_KEY")
    
    def subscriber(self, phone: str, first_name: str, last_name: str):
        headers_payload = {
            "Content-Type": "application/json",
            "API-KEY": f"{self._api_key}"
        }

        payload = {
            "phone": phone,
            "first_name": first_name,
            "last_name": last_name,
        }

        url = f"{self._url}/subscriber/"

        req = requests.post(url=url , json=payload, headers=headers_payload)

        if req.status_code == 400:
            raise BadRequestException(message='Telefone invalido')
        if req.status_code == 401:
            raise UnauthorizedException(message='Telefone já cadastrado')
        elif req.status_code == 403:
            raise ForbiddenException(message='API-KEY invalida')

        response = req.json()

        return response
    
    def find_subscriber(self, phone: str) -> SubscriberPayload:
        headers_payload = {
            "Content-Type": "application/json",
            "API-KEY": f"{self._api_key}"
        }

        url = f"{self._url}/subscriber/{phone}"

        req = requests.get(url=url, headers=headers_payload)

        if req.status_code != 200:
            raise NotFoundException(message='Subscriber não encontrado')

        return SubscriberPayload(**req.json())

    def check_subscriber(self, phone: str):
        headers_payload = {
            "Content-Type": "application/json",
            "API-KEY": f"{self._api_key}"
        }

        url = f"{self._url}/subscriber/{phone}"

        req = requests.get(url=url, headers=headers_payload)

        return req.status_code
    
    def send_mensage(self, subscribe_id: str, code: str):
        headers_payload = {
            "Content-Type": "application/json",
            "API-KEY": f"{self._api_key}"
        }

        payload = {
            "type": "text",
            "value": f"seu código de ativação é {code}"
        }

        url = f"{self._url}/subscriber/{subscribe_id}/send_message/"

        req = requests.post(url=url, json=payload, headers=headers_payload)

        if req.status_code == 400:
            raise BadRequestException(message=f'O usuário com o id {subscribe_id} não existe')
        if req.status_code == 403:
            raise ForbiddenException(message='API-KEY invalida')

        response = req.json()

        return response

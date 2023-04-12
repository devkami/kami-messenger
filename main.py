# -*- coding: utf-8 -*-
import json
from os import getenv

from dotenv import load_dotenv

from kami_messenger.botconversa import Botconversa
from kami_messenger.email_messenger import EmailMessenger
from kami_messenger.validator import DataValidator

load_dotenv()

# data = f"""{{
#       "name":"Gmail",
#       "messages":[{{
#           "sender":"dev@kamico.com.br",
#           "recipients":["maicon@kamico.com.br"],
#           "subject":"Teste",
#           "body":"<p>Teste de mensagem</p>"
#         }}],
#       "credentials":{{
#           "login":"{getenv("EMAIL_USER")}",
#           "password":"{getenv("EMAIL_PASSWORD")}"
#       }},
#       "engine":""
# }}"""

# emailMessenger_data = json.loads(data)
# emailMessenger = EmailMessenger(**emailMessenger_data)
# emailMessenger.sendMessage()

botconversa_data = {
    'name': 'Botconversa',
    'messages': [
        {
            'sender': 'adsandroxerd@gmail.com',
            'recipients': ['+5521983144824'],
            'body': 'Esse texto não é enviado',
            'type': 'text',
        }
    ],
    'credentials': {'api-key': 'b6ba8d5c-19a1-4c38-8f5b-3966f11f2bbe'},
    'engine': '',
}
botconversa = Botconversa(**botconversa_data)
botconversa.sendMessage()

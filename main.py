# -*- coding: utf-8 -*-
import json
from os import getenv

from dotenv import load_dotenv

from kami_messenger.email_messenger import EmailMessenger

load_dotenv()

data = f"""{{
      "name":"Gmail",
      "messages":[{{
          "sender":"dev@kamico.com.br",
          "recipients":["maicon@kamico.com.br"],
          "subject":"Teste",
          "body":"<p>Teste de mensagem</p>"
        }}],
      "credentials":{{
          "login":"{getenv("EMAIL_USER")}",
          "password":"{getenv("EMAIL_PASSWORD")}"
      }},
      "engine":""
}}"""

emailMessenger_data = json.loads(data)
emailMessenger = EmailMessenger(**emailMessenger_data)
emailMessenger.sendMessage()

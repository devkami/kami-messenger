# -*- coding: utf-8 -*-
import json
from os import getenv

from dotenv import load_dotenv

from kami_messenger.whatsapp import Whatsapp

load_dotenv()


class TestWhatsapp:
    data = f"""{{
      "name":"Whatsapp",
      "messages":[{{
          "sender":"",
          "recipients":["21983144824"],
          "subject":"Teste",
          "body":"<p>Teste de mensagem</p>"
        }}],
      "credentials":{{" implementar o dicionário das credenciais necessárias para acessar o whatsapp usando getenv() para proteção dos dados ": "valor"}},
      "engine":""
    }}"""

    def test_when_email_get_valid_json_data_then_returns_new_whatsapp_messenger(
        self,
    ):
        json_data = json.loads(self.data)
        new_whatsapp_messenger = Whatsapp(**json_data)
        assert json_data == new_whatsapp_messenger.dict()

    def test_connect_whatsapp_engine(self):
        json_data = json.loads(self.data)
        new_whatsapp_messenger = Whatsapp(**json_data)
        new_whatsapp_messenger.connect()

        assert new_whatsapp_messenger.engine != None

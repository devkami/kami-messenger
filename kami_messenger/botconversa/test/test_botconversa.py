# -*- coding: utf-8 -*-
import json
from os import getenv

from dotenv import load_dotenv
from pytest import mark

from kami_messenger.botconversa import Botconversa

load_dotenv()


class TestBotconversa:
    data = f"""{{
      "name":"Botconversa",
      "messages":[{{
          "sender":"",
          "recipients":["124707269"],
          "subject":"Teste",
          "body":"<p>Teste de mensagem</p>"
        }}],
      "credentials":{{" implementar o dicionário das credenciais necessárias para acessar o whatsapp usando getenv() para proteção dos dados ": "valor"}},
      "engine":""
    }}"""

    def test_when_email_get_valid_json_data_then_returns_new_botconversa_messenger(
        self,
    ):
        json_data = json.loads(self.data)
        new_botconversa_messenger = Botconversa(**json_data)
        assert json_data == new_botconversa_messenger.dict()

    def test_connect_botconversa_engine(self):
        json_data = json.loads(self.data)
        new_botconversa_messenger = Botconversa(**json_data)
        new_botconversa_messenger.connect()

        assert new_botconversa_messenger.engine != None

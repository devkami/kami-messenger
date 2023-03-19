# -*- coding: utf-8 -*-
import json
from os import getenv

from dotenv import load_dotenv

from kami_messenger.botconversa import Botconversa

load_dotenv()


class TestBotconversa:
    data = f"""{{
      "name":"Botconversa",
      "messages":[{{
          "sender":"124707269",
          "recipients":["124707269"],
          "subject":"Teste",
          "body":"<p>Teste de mensagem</p>"
        }}],
      "credentials":{{" implementar o dicionário das credenciais necessárias para acessar o botconversa usando getenv() para proteção dos dados ": "valor"}},
      "engine":null
    }}"""

    def test_when_email_get_valid_json_data_then_returns_new_botconversa_messenger(
        self,
    ):
        json_data = json.loads(self.data)
        new_botconversa_messenger = Botconversa(**json_data)
        assert json_data == new_botconversa_messenger.dict()

    def test_when_botconversa_sucess_connect_should_returns_200(self):
        json_data = json.loads(self.data)
        new_botconversa_messenger = Botconversa(**json_data)
        status = new_botconversa_messenger.connect()

        assert status == 200

    def test_when_connect_botconversa_should_update_engine(self):
        json_data = json.loads(self.data)
        new_botconversa_messenger = Botconversa(**json_data)
        new_botconversa_messenger.connect()

        assert new_botconversa_messenger.engine != None

    def test_when_send_message_by_botconversa_should_return_sent_messages_quantity(
        self,
    ):
        json_data = json.loads(self.data)
        new_botconversa_messenger = Botconversa(**json_data)
        messages_to_send = len(new_botconversa_messenger.messages)
        sent_messages = new_botconversa_messenger.sendMessage()

        assert messages_to_send == sent_messages

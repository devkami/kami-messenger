# -*- coding: utf-8 -*-
import json
from os import getenv

from dotenv import load_dotenv
from pytest import mark

from kami_messenger.email_messenger import EmailMessenger

load_dotenv()


class TestEmailMessenger:
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

    def test_when_email_get_valid_json_data_then_returns_new_email_messenger(
        self,
    ):
        json_data = json.loads(self.data)
        new_email_messenger = EmailMessenger(**json_data)
        assert json_data == new_email_messenger.dict()

    def test_connect_email_engine(self):
        json_data = json.loads(self.data)
        new_email_messenger = EmailMessenger(**json_data)
        new_email_messenger.connect()

        assert new_email_messenger.engine != None

    @mark.skip(reason='Defined but not implemented')
    def test_when_message_get_invalid_json_data_then_returns_none(self):
        pass

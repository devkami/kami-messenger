# -*- coding: utf-8 -*-
import logging
import os
import traceback
from urllib.parse import urljoin

import requests
from dotenv import load_dotenv
from kami_logging import benchmark_with, logging_with
from pydantic import validator

from kami_messenger.messenger import Messenger, RecipientFormatError
from kami_messenger.validator import DataValidator, IdBotconversaMissingError

botconversa_messenger_logger = logging.getLogger('Botconversa Messenger')
load_dotenv()


class Botconversa(Messenger):
    @logging_with(botconversa_messenger_logger)
    @benchmark_with(botconversa_messenger_logger)
    def _sendMessage(self, message):
        try:
            self.connect()

            #
            birthday_person = 'João'

            # inserindo datas que serão enviados ao aniversariante
            image = 'encurtador.com.br/dFSXY'

            # configurando parâmetros de data para realizar a requisição
            data = {
                'type': 'text',
                'value': f'Feliz aniversário {birthday_person} {image}',
            }

            self.engine = data

            # Implementar o envio de mensagens pelo botconversa usando o atributo 'engine'
            # Exemplo: self.engine.send_message()
            ...
        except Exception as e:
            botconversa_messenger_logger.error(traceback.format_exc())
            raise
        finally:
            botconversa_messenger_logger.info(
                f'Message Sucessufully Sent To {message.recipients}'
            )

    def _validate_message_recipients(self, message):
        for recipient in message.recipients:
            try:
                data = DataValidator(recipient)
                data._isIdBotconversa()
            except IdBotconversaMissingError:
                e = RecipientFormatError(
                    recipient,
                    f'Recipient {recipient} should be an valid botconversa contact',
                )
                botconversa_messenger_logger.error(f'{e.message} - {e.args}')
                raise
            except Exception as e:
                botconversa_messenger_logger.error(traceback.format_exc())
            finally:
                return message

    @validator('messages', pre=True, each_item=True)
    @classmethod
    def recipientsValid(cls, message):
        cls._validate_messages_recipients(message)

    @logging_with(botconversa_messenger_logger)
    @benchmark_with(botconversa_messenger_logger)
    def connect(self):
        try:
            engine = None
            url = f'https://backend.botconversa.com.br/webhook/subscriber/{self.subscriber_id}/send_message/'

            # configurando parâmetros de headers para realizar authentication
            # o param api_key na verdade a plataforma utiliza a chave webhook como chave
            headers = {
                'accept': 'application/json',
                'api-key': os.getenv('botconversa_webhook_key'),
            }

            # realizando a requisição com o método post e seus argumentos
            response = requests.get(url, headers=headers, data=engine)
            if response.status_code >= 200 and response.status_code < 299:
                self.engine = engine
                botconversa_messenger_logger.info(f'Successfully connected')

        except Exception as e:
            botconversa_messenger_logger.error(traceback.format_exc())
            raise


if __name__ == '__main__':
    api_key = ''
    baseurl = 'https://backend.botconversa.com.br/api/v1/webhook'
    subscriber_id = '98213097'

    bot = Botconversa()
    bot._sendMessage('Teste')

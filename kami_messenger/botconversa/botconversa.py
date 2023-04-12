# -*- coding: utf-8 -*-
import json
import logging
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
            # Implementar a conexão com o serviço do botconversa e atualizar a variavel engine com o objeto responsavel por enviar mensagens
        except Exception as e:
            botconversa_messenger_logger.error(traceback.format_exc())
            raise
        else:
            self.engine = engine
            botconversa_messenger_logger.info(f'Success Connected')

    @logging_with(botconversa_messenger_logger)
    @benchmark_with(botconversa_messenger_logger)
    def _sendMessage(self, message):
        try:
            message_data = {'type': message.type, 'value': message.body}
            for recipient in message.recipients:
                url = urljoin(
                    'https://backend.botconversa.com.br/api/v1/webhook',
                    f'webhook/subscriber/{recipient}/send_message/',
                )
                headers = {
                    'accept': 'application/json',
                    'api-key': self.credentials['api-key'],
                    'Content-Type': 'application/json',
                }
                response = requests.post(
                    url, headers=headers, data=json.dumps(message_data)
                )
                botconversa_messenger_logger.info(
                    f'Try to send message to: {recipient} | Status: {response.status_code}'
                )
        except Exception as e:
            botconversa_messenger_logger.error(traceback.format_exc())
            raise
        finally:
            botconversa_messenger_logger.info(
                f'Message Sucessufully Sent To {message.recipients}'
            )

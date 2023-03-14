# -*- coding: utf-8 -*-
import logging
import traceback

from dotenv import load_dotenv
from kami_logging import benchmark_with, logging_with
from pydantic import validator

from kami_messenger.messenger import Messenger, RecipientFormatError

botconversa_messenger_logger = logging.getLogger('Botconversa Messenger')
load_dotenv()


class Botconversa(Messenger):
    def _isIdBotconversa(value):
        # Implementar uma função que verifica se o id do bot conversa é válido
        ...

    def _validate_messages_recipients(self, message):
        for recipient in message.recipients:
            if not self._isIdBotconversa(recipient):
                raise RecipientFormatError(
                    recipient,
                    f'Recipient {recipient} should be an valid botconversa id',
                )
            else:
                return message

    @validator('messages', pre=True, each_item=True)
    @classmethod
    def recipientsValid(cls, message):
        cls._validate_messages_recipients(message)

    @logging_with(botconversa_messenger_logger)
    @benchmark_with(botconversa_messenger_logger)
    def connect(self):
        # Implementar
        ...

    @logging_with(botconversa_messenger_logger)
    @benchmark_with(botconversa_messenger_logger)
    def _sendMessage(self, message):
        try:
            self.connect()
            # implementar
            ...
        except Exception as e:
            botconversa_messenger_logger.error(traceback.format_exc())
            raise
        finally:
            botconversa_messenger_logger.info(
                f'Message Sucessufully Sent To {message.recipients}'
            )

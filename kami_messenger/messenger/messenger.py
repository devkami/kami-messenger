# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, validator


class RecipientFormatError(Exception):
    """Custom error that is raised when a recipients doesn't have the rigth format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Message(BaseModel):
    sender: str
    recipients: List[str]
    subject: Optional[str]
    body: str


class Messenger(ABC, BaseModel):
    name: str
    messages: List[Message] = []
    credentials: Dict
    engine: Any = None

    @abstractmethod
    def _validate_message_recipients(message) -> Message:
        ...

    @classmethod
    @abstractmethod
    def recipientsValid(cls, message):
        ...

    @abstractmethod
    def connect(self) -> int:
        ...

    @abstractmethod
    def _sendMessage(self, message) -> int:
        ...

    def sendMessage(self, messages=None) -> int:
        sent_messages = 0
        selected_messages = self.messages
        if messages:
            selected_messages = messages

        for message in selected_messages:
            try:
                sent_messages += 1 if self._sendMessage(message) == 200 else 0
            except Exception as e:
                raise e

        return sent_messages

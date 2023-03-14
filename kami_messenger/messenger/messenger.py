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
    def _validate_messages_recipients(message):
        ...

    @classmethod
    @abstractmethod
    def recipientsValid(cls, message):
        ...

    @abstractmethod
    def connect(self) -> str:
        ...

    @abstractmethod
    def _sendMessage(self, messages=None):
        ...

    def sendMessage(self, messages=None):
        selected_messages = self.messages
        if messages:
            selected_messages = messages

        for message in selected_messages:
            self._sendMessage(message)

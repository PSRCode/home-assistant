from dependency_injector.wiring import inject
from dataclasses import dataclass
from enum import Enum
from functools import partial
from typing import Union, List


class COMMAND_TYPES(Enum):
    FCT = 1
    OBJECT = 2


class BaseCommand:
    @inject
    def __init__(
        self,
        command_str: Union[str, List[str]],
        type: COMMAND_TYPES,
        fct: partial = None,
    ) -> None:
        self.command_str = command_str
        self.type = type
        self.fct = fct

    def execute(self, command_text: str = None):
        if command_text is None:
            self.fct()
        else:
            self.fct(command_text)

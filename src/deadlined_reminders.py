from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from datetime import datetime

from dateutil.parser import parse


class DeadlinedMetaReminder(Iterable):

    def __init__(self, metaclass=ABCMeta):
        self.metaclass = metaclass

    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(ABC, Iterable):

    @abstractmethod
    def is_due(self) -> bool:
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any(attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True


class DateReminder(DeadlinedReminder):

    def __init__(self, text: str, date: str):
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self) -> bool:
        return self.date <= datetime.now()

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

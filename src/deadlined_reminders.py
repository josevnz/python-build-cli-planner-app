from abc import ABCMeta, abstractmethod
from collections.abc import Iterable


class DeadlinedMetaReminder(Iterable):

    def __init__(self, metaclass=ABCMeta):
        self.metaclass = metaclass

    @abstractmethod
    def is_due(self):
        pass

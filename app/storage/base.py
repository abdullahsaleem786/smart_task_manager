from abc import ABC, abstractmethod
from typing import List
from app.models.task import Task


class BaseStore(ABC):

    @abstractmethod
    def load(self) -> List[Task]:
        pass

    @abstractmethod
    def save(self, tasks: List[Task]) -> None:
        pass

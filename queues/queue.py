from abc import abstractmethod, ABCMeta
from item import AbstractQueueItem


class AbstractQueue(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, definition: dict | None):
        # define a connection to the data source
        pass

    @abstractmethod
    def add(self, item: AbstractQueueItem):
        # add an item to the queue
        pass

    @abstractmethod
    def get_next(self) -> AbstractQueueItem:
        # get the next item in the queue
        # return None if the queue is empty
        # do not forget to change the status of the item
        pass

    @abstractmethod
    def get_items(self) -> list[AbstractQueueItem]:
        # get items from the queue, specify filter rules
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        # check if the queue is empty
        pass

    @abstractmethod
    def update_item(self, item, status):
        # update an item in the queue
        pass

    @abstractmethod
    def remove_item(self):
        # remove an item from the queue
        pass

    def validate_item(self, item) -> bool:
        # validate an item
        pass

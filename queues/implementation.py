from typing import Any, Sequence, Literal
from queues.queue import AbstractQueue
from queues.item import AbstractQueueItem
from design_patterns.structural.decorators.method_calls import print_after_method
from datetime import datetime


class DictQueue(AbstractQueue):
    def __init__(self, data: list):
        self.data = data

    @print_after_method
    def add(self, item: AbstractQueueItem):
        self.data.append(item)

    @print_after_method
    def get_next(self) -> AbstractQueueItem:

        next_item = next(
            (item for item in self.data if item.status == 'pending'), None)

        if not next_item:
            return None

        next_item.status = "processing"

        return next_item

    def get_items(self) -> Sequence[AbstractQueueItem]:
        return self.data

    def is_empty(self):
        return len(self.data) == 0

    def has_pending_items(self):
        return any(item.status == 'pending' for item in self.data)

    @print_after_method
    def remove_item(self, item: AbstractQueueItem):
        self.data.remove(item)

    @print_after_method
    def update_item(self, item: AbstractQueueItem, status):
        item.status = status

    def __str__(self) -> str:
        return '\n'.join(f'{index} {str(item)}' for index, item in enumerate(self.data, 1))


class Item(AbstractQueueItem):
    def __init__(self, data: dict, output_data: dict = None,
                 status: Literal['pending', 'processing',
                                 'success', 'error'] = 'pending',
                 creation_date: datetime = datetime.now()):
        self.data = data
        self._status = status
        self.output_data = output_data
        self.creation_date = creation_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: Literal['pending', 'processing', 'success', 'error']):
        self._status = value

    def validate_data(self, data_definition):
        pass

    def __str__(self) -> str:
        return f'Item: {self.data}, Status: {self.status}, creation_date: {self.creation_date}'


if __name__ == '__main__':
    print('==> instantiate queue')

    queue_items = []
    queue = DictQueue(queue_items)

    print('==> instantiate items')
    test_items = [Item(data={'name': f'test {value}'})
                  for value in range(1, 4)]

    for item in test_items:
        print('==> adding item', item)
        queue.add(item)

    while queue.has_pending_items():
        next_item = queue.get_next()
        print('processing item', next_item)

        queue.update_item(next_item, 'success')

    if not queue.has_pending_items():
        print('==> queue is empty')

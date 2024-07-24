from enum import Enum
from typing import TypeVar, Generic

T = TypeVar('T')


class ResultStatus(Enum):
    SUCCESS = 'ok',
    FAILURE = 'failure'
    BUSINESS_EXCEPTION = 'business_exception'


class Result(Generic[T]):
    def __init__(self, status, value: T = None, exception=None, message=None):
        self.status = status
        self._value = value
        self.exception = exception
        self.message = message

    @classmethod
    def success(cls, value=None, message=None):
        return cls(ResultStatus.SUCCESS, value, None, message)

    @classmethod
    def failure(cls, exception=None, message=None):
        if exception is None and message is None:
            raise ValueError('Either exception or message must be provided')

        return cls(ResultStatus.FAILURE, None, exception, message)

    @classmethod
    def business_exception(cls, message):
        return cls(ResultStatus.BUSINESS_EXCEPTION, None, message=message)

    @property
    def is_success(self):
        return self.status == ResultStatus.SUCCESS

    @property
    def is_failure(self):
        return self.status == ResultStatus.FAILURE

    @property
    def is_business_exception(self):
        return self.status == ResultStatus.BUSINESS_EXCEPTION

    @property
    def value(self):
        return self._value

    def is_of_status(self, status):
        return self.status == status

    def __str__(self):
        return f"Status: {self.status}, Value: {self._value}, Exception: {self.exception}, Message: {self.message}"


if __name__ == '__main__':
    success = Result.success(1)
    print(success)
    assert success.is_success

    success_with_message = Result.success([], 'search returned no results')
    print(success_with_message)
    assert success_with_message.is_success

    failure_with_exception = Result.failure(ValueError('search failed'))
    print(failure_with_exception)
    assert failure_with_exception.is_failure

    failure_with_message = Result.failure(None, 'search failed')
    print(failure_with_message)
    assert failure_with_message.is_failure

    business_exception = Result.business_exception(
        'items in the cart are not available')
    print(business_exception)
    assert business_exception.is_business_exception

    other_status = Result('other', 'ok')
    print(other_status)
    assert other_status.is_of_status('other')

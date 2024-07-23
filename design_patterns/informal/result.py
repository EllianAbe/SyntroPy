from enum import Enum
from typing import TypeVar, Generic

T = TypeVar('T')


class ResultType(Enum):
    SUCCESS = 'ok',
    FAILURE = 'failure'
    BUSINESS_EXCEPTION = 'business_exception'


class Result(Generic[T]):
    def __init__(self, status, value=None, exception=None, message=None):
        self.status = status
        self._value = value
        self.exception = exception
        self.message = message

    @classmethod
    def success(cls, value=None, message=None):
        return cls(ResultType.SUCCESS, value, None, message)

    @classmethod
    def failure(cls, exception=None, message=None):
        if exception is None and message is None:
            raise ValueError('Either exception or message must be provided')

        return cls(ResultType.FAILURE, None, exception, message)

    @classmethod
    def business_exception(cls, message):
        return cls(ResultType.BUSINESS_EXCEPTION, None, message=message)

    def is_success(self):
        return self.status == 'success'

    def is_failure(self):
        return self.status == 'failure'

    def is_business_exception(self):
        return self.status == 'business_exception'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        raise ValueError('Value of Result cannot be changed after creation')

    def __str__(self):
        return f"Status: {self.status}, Value: {self._value}, Exception: {self.exception}, Message: {self.message}"


if __name__ == '__main__':
    success = Result.success(1)
    print(success)

    success_with_message = Result.success([], 'search returned no results')
    print(success_with_message)

    failure_with_exception = Result.failure(ValueError('search failed'))
    print(failure_with_exception)

    failure_with_message = Result.failure(None, 'search failed')
    print(failure_with_message)

    business_exception = Result.business_exception(
        'items in the cart are not available')
    print(business_exception)

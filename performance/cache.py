
import decorators.metrics as metrics
import functools


@metrics.profile
def cachenacci_sequence(n):
    @functools.cache
    def fibonacci(i):
        return i if i < 2 else fibonacci(i - 2) + fibonacci(i - 1)

    return [fibonacci(i) for i in range(n)]


@ metrics.profile
def fibonacci_sequence(n):
    def fibonacci(i):
        return i if i < 2 else fibonacci(i - 2) + fibonacci(i - 1)

    return [fibonacci(i) for i in range(n)]


if __name__ == '__main__':
    fibonacci_sequence(30)
    cachenacci_sequence(1000)

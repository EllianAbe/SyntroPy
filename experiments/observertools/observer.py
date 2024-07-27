# Observer Design Pattern + Mediator Design Pattern + Decorator Design Pattern
class DecoratorsManager():
    def __init__(self, topic_subscribers_dict: dict[str, list] = {}):
        self.topic_subscribers_dict = topic_subscribers_dict

    def notify(self, route):
        if route not in self.topic_subscribers_dict:
            self.topic_subscribers_dict[route] = []

        def decorator(notifier_method):
            def wrapper(instance, state, *args, **kwargs):
                result = notifier_method(
                    instance, state, *args, **kwargs)

                for subscriber, method in self.topic_subscribers_dict[route]:
                    method(subscriber, instance)
                return result
            return wrapper
        return decorator

    def subscriber(self, route, method=lambda subscriber, publisher: subscriber.update(publisher)):
        def decorator(subscriber_class):
            if route not in self.topic_subscribers_dict:
                self.topic_subscribers_dict[route] = []

            def wrapper(*args, **kwargs):
                instance = subscriber_class(*args, **kwargs)
                self.topic_subscribers_dict[route].append((instance, method))
                return instance

            return wrapper

        return decorator


class Observer():
    def __init__(self):
        self.topic_subscribers_dict: dict[str, list] = {}
        self.decorators = DecoratorsManager(self.topic_subscribers_dict)
        self.notify = self.decorators.notify
        self.subscriber = self.decorators.subscriber


observer = Observer()


class Publisher():
    @ observer.notify(route='topic1')
    def notify(self, state):
        self.state = state


@observer.subscriber(route='topic1')
class Subscriber():
    def update(self, publisher):
        print(f'receive update: {publisher.state}')


publisher = Publisher()

subscriber = Subscriber()
Subscriber()
Subscriber()
publisher.notify('hello')

pass

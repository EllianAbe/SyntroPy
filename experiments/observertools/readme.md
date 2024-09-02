

**ObserverTools README**
==========================

**Overview**
------------

This repository contains an implementation of the Observer Design Pattern, Mediator Design Pattern, and Decorator Design Pattern in Python. The main concept is an Observation Mediator that facilitates the relationship between Publishers and Subscribers using decorators.

**Key Concepts**
----------------

### 1. Observer Design Pattern

The Observer Design Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

### 2. Mediator Design Pattern

The Mediator Design Pattern defines an object that encapsulates how a set of objects interact with each other. It acts as an intermediary between the objects, allowing them to communicate without having a direct reference to each other.

### 3. Decorator Design Pattern

The Decorator Design Pattern allows an object to add or modify its behavior dynamically by wrapping it with another object that provides the new behavior.

**Observation Mediator**
------------------------

The Observation Mediator is the central component of this implementation. It acts as a mediator between Publishers and Subscribers, allowing them to communicate with each other without having a direct reference.

The Observation Mediator uses decorators to facilitate the communication between Publishers and Subscribers. When a Publisher notifies the Observation Mediator of a change, the mediator uses the decorators to notify all the Subscribers that are interested in the change.

**Usage**
---------

To use the Observation Mediator, you need to create a Publisher and one or more Subscribers. The Publisher notifies the Observation Mediator of changes, and the Subscribers register with the mediator to receive notifications.

Here is an example:
```python
# Create a publisher
publisher = Publisher()

# Create a subscriber
subscriber = Subscriber()

# Register the subscriber with the observation mediator
observation_mediator = ObservationMediator()
observation_mediator.subscribe(subscriber)

# Notify the observation mediator of a change
publisher.notify(observation_mediator, 'hello')

# The subscriber will receive the notification
```
**Benefits**
------------

The Observation Mediator provides several benefits, including:

* Decoupling: The Publisher and Subscribers are decoupled from each other, allowing them to change independently without affecting each other.
* Flexibility: The Observation Mediator allows for multiple Subscribers to be registered for the same notification, making it easy to add or remove Subscribers as needed.
* Reusability: The Observation Mediator can be reused in different contexts, making it a flexible and reusable solution.

**Conclusion**
--------------

The Observation Mediator is a powerful tool for managing the relationship between Publishers and Subscribers. By using decorators to facilitate communication, it provides a flexible and reusable solution for a wide range of applications.
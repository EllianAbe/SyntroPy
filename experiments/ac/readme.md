**Air Conditioner Control System**
=====================================

**Overview**
------------

This project demonstrates a control system for an air conditioner using various programming concepts, including state machines, parallelism, and APIs.

**Main Concepts**
-----------------

### Event-Driven State Machine

The air conditioner's state is managed using an event-driven state machine approach. The state machine is implemented in states.py and defines the possible states of the air conditioner, such as ON, OFF, COOLING, and HEATING. The state machine responds to events, such as remote control button presses or temperature changes, and transitions between states accordingly.

### Parallelism

To simulate the air conditioner's operation, we use parallelism to run multiple tasks concurrently. The `server.py` file uses the `threading` module to create separate threads for running the air conditioner's control logic and the API server.]



### State Base Class

The `State` base class is a crucial component of the air conditioner's state machine. It serves as an abstraction, defining the common interface and behavior for all states.

#### Interface

The `State` base class defines an interface that all concrete states must implement. This interface includes two methods:

* `handle(self, air_conditioner)`: This method is called when the air conditioner is in a particular state. It allows the state to perform any necessary actions or transitions.
* `on_event(self, air_conditioner, event)`: This method is called when an event occurs, such as a button press or a temperature change. It allows the state to respond to the event and potentially transition to a new state.

By defining this interface, the `State` base class ensures that all concrete states have a consistent structure and behavior.

#### Abstraction

The `State` base class also provides abstraction, hiding the implementation details of the concrete states. This allows the air conditioner's control logic to interact with the states without knowing the specific details of each state.

For example, the `AirConditioner` class can call the `handle` method on the current state without knowing whether it's an `OffState`, `CoolingState`, or `HeatingState`. This decouples the control logic from the specific states, making the system more modular and easier to maintain.

#### Benefits

The `State` base class provides several benefits:

**Encapsulation**: The state's behavior and data are encapsulated within the state object, making it easier to modify or replace states without affecting the rest of the system.
**Polymorphism**: The `State` base class allows for polymorphic behavior, where different states can respond to the same events or method calls in different ways.
**Extensibility**: Adding new states is straightforward, as they can simply implement the `State` interface and be used by the air conditioner's control logic.

By using a base class to define the state interface and behavior, we can create a more modular, extensible, and maintainable state machine.

### API

The project includes a simple API implemented using FastAPI. The API provides endpoints for controlling the air conditioner, such as turning it on/off, setting the temperature, and retrieving the current state. The API is defined in `server.py`.

### Remote Control

The `remote_control.py` file demonstrates a remote control interface for the air conditioner. The remote control uses the API to send commands to the air conditioner.

**Directory Structure**
------------------------

* `server.py`: API server implementation.
* `states.py`: State machine implementation.
* `remote_control.py`: Remote control interface.

**Running the Project**
-----------------------

To run the project, execute the following commands:

1. `python server.py` to start the API server.
2. `python remote_control.py` to start the remote control interface.

**Example Use Cases**
---------------------

* Use the API to turn on the air conditioner: `curl -X POST http://localhost:1234/events -H "Content-Type: application/json" -d {"event": "turn on"}`
   -d '{"productId": 123456, "quantity": 100}' `
* Use the remote control to set the temperature: `python remote_control.py`

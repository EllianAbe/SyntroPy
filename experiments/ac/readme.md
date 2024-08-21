**Air Conditioner Control System**
=====================================

**Overview**
------------

This project demonstrates a control system for an air conditioner using various programming concepts, including state machines, parallelism, and APIs.

**Main Concepts**
-----------------

### State Machine

The air conditioner's state is managed using a finite state machine (FSM) approach. The FSM is implemented in `states.py` and defines the possible states of the air conditioner, such as `ON`, `OFF`, `COOLING`, and `HEATING`. The FSM ensures that the air conditioner can only transition between valid states.

### Parallelism

To simulate the air conditioner's operation, we use parallelism to run multiple tasks concurrently. The `server.py` file uses the `threading` module to create separate threads for running the air conditioner's control logic and the API server.

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

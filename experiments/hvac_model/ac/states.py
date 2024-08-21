import threading


class State:
    """Abstract base class representing a state."""

    def handle(self, air_conditioner):
        raise NotImplementedError

    def on_event(self, air_conditioner, event):
        raise NotImplementedError


class OffState(State):
    def handle(self, air_conditioner):
        print("Air conditioner is off.")

    def on_event(self, air_conditioner, event):
        if event == "turn_on":
            air_conditioner.state = CoolingState()
            print("Transitioning to Cooling State")


class CoolingState(State):
    def handle(self, air_conditioner):
        print(
            f"Cooling... Current temperature: {air_conditioner.current_temp}°C")

        if air_conditioner.current_temp > air_conditioner.desired_temp:
            air_conditioner.current_temp -= 1

        if air_conditioner.current_temp <= air_conditioner.desired_temp:
            air_conditioner.state = StandbyState()
            print("Desired temperature reached. Transitioning to Standby State")

    def on_event(self, air_conditioner, event):
        if event == "turn_off":
            air_conditioner.state = OffState()
            print("Turning off. Transitioning to Off State")


class StandbyState(State):
    def handle(self, air_conditioner):
        print(
            f"Standby mode. Current temperature: {air_conditioner.current_temp}°C")

        if air_conditioner.current_temp - air_conditioner.desired_temp > air_conditioner.stand_by_tolerance:
            print("Temperature too high. Transitioning to Cooling State")
            air_conditioner.state = CoolingState()

    def on_event(self, air_conditioner, event):
        if event == "turn_off":
            air_conditioner.state = OffState()
            print("Turning off. Transitioning to Off State")

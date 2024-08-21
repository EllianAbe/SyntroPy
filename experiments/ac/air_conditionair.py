from states import OffState


class AirConditioner:
    def __init__(self):
        self.state = OffState()  # Initial state
        self.current_temp = 26  # Initial temperature
        self.desired_temp = 23  # Desired temperature
        self.stand_by_tolerance = 1.5  # Tolerance

    def on_event(self, event):
        """Pass the event to the current state to handle it."""
        self.state.on_event(self, event)

    def run(self):
        """Run the handle method of the current state."""
        self.current_temp += .3
        self.current_temp = round(self.current_temp, 1)
        self.state.handle(self)

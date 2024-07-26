# Observer pattern implementation

class TrafficLight:
    def __init__(self):
        self._observers = []
        self._state = 'red'  # Initial state

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"{observer} has joined the traffic light.")

    def remove_observer(self, observer):
        self._observers.remove(observer)
        print(f"{observer} has left the traffic light.")

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def change_state(self, state):
        self._state = state
        self.notify_observers()


class Driver:
    def __init__(self, name):
        self.name = name

    def update(self, light_state):
        if light_state == 'green':
            print(f"{self.name} sees the light is green and proceeds.")
        else:
            print(f"{self.name} sees the light is {light_state} and waits.")

    def __str__(self) -> str:
        return self.name


# Example usage
if __name__ == "__main__":
    # Create a traffic light and drivers
    traffic_light = TrafficLight()
    driver1 = Driver('Driver 1')
    driver2 = Driver('Driver 2')

    # add drivers(subscribers) to traffic light (publisher) to observe the state (subject)
    traffic_light.add_observer(driver1)
    traffic_light.add_observer(driver2)

    traffic_light.change_state('red')
    traffic_light.change_state('yellow')
    traffic_light.change_state('green')

    # remove driver from traffic light
    traffic_light.remove_observer(driver1)
